#!/bin/bash

python manage.py migrate --noinput
gunicorn --bind 0.0.0.0:${PORT:-8002} --workers 3 core.wsgi:application