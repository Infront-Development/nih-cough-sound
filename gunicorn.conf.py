#!/usr/bin/env python3

import multiprocessing

# Server socket
bind = "0.0.0.0:8000"
backlog = 2048

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2

# Restart workers after this many requests, to help prevent memory leaks
max_requests = 1000
max_requests_jitter = 100

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Process naming
proc_name = "mohcough_gunicorn"

# Server mechanics
daemon = False
pidfile = "/tmp/gunicorn.pid"
user = None
group = None
tmp_upload_dir = None

# SSL (if needed in future)
keyfile = None
certfile = None

# Environment variables
raw_env = [
    "DJANGO_SETTINGS_MODULE=mohcough.settings",
]

# Preload app for better performance
preload_app = True

# Worker tmp directory
worker_tmp_dir = "/dev/shm"

# Maximum size of HTTP request line in bytes
limit_request_line = 4094

# Maximum number of HTTP request header fields
limit_request_fields = 100

# Maximum size of HTTP request header field
limit_request_field_size = 8190
