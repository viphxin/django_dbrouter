#coding=utf-8
import multiprocessing

#bind = "127.0.0.1:8000"
bind = "unix:/home/sy/workspace/foodgame_server/passport/passport/gunicorn.sock"
workers = multiprocessing.cpu_count() / 2
backlog = 2048
#sync
#eventlet - Requires eventlet >= 0.9.7
#gevent - Requires gevent >= 0.13
#tornado - Requires tornado >= 0.2
#gthread - Python 2 requires the futures package to be installed
#gaiohttp - Requires Python 3.4 and aiohttp >= 0.21.5
worker_class = "gevent"
threads = 1
#The maximum number of simultaneous clients.
#This setting only affects the Eventlet and Gevent worker types.
worker_connections = 1000
#这是一个保护机制, 超过限制自动重启
max_requests = 1000
#这个参数是max_requests的补充, 防止所有的woker同时重启
#random(0, max_requests_jitter)重启
max_requests_jitter = workers
timeout = 10
keepalive = 2
#热更
reload = False
chdir = "/home/sy/workspace/foodgame_server/passport"
user = "www-data"
group = "www-data"
umask = "0155"
"""
The granularity of Error log outputs.

Valid level names are:

debug
info
warning
error
critical
"""
loglevel = "debug"
# raw_env = "passport:wsgi"