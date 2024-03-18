from sie_mpctl.settings import * # noqa

DEBUG: bool = True
TIME_ZONE: str = 'Europe/Samara'

DATABASES: dict = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sie_mpctl',
        'USER': 'sie_mpctl',
    }
}
