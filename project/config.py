# encodingg: utf-8
import datetime
import os


class BaseConfig(object):
    SECRET_KEY = '71bcdb52a2cb4b09a5ddf6af4bf84e64'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = False
    REMEMBER_COOKIE_DURATION = datetime.timedelta(hours=24)


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
