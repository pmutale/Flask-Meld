from string import Template

requirements_template = Template(
    """
Flask>=0.9
Flask-Meld>=0.4.10
"""
)

config_template = Template(
    """
import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
"""
)

init_template = Template(
    """
from flask import Flask, render_template
from config import config
from flask_meld import Meld
# from .db import db
# from app import models

# extensions
meld = Meld()


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # db.init_app(app)

    meld.init_app(app)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app
    """
)
