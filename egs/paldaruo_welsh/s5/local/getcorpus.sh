#!/bin/bash

usage() { echo "Usage: $0 -e <model name> -s <model language>" 1>&2; exit 1; }

DATA_URL=http://techiaith.cymru/corpws/Testunau
TEST_URL=http://techiaith.cymru/corpws/Testunau/Profi
DEST='data/local'

while getopts "e:s:" o; do
	case "${o}" in
		e)
			NAME=${OPTARG}		
			echo "Name of model/engine/collection : ${NAME}" 
			;;
		s)
			MODEL_LANG=${OPTARG}
			echo "Model language" : ${MODEL_LANG}
			;;
		*)
			usage	
			;;
	esac
done  
shift $((OPTIND-1))

if [ -z "${NAME}" ] || [ -z "${MODEL_LANG}" ]; then
    usage
fi

wget -P ${DEST} -N -nd -c -e robots=off -r -np ${DATA_URL}/${NAME}.tar.gz || \
 { echo "WGET error"'!' ; exit 1 ; }

tar -zxf ${DEST}/${NAME}.tar.gz --directory ${DEST}

for f in ${DEST}/*.${MODEL_LANG}
do
	echo "Processing file $f...."
	./tokenize.py -i $f -o $f.txt
done

find ${DEST} -type f -not -name '*.txt' | xargs rm 
mv ${DEST}/${NAME}.${MODEL_LANG}.txt ${DEST}/corpus.txt

