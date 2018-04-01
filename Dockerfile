FROM debian:9.4-slim

MAINTAINER Hanspeter Gysin <hpgy59@gmail.com>

# Install required packages and make python3 the default python version
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       ca-certificates \
       imagemagick \
       python3 \
       wget \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3 1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


WORKDIR /app
ADD . .

# Install python pip and requirements
RUN wget -nv https://bootstrap.pypa.io/get-pip.py -O - | python \
    && pip install setuptools wheel \
    && pip install -r requirements.txt


# Use volume '/data' and provide a sym link '/app/data'
RUN mkdir /data && ln -s /data /app
VOLUME /data

EXPOSE 5000

CMD [ "python3", "manage.py", "runserver", "--host=0.0.0.0", "--no-debug" ]
