"""
Django settings for to_pm project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Template paths
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Use jinja template loader
TEMPLATE_LOADERS = (
    'django_jinja.loaders.FileSystemLoader',
    'django_jinja.loaders.AppLoader',
)

# template extension
DEFAULT_JINJA2_TEMPLATE_EXTENSION = '.jinja'
#DEFAULT_JINJA2_TEMPLATE_INTERCEPT_RE = r"^(?!admin/).*"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!_u7(@s0zqg4d_d0il_2f*j-t87$z9%^woxg@i7!n!!kx0rjd@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

#ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'forum',
    'django_jinja',
    'captcha',
    'ckeditor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'to_pm.urls'

WSGI_APPLICATION = 'to_pm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# for production
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# path to store media files
MEDIA_URL = '/media/'


# Configuration for CKEditor
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"

# By default if you haven't set a name to CKEditor its name is 'default'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full', # Basic or Full
        'height': 200,
        'width': 620,
        'title': False,
        'resize_maxHeight': 250,
        'removePlugins': "stylesheetparser",
        # CKEDITOR.ENTER_P  1
        # CKEDITOR.ENTER_BR 2
        # CKEDITOR.ENTER_DIV 3 
        'forcePasteAsPlainText': True
    },
}

# Spot runtime warning of datetime
import warnings
warnings.filterwarnings('error',
                        r"DateTimeField .* received a naive datetime",
                        RuntimeWarning, r'django\.db\.models\.fields')

