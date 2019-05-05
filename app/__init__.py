from flask import Flask
from flask_restful import Api
from config import config

from app.resources.user import UserRegister


def create_app(config_name):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(config[config_name])

    api.add_resource(UserRegister, '/register')
    return app
