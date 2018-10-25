import uuid
import datetime

from app.main import db
from app.main.models.user import User

class UserService(object):
    @staticmethod
    def save_new_user(data):
        user = User.query.filter_by(username=data['username']).first()
        if not user:
            new_user = User(
                username=data['username'],
                password=data['password'],
                registered_on=datetime.datetime.utcnow()
            )

            UserService.save_changes(new_user)

            response_object = {
                'status': 'success',
                'message': 'Successfully registered.'
            }

            return response_object, 201

        else:
            response_object = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }

            return response_object, 409

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_a_user(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def save_changes(data):
        db.session.add(data)
        db.session.commit()
