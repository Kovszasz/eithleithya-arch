from .base import *
from decouple import config
import dj_database_url
DEBUG = True

ALLOWED_HOSTS = ['*','.herokuapp.com']
DATABASE_URL = config('DATABASE_URL')
DATABASES:{
    'default':{}
}
DATABASES['default']=dj_database_url.config(conn_max_age=600)
