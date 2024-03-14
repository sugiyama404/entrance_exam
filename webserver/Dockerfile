FROM python:3.8.8-buster
USER root

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
    locales=2.28-10+deb10u2 bash=5.0-4 && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 && \
    apt-get clean \
    && rm -rf /var/lib/apt/lists/*
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

WORKDIR /root/opt
COPY requirements.txt /root/opt/

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r /root/opt/requirements.txt

COPY . .

