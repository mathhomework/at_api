import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'adventure_time',
        'USER': 'postgres',
        'PASSWORD': 'hotdog'
    }
}

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
