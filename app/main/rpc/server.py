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
        response = users_pb2.Number()
        response.value = UserService.get_user(request.value)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
calculator_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorServicer(), server)

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
