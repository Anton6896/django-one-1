"""
prod settings
"""

ALLOWED_HOSTS = ['django-one.herokuapp.com', ]
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dcag045nqie3kj',
        'USER': 'kyetdefmiyibus',
        'PASSWORD': 'ef66328984fa42653a3867ffc74da689f22f4625a5896e6fb392a90709a79fb6',
        'HOST': 'ec2-63-34-97-163.eu-west-1.compute.amazonaws.com',
        'POST': '',
    }
}
