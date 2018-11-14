import os

from .settings import *  # noqa


SECRET_KEY = 'some-text-secret'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'gui.ifsp11@gmail.com'
EMAIL_HOST_PASSWORD = os.getenv('MY_EMAIL_PASS')
EMAIL_PORT = 587
