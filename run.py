# -*- coding: utf-8 -*-
# Entry point to bring up the web app

from os import environ
import subprocess

# Boolean 0=Website mode enabled all is good 1=Disabled web app
x = environ.get('APP_MODE')
# Grab the config file from enviro var
c = environ.get('APP_CONFIG')
# Get which app to run
a = environ.get('APP_MODULE')

if x=="0":
    print('Starting web application')
elif x=="1":
    print('Web app is disabled and will exit')
else:
    print('Invalid mode value default start up')

# Attempt to run Gunicorn to serve the app
try:
    subprocess.call(['gunicorn', '-c', c, a])
except RuntimeError:
    print('Unable to start application server')

# Run the Flask app server
# from flask import Flask
# from app import application
# application.run(host='0.0.0.0', port=8080)
