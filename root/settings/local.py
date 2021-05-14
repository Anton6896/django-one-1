from root.settings import BASE_DIR

ALLOWED_HOSTS = ['127.0.0.1', ]
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
