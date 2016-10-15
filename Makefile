default: run

run : build

	docker run --name kaldi-env -it -v $(PWD)/egs/paldaruo_welsh/:/usr/local/src/kaldi/egs/paldaruo_welsh/ techiaith/kaldi-env bash

build:
	docker build --rm -t techiaith/kaldi-env .

clean: stop
	docker rmi techiaith/kaldi-env

stop:
	docker stop kaldi-env
	docker rm kaldi-env

