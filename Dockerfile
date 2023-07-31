FROM python:3.11.4

RUN apt-get update && apt install -y libpq-dev gdal-bin libgdal-dev

ENV PYTHONUNBUFFERED 1

WORKDIR /docu

COPY requirements.txt /docu/requirements.txt

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY docu/ /docu/

COPY .env-template /docu/.env

CMD python3 manage.py migrate && \
    python3 manage.py collectstatic --noinput && \
    gunicorn --bind 0.0.0.0:$PORT --env DJANGO_SETTINGS_MODULE=ramplus.settings ramplus.wsgi:application --timeout 30 --keep-alive 10 --log-level debug
