# kaldi-env

Dyma broject Docker sy'n darparu amgylchedd hwylus a chaeth ar gyfer hyfforddi 
modelau ar gyfer adnabod lleferydd Cymraeg gyda Kaldi.


Ewch i'r gwefan swyddogol i wybod mwy am Kaldi: http://kaldi-asr.org/


Mae tair haen o amgylchoedd Docker wedi eu trefnu fel stac:


|                                                              |
----------------------------------------------------------------
|Amgylchedd/sgriptiau hyfforddi modelau Kaldi gyda data Cymraeg|
|Amgylchedd/cydrannau modelau iaith (SRILM neu IRSTLM)         |
|Amgylchedd/meddalwedd craidd Kaldi                            |
 

### Adeiladu'r Haenau
Er mwyn creu'r haen gwaelod, ewch i ffolder base ac yna:

```bash
$ cd base
$ make
```

Mae'r proses o adeiladu meddalwedd Kaldi yn cymryd peth amser. Ar ei diwedd bydd
yn profi'r amgylchedd ar gorpws bach syml ac yn dangos WER ('word error rate') o
0%.

Bydd delwedd newydd o fewn eich system Docker:

```bash
$ docker images
REPOSITORY                             TAG                 IMAGE ID            CREATED             SIZE
techiaith/kaldi-env-base               latest              9912c046466e        1 minute ago          9.37 GB
```

Ewch yn nesaf i'r ffolder srilm:

```bash
$ cd srilm
$ ls
Dockerfile  Makefile  srilm-1.7.1.tar.gz
```

Mae angen i chi estyn a llwytho i lawr y ffeil tar.gz srilm eich hunain o wefan
http://www.speech.sri.com/projects/srilm/

SRILM yw'r meddalwedd modelau iaith mae'r project Kaldi yn ei argymell fel y gorau ar gyfer Kaldi. 

Defnyddiwch y gorchymyn 'make' unwaith eto:


```bash
$ make
```

Ar ddiwedd adeiladu meddalwedd SRILM mae delwedd newydd arall yn bodoli o fewn Docker:

```bash
$ docker images
REPOSITORY                             TAG                 IMAGE ID            CREATED             SIZE
techiaith/kaldi-env-base               latest              9912c046466e        30 minutes ago       9.37 GB
techiaith/kaldi-env-base-srilm         latest              83cdba1d0fd3        1 minute ago         10.01 GB
```

Ewch yn ol i brif ffolder y project ac yna defnyddiwch 'make' eto er mwyn greu'r
amgylchedd hyfforddi modelau Kaldi ar gyfer y Gymraeg:

```bash
$ make
```

Ar ôl peth amser, fe fydd linell gorchymyn newydd yn ymddangos:

```bash
root@733ed0db77a6:/usr/local/src/kaldi/egs/paldaruo_welsh# 
```

Dilynwch y cyfarwyddiadau yn y ffeil README.txt 


Yn y cyfamser, mae eich system Docker yn cynnwys delwedd ar gyfer drydedd haen 
eich amgylchedd Kaldi:

```bash
$ docker images
REPOSITORY                             TAG                 IMAGE ID            CREATED             SIZE
techiaith/kaldi-env                    latest              f0806ba389cb        4 seconds ago       10.12 GB
techiaith/kaldi-env-base-srilm         latest              83cdba1d0fd3        10 minutes ago      10.01 GB
techiaith/kaldi-env-base               latest              9912c046466e        30 minutes ago      9.37 GB
```

  
 






