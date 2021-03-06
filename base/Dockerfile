#
# Copyright 2016 Prifysgol Bangor University
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
FROM ubuntu:16.04
MAINTAINER Uned Technolegau Iaith, Prifysgol Bangor University

ARG NCPUS
ENV NCPUS $NCPUS
RUN echo $NCPUS

RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN dpkg --add-architecture i386

# Setup Linux base environment
RUN apt-get update \ 
    && apt-get install -q -y autoconf automake build-essential \
	git libtool libatlas3-base make python python3 perl subversion \
	wget curl zlib1g-dev zip vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/src
RUN wget https://github.com/kaldi-asr/kaldi/archive/5.2.zip
RUN unzip 5.2.zip && mv kaldi-5.2 kaldi && rm 5.2.zip

WORKDIR /usr/local/src/kaldi/tools
RUN ./extras/check_dependencies.sh
RUN make -j $NCPUS

WORKDIR /usr/local/src/kaldi/src
RUN ./configure
RUN make depend
RUN make -j $NCPUS

CMD bash

