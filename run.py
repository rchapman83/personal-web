# -*- coding: utf-8 -*-
# Entry point to bring up the web app

from os import environ
import logging, timber

# Boolean 0=Website mode enabled all is good 1=Disabled web app 2=default flask server for debug
x = environ.get('APP_MODE')
# Grab the config file from enviro var
c = environ.get('APP_CONFIG')
# Get which app to run
a = environ.get('APP_MODULE')
# Timber api token
t = environ.get('TIMBER_TOKEN')

# Never allow more than 50 outstanding log events in buffer and send any outstanding log events at most every 60 seconds
logger = logging.getLogger(__name__)
timber_handler = timber.TimberHandler(api_key=t, level=logging.DEBUG, buffer_capacity=20, flush_interval=60, raise_exceptions=True)
logger.addHandler(timber_handler)

if x=='0':
    print('Starting web application')
    logger.info('Starting web application as normal')
    import subprocess
    # Attempt to run Gunicorn to serve the app
    try:
        subprocess.call(['gunicorn', '-c', c, a])
        logger.info('gunicorn start-up complete')
    except RuntimeError as e:
        print('Failed to start-up application server, exiting')
        logger.error('Failed to start-up gunicorn, exiting. Consider putting application into debug mode' + e)
        quit()
elif x=='1':
    import requests
    print('Web application is disabled and will take alternitive action')
    try:
        logger.info('Web application is manually disabled, redirecing request to rnchapman.directory')
        r = requests.get('https://www.rnchapman.directory', timeout=0.005)
        r.url
    except ConnectionError as e:
        print('Connection error or no response')
        r = "No response"
        logger.error('Web application is manually disabled and a connection error occured' + e)
        quit()
elif x=='2':
    print('Starting web application in debug mode')
    logger.debug('Starting flask app server in debug mode')
    # Run the Flask app server
    from flask import Flask
    from app import application
    application.run(host='0.0.0.0', port=8080, debug=True)
else:
    print('Invalid start-up configuration')
    logger.critical('Invalid start-up configuration, quitting')
    quit()
