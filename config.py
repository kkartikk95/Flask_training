import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret_string"
    # Secret key for security reasons like cookies etc.

    MONGODB_SETTINGS = {'db' : 'Flask_MongoDB_training'}