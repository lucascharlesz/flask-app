from flask import request
from flask_restplus import Resource

from ..utils.dto import UserDto
from ..services.user_service import UserService

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return UserService.get_all_users()

    @api.response(201, 'User successfully created.')
    @api.response(209, 'User failed to create. Username already taken.')

    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return UserService.save_new_user(data=data)


@api.route('/<username>')
@api.param('username', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, username):
        """get a user given its identifier"""
        user = UserService.get_a_user(username)
        if not user:
            api.abort(404, "User not found.")
        else:
            return user
