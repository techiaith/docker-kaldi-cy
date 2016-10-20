#!/bin/bash

DATA_SRC="http://techiaith.cymru/lts/"
DEST="data/local/dict"

# Check if the executables needed for this script are present in the system
command -v wget >/dev/null 2>&1 ||\
 { echo "\"wget\" is needed but not found"'!'; exit 1; }

echo "--- Starting data download ..."
wget -P ${DEST} -N -nd -c -e robots=off -A txt,lexicon -r -np ${DATA_SRC} || \
 { echo "WGET error"'!' ; exit 1 ; }
 

mv ${DEST}/cym.lexicon ${DEST}/lexicon
