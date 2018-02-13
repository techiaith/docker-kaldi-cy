default: build

run : 
	docker run --name kaldi -it -v $(PWD)/../kaldi-cy/paldaruo_welsh/:/usr/local/src/kaldi/egs/paldaruo_welsh/ -v $(PWD)/KALDI_HOME/:/root/kaldi-cy/ techiaith/kaldi bash

build:
	docker build --rm -t techiaith/kaldi .

clean: 
	docker rmi techiaith/kaldi

stop:
	docker stop kaldi
	docker rm kaldi

