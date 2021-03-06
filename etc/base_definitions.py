from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

TELEGRAM_API_KEY = environ.get("TELEGRAM_API_KEY")
TELEGRAM_CHAT_ID = environ.get("TELEGRAM_CHAT_ID")

CELERY_BROKER = environ.get('REDIS_URL')
CELERY_BACKEND = environ.get('REDIS_URL')

CELERY_NAME = environ.get('CELERY_NAME', 'default_name')

DEBUG = environ.get('DEBUG')
HOST = environ.get('HOST')
PORT = environ.get('PORT')
