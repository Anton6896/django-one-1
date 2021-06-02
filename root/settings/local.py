from root.settings import BASE_DIR
import os

ALLOWED_HOSTS = ['127.0.0.1', ]
DEBUG = True

SECRET_KEY = 'django-insecure-ww(aek15i5y_kzs^-h_!*qn#g@k3q=qcf@!xrt1!2n56bdapu!'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
