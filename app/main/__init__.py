from flask import Flask, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()

def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.register_error_handler(404, not_found)

    db.init_app(app)
    flask_bcrypt.init_app(app)

    # from . import auth
    # app.register_blueprint(auth.bp)

    return app
