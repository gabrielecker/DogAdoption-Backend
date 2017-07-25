# encoding: utf-8
from decouple import config
import datetime


class BaseConfig(object):
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL', default='')
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
