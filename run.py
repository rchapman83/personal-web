# -*- coding: utf-8 -*-
# Entry point to bring up the web app

from os import environ
import subprocess

# Boolean 0=Website mode enabled all is good 1=Disabled web app
x = environ.get('APP_MODE')

if x=="0":
    print('Running web application')
elif x=="1":
    print('Web app disabled')
else:
    print('Invalid value starting web application')

# Grab the config file from enviro var
c = environ.get('APP_CONFIG')
# Get which app to run
a = environ.get('APP_MODULE')


# Run Gunicorn to serve the app
subprocess.call(['gunicorn', '-c', c, a])

# Run the Flask app server
# from flask import Flask
# from app import application
# application.run(host='0.0.0.0', port=8080)
