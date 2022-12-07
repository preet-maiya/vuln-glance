#!/bin/bash

# run celerybeat
python3 -m celery -A src.celery:celery_app beat --loglevel=DEBUG &

# run celery workers
python3 -m celery -A src.celery:celery_app worker --loglevel=DEBUG &

# run flask server
python3 src/server.py