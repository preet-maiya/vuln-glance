#!/bin/bash

# run celerybeat
python3 -m celery -A src.celery_config:celery_app beat --loglevel=INFO &

# run celery workers
python3 -m celery -A src.celery_config:celery_app worker --loglevel=INFO &

# run flask server
python3 -m src.server