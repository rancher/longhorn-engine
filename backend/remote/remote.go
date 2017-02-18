package remote

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net"
	"net/http"
	"strconv"
	"time"

	"github.com/Sirupsen/logrus"
	"github.com/rancher/longhorn/replica/rest"
	"github.com/rancher/longhorn/rpc"
	"github.com/rancher/longhorn/types"
	"github.com/rancher/longhorn/util"
)

var (
	pingInveral   = 2 * time.Second
	timeout       = 30 * time.Second
	requestBuffer = 1024
)

func New() types.BackendFactory {
	return &Factory{}
}

type Factory struct {
}

type Remote struct {
	types.ReaderWriterAt
	name        string
	pingURL     string
	replicaURL  string
	httpClient  *http.Client
	closeChan   chan struct{}
	monitorChan types.MonitorChannel
}

func (r *Remote) Close() error {
	logrus.Infof("Closing: %s", r.name)
	return r.doAction("close", "")
}

func (r *Remote) open() error {
	logrus.Infof("Opening: %s", r.name)
	return r.doAction("open", "")
}

func (r *Remote) Snapshot(name string) error {
	logrus.Infof("Snapshot: %s %s", r.name, name)
	return r.doAction("snapshot", name)
}

func (r *Remote) doAction(action, name string) error {
	body := io.Reader(nil)
	if name != "" {
		buffer := &bytes.Buffer{}
		if err := json.NewEncoder(buffer).Encode(&map[string]string{"name": name}); err != nil {
			return err
		}
		body = buffer
	}

	req, err := http.NewRequest("POST", r.replicaURL+"?action="+action, body)
	if err != nil {
		return err
	}

	if name != "" {
		req.Header.Add("Content-Type", "application/json")
	}

	resp, err := r.httpClient.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return fmt.Errorf("Bad status: %d %s", resp.StatusCode, resp.Status)
	}

	return nil
}

func (r *Remote) Size() (int64, error) {
	replica, err := r.info()
	if err != nil {
		return 0, err
	}
	return strconv.ParseInt(replica.Size, 10, 0)
}

func (r *Remote) SectorSize() (int64, error) {
	replica, err := r.info()
	if err != nil {
		return 0, err
	}
	return replica.SectorSize, nil
}

func (r *Remote) RemainSnapshots() (int, error) {
	replica, err := r.info()
	if err != nil {
		return 0, err
	}
	if replica.State != "open" && replica.State != "dirty" && replica.State != "rebuilding" {
		return 0, fmt.Errorf("Invalid state %v for counting snapshots", replica.State)
	}
	return replica.RemainSnapshots, nil
}

func (r *Remote) GetRevisionCounter() (int64, error) {
	replica, err := r.info()
	if err != nil {
		return 0, err
	}
	if replica.State != "open" && replica.State != "dirty" {
		return 0, fmt.Errorf("Invalid state %v for getting revision counter", replica.State)
	}
	return replica.RevisionCounter, nil
}

func (r *Remote) SetRevisionCounter(counter int64) error {
	body := &bytes.Buffer{}
	if err := json.NewEncoder(body).Encode(&map[string]int64{"counter": counter}); err != nil {
		return err
	}

	req, err := http.NewRequest("POST", r.replicaURL+"?action=setrevisioncounter", body)
	if err != nil {
		return err
	}
	req.Header.Add("Content-Type", "application/json")

	resp, err := r.httpClient.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return fmt.Errorf("Bad status: %d %s", resp.StatusCode, resp.Status)
	}

	return nil
}

func (r *Remote) info() (rest.Replica, error) {
	var replica rest.Replica
	req, err := http.NewRequest("GET", r.replicaURL, nil)
	if err != nil {
		return replica, err
	}

	resp, err := r.httpClient.Do(req)
	if err != nil {
		return replica, err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return replica, fmt.Errorf("Bad status: %d %s", resp.StatusCode, resp.Status)
	}

	err = json.NewDecoder(resp.Body).Decode(&replica)
	return replica, err
}

func (rf *Factory) Create(address string) (types.Backend, error) {
	logrus.Infof("Connecting to remote: %s", address)

	controlAddress, dataAddress, _, err := util.ParseAddresses(address)
	if err != nil {
		return nil, err
	}

	r := &Remote{
		name:       address,
		replicaURL: fmt.Sprintf("http://%s/v1/replicas/1", controlAddress),
		pingURL:    fmt.Sprintf("http://%s/ping", controlAddress),
		httpClient: &http.Client{
			Timeout: timeout,
		},
		closeChan:   make(chan struct{}, 1),
		monitorChan: make(types.MonitorChannel),
	}

	replica, err := r.info()
	if err != nil {
		return nil, err
	}

	if replica.State != "closed" {
		return nil, fmt.Errorf("Replica must be closed, Can not add in state: %s", replica.State)
	}

	conn, err := net.Dial("tcp", dataAddress)
	if err != nil {
		return nil, err
	}

	rpc := rpc.NewClient(conn)
	r.ReaderWriterAt = rpc

	if err := r.open(); err != nil {
		return nil, err
	}

	go r.monitorPing(rpc)

	return r, nil
}

func (r *Remote) monitorPing(client *rpc.Client) error {
	ticker := time.NewTicker(pingInveral)
	defer ticker.Stop()

	//bug here, if replica was marked as ERR in normal situation, this
	//thread still won't exit until it failed multiple times of ping
	// at least the channel should be closed
	for {
		select {
		case <-r.closeChan:
			r.monitorChan <- nil
			return nil
		case <-ticker.C:
			if err := client.Ping(); err != nil {
				client.SetError(err)
				r.monitorChan <- err
				return err
			}
		}
	}
}

func (r *Remote) GetMonitorChannel() types.MonitorChannel {
	return r.monitorChan
}
