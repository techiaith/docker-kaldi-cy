default: build

run : 
	docker run --name kaldi-env -it -v $(PWD)../kaldi-cy/paldaruo_welsh/:/usr/local/src/kaldi/egs/paldaruo_welsh/ techiaith/kaldi-env bash

build:
	docker build --rm -t techiaith/kaldi-env .

clean: stop
	docker rmi techiaith/kaldi-env

stop:
	docker stop kaldi-env
	docker rm kaldi-env

git-clone:
