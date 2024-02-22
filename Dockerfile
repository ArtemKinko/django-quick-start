FROM python:3.12
ENV PYTHONUNBUFFERED=1

RUN mkdir "/django_app"
COPY ./django_app /django_app
RUN pip install -r /django_app/requirements.txt

WORKDIR /django_app/django_app