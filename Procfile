web: gunicorn config.wsgi --log-file -
worker: celery -A config worker -l info