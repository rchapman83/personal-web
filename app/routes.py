# -*- coding: utf-8 -*-
# All the views here

# Import app via circular imports
from . import application
# Import flask stuff
from flask import Flask, render_template, send_from_directory
# import code for encoding urls and generating md5 hashes
import urllib, hashlib

@application.route('/')
def entry():
    # Set your variables here
    gravEmail = 'rowan.chapman@hobsons.com'
    # construct the url
    gravURL = 'https://www.gravatar.com/avatar/' + hashlib.md5(gravEmail.lower()).hexdigest() + '?s=150'
    return render_template('index.html', profilePic=gravURL)

@application.route('/robots.txt')
def robots_static():
    return send_from_directory(application.static_folder, request.path[1:])

@application.route('/sitemap.xml')
def sitemap_static():
    return send_from_directory(application.static_folder, request.path[1:])

@application.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@application.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500
