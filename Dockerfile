FROM python:2.7

ENV PYTHONUNBUFFERED 1

RUN git clone https://github.com/mushfiq/djmsc.git djmsc

WORKDIR djmsc

RUN pip install -r requirements.txt

RUN python manage.py migrate

CMD ["uwsgi", "--module=djmsc.wsgi:application", "--env=DJANGO_SETTINGS_MODULE=djmsc.settings", "--master", "--pidfile=/tmp/djmsc.pid", "--http=0.0.0.0:8000", "--socket=0.0.0.0:8001", "--buffer-size=32768"]

