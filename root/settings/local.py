import boto3
from botocore.config import Config

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

s3 = boto3.client('s3', config=Config(signature_version='s3v4'))
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('S3_BUCKET')
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
