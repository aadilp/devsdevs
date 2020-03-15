FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash postgresql-dev gcc python3-dev musl-dev
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt

