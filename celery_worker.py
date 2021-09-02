from celery import Celery
from etc.base_definitions import *
from utils.send_telegram import telegram_signal_send

celery = Celery(CELERY_NAME, broker=CELERY_BROKER, backend=CELERY_BACKEND)


@celery.task(name='celery_worker.send_telegram', bind=True)
def send_telegram(self, task_data):
    telegram_signal_send(
        chat_id=task_data.get('chat_id'),
        api_key=task_data.get('api_key'),
        text=task_data.get('text')
    )
