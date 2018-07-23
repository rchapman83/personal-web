# -*- coding: utf-8 -*-
# All the views here

# Import app via circular imports
from . import application
# Import flask stuff
from flask import Flask, render_template, send_from_directory, request
# Import os environment mods
from os import environ
# import code for encoding urls and generating md5 hashes
import urllib, hashlib

# define functions
def gravatar():
    # Set your desired email from environ var, must be lower case
    gravEmail = environ.get('GRAV_USER')
    # construct the url
    gravURL = 'https://www.gravatar.com/avatar/' + hashlib.md5(gravEmail.encode('utf-8')).hexdigest() + '?s=150'
    return gravURL

@application.route('/')
def entry():
    gravThumb = gravatar()
    return render_template('index.html', profilePic=gravThumb)

@application.route('/colophon')
def colophon():
    return render_template('colophon.html')

@application.route('/robots.txt')
def robots_static():
    return send_from_directory(application.static_folder, request.path[1:])

@application.route('/humans.txt')
def human_static():
    return send_from_directory(application.static_folder, request.path[1:])

@application.route('/keybase.txt')
def keybase_static():
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
