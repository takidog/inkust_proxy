# DEBUGGING
reload = True

# Bind IP
bind = "0.0.0.0:8050"

# Performance
workers = 4
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 5

# Logger
accesslog = "-"
access_log_format = '%(t)s [Inkust_Proxy] [%(h)s] [%(a)s] [%(m)s] [%(U)s] [%(s)s]'
