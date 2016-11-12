import os

MONGODB_DB = 'music'
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
PROXIES = []

REDIS_DB = 0
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

DEBUG = False

USERNAME = '用户名'
PASSWORD = '密码'

try:
    from local_settings import *  # noqa
except ImportError:
    pass
