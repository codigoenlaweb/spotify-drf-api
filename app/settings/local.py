from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = tuple(env.list('ALLOWED_HOSTS', default=['*']))

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env.str('ENGINE_DB'),
        'NAME': env.str('NAME_DB'),
        'USER': env.str('USER_DB'),
        'PASSWORD': env.str('PASSWORD_DB'),
        'HOST': env.str('HOST_DB'),
        'PORT': env.int('PORT_DB')
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"