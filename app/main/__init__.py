from flask import Flask, make_response, jsonify
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    from app.main.schema import schema
    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app
