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
