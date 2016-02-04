import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgres://verna:P4verna@localhost/vernadb'
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# @LetsTellBot
#API_TOKEN = '168884644:AAFqWudrVScVIOd2jfo_uKsxmROgOkwXqx4'
# @VernaPolemicBot
API_TOKEN = '196208822:AAESVQ98Ts9XK5pINUvAXhlXOV2ypCFJDEs'

WEBHOOK_HOST = 'verna.mobi'
WEBHOOK_PORT = 443  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_LISTEN = '0.0.0.0'  # In some VPS you may need to put here the IP addr: 128.199.43.243
basedir = os.path.abspath(os.path.dirname(__file__))
WEBHOOK_SSL_CERT = os.path.join(basedir, 'ssl/verna.mobi.crt')  # Path to the ssl certificate
WEBHOOK_SSL_PRIV = os.path.join(basedir, 'ssl/verna.mobi.key')  # Path to the ssl private key

# Quick'n'dirty SSL certificate generation:
#
# openssl genrsa -out webhook_pkey.pem 2048
# openssl req -new -x509 -days 3650 -key webhook_pkey.pem -out webhook_cert.pem
#
# When asked for "Common Name (e.g. server FQDN or YOUR name)" you should reply
# with the same value in you put in WEBHOOK_HOST

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (API_TOKEN)

YOUTUBE_URL_REGEXP = "(?:([0-9])+)\.mp4"
