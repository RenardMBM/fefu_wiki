#!/bin/bash
DJANGODIR=/www
# shellcheck disable=SC2164
cd ${DJANGODIR}
export PYTHONPATH="${DJANGODIR}:${PYTHONPATH}"

exec gunicorn -c "./gunicorn_config.py" ${DJANGO_WSGI_MODULE}