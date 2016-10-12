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
FROM ubuntu:16.04
MAINTAINER Uned Technolegau Iaith, Prifysgol Bangor

RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN dpkg --add-architecture i386

# Setup Linux base environment
RUN apt-get update --fix-missing && apt-get upgrade -y
RUN apt-get install -q -y autoconf automake build-essential \
	git libtool libatlas3-base make python perl subversion \
	wget zlib1g-dev zip 

WORKDIR /usr/local/src
RUN wget https://github.com/kaldi-asr/kaldi/archive/master.zip
RUN unzip master.zip && mv kaldi-master kaldi && rm master.zip

WORKDIR /usr/local/src/kaldi/tools
RUN ./extras/check_dependencies.sh
RUN make

WORKDIR /usr/local/src/kaldi/src
RUN ./configure
RUN make depend
RUN make

CMD bash
