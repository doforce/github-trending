from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)

    from .api import api
    app.register_blueprint(api)

    return app

