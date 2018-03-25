# -*- coding: utf-8 -*-
import os.path


DEBUG = True
TESTING = False
# generated with os.urandom(24)
SECRET_KEY = 'M\xe9b\x99\xf5w\x15\xdd\x15\xa3&aqa\x81\xd7\xec\x8a\xbb\r\xf5\xf8\x98\xd8'

MAX_CONTENT_LENGTH = 128 * 1024 * 1024

# Flask-Cache configuration
# CACHE_TYPE:
# - null: NullCache (default)
# - simple: SimpleCache
# - memcached: MemcachedCache (pylibmc or memcache required)
# - gaememcached: GAEMemcachedCache
# - redis: RedisCache (Werkzeug 0.7 required)
# - filesystem: FileSystemCache
# - saslmemcached: SASLMemcachedCache (pylibmc required)
CACHE_TYPE = 'redis'

# Application
DATA_PATH = os.path.realpath('data')
TEMPLATE_PATH = None
GNUPG_TIMESTAMP_URL = 'http://timestamp.synology.com/timestamp.php'
GNUPG_PATH = None
GNUPG_FINGERPRINT = 'gnupg-fingerprint'

# Security
SECURITY_CONFIRMABLE = True
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
SECURITY_PASSWORD_HASH = 'sha512_crypt'
SECURITY_PASSWORD_SALT = 'h\x8d\x92p9\x81\xcb\xcf\xca\x81\xcf\x86\xc4\xbe\xd8\x94b)\x01\x05.\xf8\xc6T'

# SQLAlchemy
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/spkrepo.db' % DATA_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Restful
HTTP_BASIC_AUTH_REALM = 'spkrepo'

# Migrate
MIGRATE_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'migrations'))

# Debug Toolbar
DEBUG_TB_INTERCEPT_REDIRECTS = False
