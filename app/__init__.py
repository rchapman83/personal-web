# -*- coding: utf-8 -*-
# Entry point to bring up the web app __init__

# Flask mod imports
from flask import Flask
from flask_talisman import Talisman

# Content Security Policy (CSP) Header
csp = {
    "default-src": ["'self'", "https://*.rnchapman.pw", "https://*.rnchapman.me"],
    "script-src": ["'self'", "https://www.googletagmanager.com"],    # allow local scripts + GTM
    "style-src": ["'self'", "https://fonts.googleapis.com"],         # allow Google Fonts CSS if needed
    "font-src": ["https://fonts.gstatic.com", "https://fonts.googleapis.com"],
    "img-src": ["'self'", "https://www.gravatar.com", "data:"],      # allow gravatar + data URIs
}
# HTTP Strict Transport Security (HSTS) Header
hsts = {
    'max-age': 31536000,
    'includeSubDomains': True
}

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