from .settings import *

DEBUG = True
INTERNAL_IPS = ['127.0.0.1']
ALLOWED_HOSTS += INTERNAL_IPS
ALLOWED_HOSTS.append('localhost')
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'UltraSoundOrders',
    'USER': 'kovszasz',
    'PASSWORD': 'iJO1366ug',
    'HOST': 'localhost',
    'PORT': '',
}
