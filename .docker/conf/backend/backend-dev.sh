#!/bin/bash

DJANGODIR=/www
PYTHONPATH=/usr/bin/python3.9
# shellcheck disable=SC2164
export PYTHONPATH=/usr/bin/python3.9
whereis python
echo ${PYTHONPATH}
pip list # where packages
python manage.py runserver 0.0.0.0:8000 "${PARAMS}"
