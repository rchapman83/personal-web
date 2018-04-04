# -*- coding: utf-8 -*-
# All the views here

# Import app via circular imports
from . import application
# Import flask stuff
from flask import Flask, render_template, send_from_directory


@application.route('/')
def entry():
    return render_template('test.html')

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
