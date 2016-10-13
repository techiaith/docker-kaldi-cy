default: run

run : build

	docker run --name kaldi-env -i -t techiaith/kaldi-env bash

build:
	docker build --rm -t techiaith/kaldi-env .

clean: stop
	docker rmi techiaith/kaldi-env

stop:
	docker stop kaldi-env
	docker rm kaldi-env

