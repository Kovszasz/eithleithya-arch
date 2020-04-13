from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*','.herokuapp.com']
db_from_env = config('DATABASE_URL')
DATABASES:{
    'default':{}
}
DATABASES['default'].update(db_from_env)
