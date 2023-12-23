#!/bin/bash
python manage.py collectstatic --no-input

export WORKERS=${SERVER_WORKERS:-3}
export TIMEOUT=${WORKER_TIMEOUT:-180}
exec /home/pi/longanisa-maker/env/bin/gunicorn server.wsgi --workers=$WORKERS --timeout $TIMEOUT --bind 0.0.0.0:8000 --access-logfile -
