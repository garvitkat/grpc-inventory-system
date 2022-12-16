from concurrent import futures
import logging

import grpc
import inventory_pb2_grpc 
import inventory_pb2

Dict = {}

class AddOneServiceServicer(inventory_pb2_grpc.AddOneServiceServicer):
    def addOne(self, request, context):
        ans = request.input + 1
        return inventory_pb2.Result(result=ans)


class BookServiceServicer(inventory_pb2_grpc.BookServiceServicer):
    def getBook(self, request, context):
        isbn = request.input
        book_obj = Dict[isbn]
        return inventory_pb2.Book(id=book_obj.id,title=book_obj.title,author=book_obj.author,pub_year=book_obj.pub_year,genre=book_obj.genre)

    def addBook(self, request, context):
        book_obj = inventory_pb2.Book()
        book_obj.id = request.id
        book_obj.title = request.title
        book_obj.author = request.author
        book_obj.genre = inventory_pb2.Book.FICTION
        book_obj.pub_year = request.pub_year

        if book_obj.id in Dict:
            return inventory_pb2.ResultAddBook(result="Book id already exists")

        Dict[book_obj.id] = book_obj
        return inventory_pb2.ResultAddBook(result="Book successfully added")


def initdata():
    book_obj = inventory_pb2.Book()
    book_obj.id = "001"
    book_obj.title = "Book 1"
    book_obj.author = "Ping"
    book_obj.genre = inventory_pb2.Book.FICTION
    book_obj.pub_year = 1991

    book_obj2 = inventory_pb2.Book()
    book_obj2.id = "002"
    book_obj2.title = "Book 2"
    book_obj2.author = "Pong"
    book_obj2.genre = inventory_pb2.Book.NONFICTION
    book_obj2.pub_year = 2011
    

    book_obj3 = inventory_pb2.Book()
    book_obj3.id = "003"
    book_obj3.title = "Book 3"
    book_obj3.author = "Frank Lin"
    book_obj3.genre = inventory_pb2.Book.HORROR
    book_obj3.pub_year = 2021
    
    
    Dict[book_obj.id] = book_obj
    Dict[book_obj2.id] = book_obj2
    Dict[book_obj3.id] = book_obj3
    


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_pb2_grpc.add_BookServiceServicer_to_server(BookServiceServicer(),server)
    server.add_insecure_port('[::]:50051')
    print("start server")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    initdata()
    serve()