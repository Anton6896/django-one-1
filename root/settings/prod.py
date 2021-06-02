"""
prod settings
"""

ALLOWED_HOSTS = ['django-one.herokuapp.com', ]
DEBUG = False
import os

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'POST': '',
    }
}
