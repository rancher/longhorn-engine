# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import rpc_pb2 as rpc__pb2


class EngineManagerServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.EngineCreate = channel.unary_unary(
        '/EngineManagerService/EngineCreate',
        request_serializer=rpc__pb2.EngineCreateRequest.SerializeToString,
        response_deserializer=rpc__pb2.EngineResponse.FromString,
        )
    self.EngineDelete = channel.unary_unary(
        '/EngineManagerService/EngineDelete',
        request_serializer=rpc__pb2.EngineRequest.SerializeToString,
        response_deserializer=rpc__pb2.EngineResponse.FromString,
        )
    self.EngineGet = channel.unary_unary(
        '/EngineManagerService/EngineGet',
        request_serializer=rpc__pb2.EngineRequest.SerializeToString,
        response_deserializer=rpc__pb2.EngineResponse.FromString,
        )
    self.EngineList = channel.unary_unary(
        '/EngineManagerService/EngineList',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=rpc__pb2.EngineListResponse.FromString,
        )
    self.EngineUpgrade = channel.unary_unary(
        '/EngineManagerService/EngineUpgrade',
        request_serializer=rpc__pb2.EngineUpgradeRequest.SerializeToString,
        response_deserializer=rpc__pb2.EngineResponse.FromString,
        )
    self.EngineLog = channel.unary_stream(
        '/EngineManagerService/EngineLog',
        request_serializer=rpc__pb2.LogRequest.SerializeToString,
        response_deserializer=rpc__pb2.LogResponse.FromString,
        )
    self.EngineWatch = channel.unary_stream(
        '/EngineManagerService/EngineWatch',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=rpc__pb2.EngineResponse.FromString,
        )
    self.EngineExpand = channel.unary_unary(
        '/EngineManagerService/EngineExpand',
        request_serializer=rpc__pb2.EngineExpandRequest.SerializeToString,
        response_deserializer=rpc__pb2.EngineResponse.FromString,
        )
    self.FrontendStart = channel.unary_unary(
        '/EngineManagerService/FrontendStart',
        request_serializer=rpc__pb2.FrontendStartRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.FrontendShutdown = channel.unary_unary(
        '/EngineManagerService/FrontendShutdown',
        request_serializer=rpc__pb2.EngineRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.FrontendStartCallback = channel.unary_unary(
        '/EngineManagerService/FrontendStartCallback',
        request_serializer=rpc__pb2.EngineRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.FrontendShutdownCallback = channel.unary_unary(
        '/EngineManagerService/FrontendShutdownCallback',
        request_serializer=rpc__pb2.EngineRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class EngineManagerServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def EngineCreate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EngineDelete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EngineGet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EngineList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EngineUpgrade(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EngineLog(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EngineWatch(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EngineExpand(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FrontendStart(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FrontendShutdown(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FrontendStartCallback(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FrontendShutdownCallback(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EngineManagerServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'EngineCreate': grpc.unary_unary_rpc_method_handler(
          servicer.EngineCreate,
          request_deserializer=rpc__pb2.EngineCreateRequest.FromString,
          response_serializer=rpc__pb2.EngineResponse.SerializeToString,
      ),
      'EngineDelete': grpc.unary_unary_rpc_method_handler(
          servicer.EngineDelete,
          request_deserializer=rpc__pb2.EngineRequest.FromString,
          response_serializer=rpc__pb2.EngineResponse.SerializeToString,
      ),
      'EngineGet': grpc.unary_unary_rpc_method_handler(
          servicer.EngineGet,
          request_deserializer=rpc__pb2.EngineRequest.FromString,
          response_serializer=rpc__pb2.EngineResponse.SerializeToString,
      ),
      'EngineList': grpc.unary_unary_rpc_method_handler(
          servicer.EngineList,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=rpc__pb2.EngineListResponse.SerializeToString,
      ),
      'EngineUpgrade': grpc.unary_unary_rpc_method_handler(
          servicer.EngineUpgrade,
          request_deserializer=rpc__pb2.EngineUpgradeRequest.FromString,
          response_serializer=rpc__pb2.EngineResponse.SerializeToString,
      ),
      'EngineLog': grpc.unary_stream_rpc_method_handler(
          servicer.EngineLog,
          request_deserializer=rpc__pb2.LogRequest.FromString,
          response_serializer=rpc__pb2.LogResponse.SerializeToString,
      ),
      'EngineWatch': grpc.unary_stream_rpc_method_handler(
          servicer.EngineWatch,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=rpc__pb2.EngineResponse.SerializeToString,
      ),
      'EngineExpand': grpc.unary_unary_rpc_method_handler(
          servicer.EngineExpand,
          request_deserializer=rpc__pb2.EngineExpandRequest.FromString,
          response_serializer=rpc__pb2.EngineResponse.SerializeToString,
      ),
      'FrontendStart': grpc.unary_unary_rpc_method_handler(
          servicer.FrontendStart,
          request_deserializer=rpc__pb2.FrontendStartRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'FrontendShutdown': grpc.unary_unary_rpc_method_handler(
          servicer.FrontendShutdown,
          request_deserializer=rpc__pb2.EngineRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'FrontendStartCallback': grpc.unary_unary_rpc_method_handler(
          servicer.FrontendStartCallback,
          request_deserializer=rpc__pb2.EngineRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'FrontendShutdownCallback': grpc.unary_unary_rpc_method_handler(
          servicer.FrontendShutdownCallback,
          request_deserializer=rpc__pb2.EngineRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'EngineManagerService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class ProcessManagerServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ProcessCreate = channel.unary_unary(
        '/ProcessManagerService/ProcessCreate',
        request_serializer=rpc__pb2.ProcessCreateRequest.SerializeToString,
        response_deserializer=rpc__pb2.ProcessResponse.FromString,
        )
    self.ProcessDelete = channel.unary_unary(
        '/ProcessManagerService/ProcessDelete',
        request_serializer=rpc__pb2.ProcessDeleteRequest.SerializeToString,
        response_deserializer=rpc__pb2.ProcessResponse.FromString,
        )
    self.ProcessGet = channel.unary_unary(
        '/ProcessManagerService/ProcessGet',
        request_serializer=rpc__pb2.ProcessGetRequest.SerializeToString,
        response_deserializer=rpc__pb2.ProcessResponse.FromString,
        )
    self.ProcessList = channel.unary_unary(
        '/ProcessManagerService/ProcessList',
        request_serializer=rpc__pb2.ProcessListRequest.SerializeToString,
        response_deserializer=rpc__pb2.ProcessListResponse.FromString,
        )
    self.ProcessLog = channel.unary_stream(
        '/ProcessManagerService/ProcessLog',
        request_serializer=rpc__pb2.LogRequest.SerializeToString,
        response_deserializer=rpc__pb2.LogResponse.FromString,
        )
    self.ProcessWatch = channel.unary_stream(
        '/ProcessManagerService/ProcessWatch',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=rpc__pb2.ProcessResponse.FromString,
        )


class ProcessManagerServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ProcessCreate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ProcessDelete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ProcessGet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ProcessList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ProcessLog(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ProcessWatch(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ProcessManagerServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ProcessCreate': grpc.unary_unary_rpc_method_handler(
          servicer.ProcessCreate,
          request_deserializer=rpc__pb2.ProcessCreateRequest.FromString,
          response_serializer=rpc__pb2.ProcessResponse.SerializeToString,
      ),
      'ProcessDelete': grpc.unary_unary_rpc_method_handler(
          servicer.ProcessDelete,
          request_deserializer=rpc__pb2.ProcessDeleteRequest.FromString,
          response_serializer=rpc__pb2.ProcessResponse.SerializeToString,
      ),
      'ProcessGet': grpc.unary_unary_rpc_method_handler(
          servicer.ProcessGet,
          request_deserializer=rpc__pb2.ProcessGetRequest.FromString,
          response_serializer=rpc__pb2.ProcessResponse.SerializeToString,
      ),
      'ProcessList': grpc.unary_unary_rpc_method_handler(
          servicer.ProcessList,
          request_deserializer=rpc__pb2.ProcessListRequest.FromString,
          response_serializer=rpc__pb2.ProcessListResponse.SerializeToString,
      ),
      'ProcessLog': grpc.unary_stream_rpc_method_handler(
          servicer.ProcessLog,
          request_deserializer=rpc__pb2.LogRequest.FromString,
          response_serializer=rpc__pb2.LogResponse.SerializeToString,
      ),
      'ProcessWatch': grpc.unary_stream_rpc_method_handler(
          servicer.ProcessWatch,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=rpc__pb2.ProcessResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ProcessManagerService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
