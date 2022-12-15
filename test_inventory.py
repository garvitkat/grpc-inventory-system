import grpc
import services.inventory_pb2 as test_pb2
import services.inventory_pb2_grpc as test_pb2_grpc

def run():
    with grpc.insecure_channel('0.0.0.0:50051') as channel:
        stub = test_pb2_grpc.BookServiceStub(channel)
        response = stub.getBook(test_pb2.BookIsbn(input="001"))
        print(response.title)


if __name__ == '__main__':
    run()