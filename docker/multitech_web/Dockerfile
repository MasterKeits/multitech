FROM python:3.6

RUN apt-get update && apt-get install -y \
		gunicorn \
		libxml2-dev libxslt-dev libjpeg-dev libssl-dev \
		ghostscript \
		libgs-dev \
		libmagickwand-dev \
		imagemagick \
		python-dev \
		python-pip

ADD ./gunicorn-log.conf /etc/gunicorn-log.conf
ADD ./gunicorn.conf.py /etc/gunicorn.conf.py

ADD ./requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

# For gunicorn logging
RUN pip install json-logging-py

RUN mkdir -p /opt/app
WORKDIR /opt/app

EXPOSE 8000
ENTRYPOINT ["gunicorn"]
CMD ["--bind", "0.0.0.0:8000", "--log-config", "/etc/gunicorn-log.conf", "-c", "/etc/gunicorn.conf.py",	"multitech_web.wsgi:application"]
