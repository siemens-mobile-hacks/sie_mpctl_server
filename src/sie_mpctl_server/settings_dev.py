from sie_mpctl_server.settings import * # noqa

DEBUG: bool = True

DATABASES: dict = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sie_mpctl',
        'USER': 'sie_mpctl',
    }
}
