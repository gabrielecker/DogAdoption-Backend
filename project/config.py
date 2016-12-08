# encodingg: utf-8


class BaseConfig(object):
    SECRET_KEY = '71bcdb52a2cb4b09a5ddf6af4bf84e64'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:@localhost/dog_adoption'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
