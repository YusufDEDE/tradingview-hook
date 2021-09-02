from celery import Celery
from etc.base_definitions import *
from utils.send_telegram import telegram_signal_send

celery = Celery(CELERY_NAME, broker=CELERY_BROKER, backend=CELERY_BACKEND)


@celery.task(name='celery_worker.send_telegram', bind=True)
def send_telegram(self, kwargs):
    telegram_signal_send(
        chat_id=kwargs.get('chat_id'),
        api_key=kwargs.get('api_key'),
        text=kwargs.get('text')
    )
