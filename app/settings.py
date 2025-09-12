# -*- settings:utf-8 -*-
# Flask settings

from os import environ
"""
proj_name = 'Personal Web'
debug_mode = 'true'
secret_code = 'verysecretkey'

"""
proj_name = environ.get('PROJECT_NAME')
debug_mode = environ.get('FLASK_DEBUG')
secret_code = environ.get('FLASK_SECRET')

DEBUG = debug_mode
TESTING = debug_mode
USE_X_SENDFILE = False
CSRF_ENABLED = True
SECRET_KEY = secret_code