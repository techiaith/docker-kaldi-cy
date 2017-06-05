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
FROM techiaith/kaldi-base-srilm
MAINTAINER Uned Technolegau Iaith, Prifysgol Bangor

RUN apt-get update && apt-get install -y graphviz ghostscript sox \
	&& apt-get clean \
 	&& rm -rf /var/lib/apt/lists/* \

#WORKDIR /usr/local/src/kaldi/egs/paldaruo_welsh

#RUN mkdir -p paldaruo_welsh/s5/local

#WORKDIR /usr/local/src/kaldi/egs/paldaruo_welsh/s5

#ADD egs/paldaruo_welsh/s5/conf/* ./
#ADD egs/paldaruo_welsh/s5/*.sh ./

#WORKDIR /usr/local/src/kaldi/egs/paldaruo_welsh/s5/local

#ADD egs/paldaruo_welsh/s5/local/*.sh ./
#ADD egs/paldaruo_welsh/s5/local/*.py ./

CMD bash

