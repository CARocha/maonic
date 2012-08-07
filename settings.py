# Django settings for maonic project.
from settings_local import *
TEMPLATE_DEBUG = DEBUG

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Managua'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-ni'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PROJECT_ROOT + '/media/'

STATIC_ROOT = ''
STATIC_URL = '/files/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/uploads/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '--xd_54^$2u*aasce&3ey8=+0+w-9tjaq3jgrz%!*^=3mz_@+j'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'maonic.urls'

TEMPLATE_DIRS = (
        PROJECT_ROOT + '/templates',
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.humanize',
    'maonic.mapeo',
    'maonic.noticias',
#    'maonic.monitoreo',
#    'registration',
    'maonic.lugar',
    'south',
    'smart_selects',
    'ckeditor',
    #app del monitoreo
    'maonic.encuestas',
    'maonic.organizacion',
    'maonic.tierra',
    'maonic.animales',
    'maonic.cultivos',
    'maonic.opciones_agroecologico',
    'maonic.semilla',
    'maonic.suelo',
    'maonic.inversiones',
    'maonic.ingresos',
    'maonic.propiedades',
    'maonic.credito',
    'maonic.seguridad',
    'maonic.riesgo',
)

ACCOUNT_ACTIVATION_DAYS = 3
ACCOUNT_ACTIVATION_DAYS = 2
LOGIN_REDIRECT_URL = '/'
EMAIL_HOST = 'maonic.simas.org.ni'
EMAIL_HOST_USER = 'no-reply@maonic.simas.org.ni'
EMAIL_HOST_PASSWORD = 'gatitobonito'
DEFAULT_FROM_EMAIL = 'no-reply@maonic.simas.org.ni'
NO_DATA_GRAPH_URL = '/files/images/NODATA.jpg'

#Configuracion del ckeditor

CKEDITOR_MEDIA_PREFIX = '/media/files/ckeditor/'

CKEDITOR_UPLOAD_PATH = PROJECT_ROOT + '/media/uploads/'

CKEDITOR_RESTRICT_BY_USER = True

CKEDITOR_CONFIGS = {
    'default': {
        'height': 300,
        'width': 650,
        'toolbar': [
            [ 
              'Undo', 'Redo',
              '-', 'Bold', 'Italic', 'Underline',
              '-','JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock',
              '-', 'Link', 'Unlink', 'Anchor',
              '-', 'Format',
              '-', 'SpellChecker', 'Scayt',
              '-', 'Maximize',
             ],
           [
              'HorizontalRule',
              '-', 'Table',
              '-', 'BulletedList', 'NumberedList','-','Outdent','Indent',
              '-', 'Cut','Copy','PasteText',
              '-', 'Source',
              '-', 'Superscript','Subscript','Font','Image',
              '-', 'FontSize',
            ]
        ],
        'toolbarCanCollapse': False,
        'skin':'office2003',
        'uiColor': '#EEe',
    }
}