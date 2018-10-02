# -*- coding: utf-8 -*-
# All the views here

# Import app via circular imports
from . import application
# Import flask stuff
from flask import Flask, render_template, send_from_directory, request
# Import os environment mods
from os import environ
# Import PyGitHub library to access the GitHub API v3
from github import Github
# Import code for encoding urls and generating md5 hashes
import urllib, hashlib

# Define custom functions
# Funtion to generate the URL my gravatar profile picture on the home page
def gravatar():
    # Set your desired email from environ var, must be lower case
    gravEmail = environ.get('GRAV_USER')
    # construct the url
    gravURL = 'https://www.gravatar.com/avatar/' + hashlib.md5(gravEmail.encode('utf-8')).hexdigest() + '?s=150'
    return gravURL

# Github function for changelog intergration on the colophon page
def githubChg():
    # Set personal access token generated from GitHub via an enviro var
    gToken = environ.get('GIT_TOKEN')
    gRepo = environ.get('GIT_REPO')
    gAccess = Github(gToken)
    repo = gAccess.get_repo(gRepo)
    repoInfo = 'The pull req nums are: '
    pulls = repo.get_pulls(state='open', sort='created', base='dev')
    for pr in pulls:
        i = pr.number
        repoInfo = repoInfo + i
    #for repo in gAccess.get_user().get_repos():
     #   i = repo.name
      #  repoInfo = repoInfo + i
    return repoInfo

@application.route('/')
def entry():
    x = gravatar()
    return render_template('index.html', profilePic=x)

@application.route('/colophon')
def colophon():
    return render_template('colophon.html')

@application.route('/test')
def test():
    y = githubChg()
    return render_template('test.html', chgLog=y)

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
