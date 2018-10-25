from flask_restplus import Api
from flask import Blueprint

from .main.controllers.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='Flask Blog API',
    version='1.0',
    description='a cool web api to blog with people users (:'
)

api.add_namespace(user_ns, path='/user')
