# default settings

DEBUG = True

PROJECT_NAME = ""
PROJECT_VERSION = ""

DATABASE_ENGINE = ""
DATABASE_NAME = ""
DATABASE_USER = ""
DATABASE_PASSWORD = ""
DATABASE_HOST = ""
DATABASE_PORT = ""

USE_I18N = True

DEFAULT_LOCALE = 'en_US'

DEFAULT_TIMEZONE = 'UTC'

MIDDLEWARE_CLASSES = (
)

SESSION_ENGINE = "memory"
SESSION_COOKIE = {
    'name': 'session_id',
    'age': 60 * 60 * 24 * 7 * 2,
    'domain': None,
    'path': '/'
}

INSTALLED_PACKAGES = (
)

PACKAGE_OPTIONS = {
}

