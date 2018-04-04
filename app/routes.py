# -*- coding: utf-8 -*-
# All the views here

# Import app via circular imports
from . import application
# Import password and keygen junk
from . import gen
# Import flask stuff
from flask import Flask, render_template, request, send_from_directory


@application.route('/')
def entry():
    newPasswd = gen.mkPasswordWeb(16)
    newLead = gen.mkLead()
    return render_template('index.html', passwd=newPasswd, leadText=newLead)


@application.route('/robots.txt')
def robots_static():
    return send_from_directory(application.static_folder, request.path[1:])


@application.route('/sitemap.xml')
def sitemap_static():
    return send_from_directory(application.static_folder, request.path[1:])


@application.route('/environ')
def env():
    newToken = gen.mkKey(64)
    return 'Root path : ' + application.root_path + ' <br>Template path: ' + application.template_folder + '<br> Key : ' + newToken


@application.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@application.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500
