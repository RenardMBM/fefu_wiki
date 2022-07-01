#!/bin/bash

DJANGODIR=/www
# shellcheck disable=SC2164
cd ${DJANGODIR}
export PYTHONPATH=${DJANGODIR}:${PYTHONPATH}
python manage.py runserver 0.0.0.0:8000 "${PARAMS}"
