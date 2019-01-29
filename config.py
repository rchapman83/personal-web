# -*- config:utf-8 -*-
# make Gunicorn work good and stuff

import multiprocessing
from os import environ


bind = '0.0.0.0:8080'
name = environ.get('PROJECT_NAME')
backlog = 2048
max_requests = 1000
proc_name = environ.get('PROJECT_NAME')
workers = int((multiprocessing.cpu_count() * 2) + 1)
threads = int(multiprocessing.cpu_count()+1)
daemon = False
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2
# keyfile = myserver-dev.key
# certfile = myserver-dev.crt
forwarded_allow_ips = '*'
# secure_scheme_headers = {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}

errorlog = '-'
loglevel = 'info'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
