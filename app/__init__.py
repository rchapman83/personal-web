# -*- coding: utf-8 -*-
# Entry point to bring up the web app __init__

# Flask mod imports
from flask import Flask

# Construct application
application = Flask(__name__.split('.')[0], static_folder='static', template_folder='templates')
#application.config.from_envvar('FLASK_SETTINGS')
application.config.from_pyfile('settings.py')

# Import all the views for this web app
from . import routes