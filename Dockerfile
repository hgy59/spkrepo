FROM debian:9.3-slim

MAINTAINER Hanspeter Gysin <hpgy59@gmail.com>

# Install required packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
	   imagemagick \
	   build-essential \
       python \
       python-pip \
	   python-setuptools \
       wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /app
ADD . .

# Install python pip and requirements
RUN wget -nv https://bootstrap.pypa.io/get-pip.py -O - | python \
    && pip install -r dev-requirements.txt

# Use volume '/data' and provide a sym link '/app/data'
RUN mkdir /data && ln -s /data /app/data
VOLUME /data

EXPOSE 5000

CMD [ "python", "manage.py", "runserver", "--host=0.0.0.0", "--no-debug" ]
