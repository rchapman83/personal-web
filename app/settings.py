# -*- settings:utf-8 -*-
# Flask settings

from os import environ

proj_name = environ.get('PROJECT_NAME')
secret_code = environ.get('FLASK_SECRET')

DEBUG = True
TESTING = True
USE_X_SENDFILE = False
CSRF_ENABLED = True
SECRET_KEY = secret_code
SESSION_COOKIE_NAME = proj_name + '_session'
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Lax'
PERMANENT_SESSION_LIFETIME = 3600  # 1 hour