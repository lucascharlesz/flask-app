import grpc

# import the generated classes
from .protos import users_pb2
from .protos import users_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = users_pb2_grpc.UsersStub(channel)

def get_users(a_username=None):
    # create a valid request message
    user = users_pb2.User(username=a_username, id=None)
    params = users_pb2.GetUsersRequest(user=[user])
    import pdb; pdb.set_trace()

    # make the call
    response = stub.get_user(params)

    # et voilà
    print(response.value)