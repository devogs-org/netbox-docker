# Behind Traefik: trust the X-Forwarded-Proto header it sends so NetBox builds https:// URLs
# (redirects, API pagination links). Loaded automatically with the other files of this directory.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
