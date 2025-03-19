import grpc
import service_pb2_grpc as pb2_grpc
import service_pb2 as pb2

# Настройте gRPC-клиент
channel = grpc.insecure_channel("vuln.host.com:8002")
stub = pb2_grpc.MyServiceStub(channel)

# Отправьте запрос на сервер
response = stub.SayHello(pb2.HelloRequest(name="World"))
print(response.message)
