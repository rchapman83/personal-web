# -*- settings:utf-8 -*-
# Flask settings 

import logging
import os


proj_name = os.environ.get('PROJECT_NAME')
debug_mode = os.environ.get('FLASK_DEBUG')
secret_code = os.environ.get('FLASK_SECRET') 

DEBUG = debug_mode
TESTING = False
USE_X_SENDFILE = False
CSRF_ENABLED = True
SECRET_KEY = secret_code
 
# LOGGING
LOGGER_NAME = '%s_log' % proj_name
LOG_FILENAME = '/var/tmp/app.%s.log' % proj_name
LOG_LEVEL = logging.INFO
LOG_FORMAT = '%(asctime)s %(levelname)s\t: %(message)s'
