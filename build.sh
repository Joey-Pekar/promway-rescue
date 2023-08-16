#!/usr/bin/env bash

set -o errexit # exit on error

poetry install

python manage.py tailwind build
python manage.py collectstatic --no-input
python manage.py migrate