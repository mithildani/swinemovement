FROM ubuntu:20.04
MAINTAINER Mithil Dani <danimithil@gmail.com>
ENV DEBIAN_FRONTEND="noninteractive" TZ="America/New_York"

RUN mkdir /config
RUN mkdir /libs

RUN apt-get update
RUN apt-get install -y python3.8
RUN apt-get install -y python3-pip
RUN apt-get install -y libpq-dev xz-utils libxext-dev libssl-dev libxrender1 zip unzip xvfb wget libfontconfig1
RUN apt-get install -y build-essential python3-dev python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

RUN mkdir -p /config
ADD requirements/base.txt /config/base.txt
ADD requirements/production.txt /config/requirements.txt
RUN pip3 install -r /config/requirements.txt

RUN mkdir -p /src;
WORKDIR /src
COPY . ./
