FROM python:3.6

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./app/ ./app/
COPY ./project/ ./project/
COPY ./conf.ini ./
COPY ./manage.py ./
COPY ./start ./
COPY ./test ./

EXPOSE 8080
CMD ["uwsgi","--ini", "conf.ini"]
