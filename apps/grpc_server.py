from concurrent import futures
import grpc
from grpc import reflection
import service_pb2_grpc
import service_pb2

class MyServiceServicer(service_pb2_grpc.MyServiceServicer):
    def SayHello(self, request, context):
        return service_pb2.HelloResponse(message=f"Hello, {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), server)

    # Добавляем поддержку Reflection API
    SERVICE_NAMES = (
        service_pb2.DESCRIPTOR.services_by_name['MyService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:443')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
