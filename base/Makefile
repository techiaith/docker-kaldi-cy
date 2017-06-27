os	:= $(shell uname -s)
ncpus	:= 1

ifeq (Linux, $(os))
	ncpus=$(shell grep -c ^processor /proc/cpuinfo)
endif

default: build

build:
	docker build --rm --build-arg NCPUS=$(ncpus) -t techiaith/kaldi-base .

clean: 
	docker rmi techiaith/kaldi-base

