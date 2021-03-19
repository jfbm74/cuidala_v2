from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cuidalapp_test',
        'USER': 'cuidalapp_user',
        'PASSWORD': '4dreamCoders',
        'HOST': '143.198.229.44',
        'PORT': '3306',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
STATIC_ROOT = BASE_DIR.child('staticfiles')

MEDIA_URL = '/media_profiles/'
MEDIA_ROOT = BASE_DIR.child('media_profiles')
