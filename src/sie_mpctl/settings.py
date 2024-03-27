from pathlib import Path
from sie_mpctl.secret import * # noqa

BASE_DIR: Path = Path(__file__).resolve().parent.parent
ROOT_DIR: Path = BASE_DIR.parent

ALLOWED_HOSTS: list = ['*']

INSTALLED_APPS: list = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE: list = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF: str = 'sie_mpctl.urls'

TEMPLATES: list = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION: str = 'sie_mpctl.wsgi.application'
ASGI_APPLICATION: str = 'sie_mpctl.asgi.application'

AUTH_PASSWORD_VALIDATORS: list = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE: str = 'en-us'
USE_I18N: bool = True
USE_TZ: bool = True

STATIC_URL: str = '/static/'
STATICFILES_DIRS: list = [
    ROOT_DIR / 'dist',
    ROOT_DIR / 'static',
]
STATIC_ROOT: Path = ROOT_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD: str = 'django.db.models.BigAutoField'

CHANNEL_LAYERS: dict = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [],
        },
    },
}
