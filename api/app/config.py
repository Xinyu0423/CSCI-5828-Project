import os, datetime
# from redis import Redis


class Config(object):
    DEBUG = False
    TESTING = False
    # Session
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'xxxx'
    # SESSION_TYPE = 'redis'
    # SESSION_KEY_PREFIX = 'csci5828'
    # SESSION_REDIS = Redis(host='localhost', port=6379)
    # SESSION_PERMANENT = True
    # PERMANENT_SESSION_TIME = datetime.timedelta(hours = 12)
    # SESSION_REFRESH_EACH_REQUEST = True

    # Database
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite.db"
    # SESSION_REDIS = Redis(host='localhost', port=6379)

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite.db"
    # SESSION_REDIS = Redis(host='localhost', port=6379)