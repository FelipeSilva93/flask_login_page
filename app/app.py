from flask import Flask
from app.ext import conf


def create_app():
    """Factory that will create our app"""
    app = Flask(__name__)
    conf.init_app(app)

    return app
