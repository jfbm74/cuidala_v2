from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.34.58.135', 'localhost', '127.0.0.1']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cuidalapp_test',
        'USER': 'cuidalapp_user',
        'PASSWORD': '4dreamCoders',
        'HOST': '192.34.59.183',
        'PORT': '3306',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
MEDIA_URL = '/media_profiles/'
MEDIA_ROOT = BASE_DIR.child('media_profiles')
