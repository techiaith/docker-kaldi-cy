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

RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash \
	&& apt-get update && apt-get install -y graphviz ghostscript sox git-lfs \
	&& apt-get clean \
	&& git lfs install \
 	&& rm -rf /var/lib/apt/lists/* 

WORKDIR /usr/local/src/kaldi/

CMD bash

