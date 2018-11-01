import grpc
from concurrent import futures
import time

# import the generated classes
from .protos import users_pb2
from .protos import users_pb2_grpc

# import the original calculator.py
from ..services.user_service import UserService

# create a class to define the server functions, derived from
# calculator_pb2_grpc.CalculatorServicer
class UsersServicer(users_pb2_grpc.UsersServicer):

    # calculator.square_root is exposed here
    # the request and response are of the data type
    # calculator_pb2.Number
    def get_user(self, request, context):
        import pdb; pdb.set_trace()
        response = users_pb2.GetUsersResult()
        response.user = UserService.get_a_user(request.user[0].username) if request.user else UserService.get_all_users()
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
users_pb2_grpc.add_UsersServicer_to_server(
        UsersServicer(), server)

def start():
    # listen on port 50051
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()

    # since server.start() will not block,
    # a sleep-loop is added to keep alive
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
