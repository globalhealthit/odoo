FROM python:3.8

WORKDIR /app

RUN apt-get update -y && apt-get install -y postgresql && apt-get install -y postgresql-client && apt-get install -y libsasl2-dev && apt-get install -y python3-dev && apt-get install -y libldap2-dev && apt-get install -y libssl-dev && apt-get install -y wkhtmltopdf

COPY ./requirements.txt /requirements.txt

#RUN sed -n -e '/^Depends:/,/^Pre/ s/ python3-\(.*\),/python3-\1/p' /app/debian/control |  xargs apt-get install -y

RUN pip install -r /requirements.txt

COPY . /app

#CMD["python", "odoo-bin", "--addons-path=addons", "-d", "mydb"]
