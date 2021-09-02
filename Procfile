web: gunicorn app:app --log-file=-
worker: celery --app="celery_worker" --loglevel=info --concurrency=1 worker