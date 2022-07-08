FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ADD ../. /www/
WORKDIR /www
RUN pip install --no-cache-dir -r /www/requirements.txt
