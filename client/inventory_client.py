import grpc

import sys
sys.path.insert(1, 'services')

import inventory_pb2 as test_pb2
import inventory_pb2_grpc as test_pb2_grpc

class TestInventory:
    # get books using isbn
    def run_with_isbn(self,isbn):
        with grpc.insecure_channel('0.0.0.0:50051') as channel:
            stub = test_pb2_grpc.BookServiceStub(channel)
            response = stub.getBook(test_pb2.BookIsbn(input=isbn))
            return response