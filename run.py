# -*- coding: utf-8 -*-
# Entry point to bring up the web app

from os import environ
import subprocess

# Boolean 0=Website mode 1=API mode
x = environ.get('APP_MODE')

if x=="0":
    environ["APP_MODULE"] = "app:application"
    print('Running web application')

elif x=="1":
    environ["APP_MODULE"] = "api:application"
    print('Running api')
else:
    print('Invalid value using defaults')

# Grab the config file from enviro var
c = environ.get('APP_CONFIG')
# Get which app to run
a = environ.get('APP_MODULE')


# Run Gunicorn to serve the app
print('Time to start it up')
subprocess.call(['gunicorn', '-c', c, a])

# Run the Flask app server
# from flask import Flask
# from app import application
# application.run(host='0.0.0.0', port=8080)
