from root.settings import BASE_DIR
import os

ALLOWED_HOSTS = ['127.0.0.1', ]
DEBUG = True

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
