# -*- coding: utf-8 -*-
# Entry point to bring up the web app __init__

from os import environ
# Flask mod imports
from flask import Flask
from flask_talisman import Talisman # type: ignore
# Google Cloud Profiler import
import googlecloudprofiler # type: ignore

proj_name = environ.get('PROJECT_NAME')
srvc_name = environ.get('APP_NAME')
srvc_version = environ.get('APP_VERSION')

# Content Security Policy (CSP) Header
csp = {
    "default-src": ["'self'", "https://*.rnchapman.pw", "https://*.rnchapman.me"],
    "script-src": ["'self'", "https://www.googletagmanager.com", "https://www.google-analytics.com"],    # allow local scripts + GTM
    "style-src": ["'self'", "https://fonts.googleapis.com"],         # allow Google Fonts CSS if needed
    "font-src": ["https://fonts.gstatic.com", "https://fonts.googleapis.com"],
    "img-src": ["'self'", "https://www.gravatar.com", "data:"],      # allow gravatar + data URIs
}
# HTTP Strict Transport Security (HSTS) Header
hsts = {
    'max-age': 31536000,
    'includeSubDomains': True
}

try:
    googlecloudprofiler.start(
    service=srvc_name,
    service_version=srvc_version,
    # verbose is the logging level. 0-error, 1-warning, 2-info, 3-debug. It defaults to 0 (error) if not set.
    verbose=0,
    # project_id must be set if not running on GCP.
    project_id=proj_name,
    )
except (ValueError, NotImplementedError) as e:
    print(e)  # Handle errors here

# Construct application
# Should the env var not be set you can use application.config.from_pyfile('SETTING FILE')
application = Flask(__name__.split('.')[0], static_folder='static', template_folder='templates')
application.config.from_envvar('FLASK_SETTINGS')
talisman = Talisman(application)

# Enforce HTTPS and other headers
talisman.force_https = True
talisman.force_file_save = True
talisman.x_xss_protection = True
talisman.session_cookie_secure = True
talisman.session_cookie_samesite = 'Lax'
talisman.frame_options_allow_from = 'https://www.google.com/'

# Add the headers to Talisman
talisman.content_security_policy = csp
talisman.strict_transport_security = hsts

# Import all the views for this web app
from . import routes