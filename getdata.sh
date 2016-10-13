#!/bin/bash

# defines the "DATA_ROOT" variable - the location to store data 
source ./path.sh

DATA_SRC="http://techiaith.cymru/corpws/Paldaruo/"
DATA_ZIP=${DATA_ROOT}/zip
DATA_EXTRACT=${DATA_ROOT}

source utils/parse_options.sh

mkdir -p ${DATA_ZIP} 2>/dev/null

# Check if the executables needed for this script are present in the system
command -v wget >/dev/null 2>&1 ||\
 { echo "\"wget\" is needed but not found"'!'; exit 1; }

echo "--- Starting data download (may take some time) ..."
wget -P ${DATA_ZIP} -N -nd -c -e robots=off -A zip -r -np ${DATA_SRC} || \
 { echo "WGET error"'!' ; exit 1 ; }
 
mkdir -p ${DATA_EXTRACT}

echo "--- Starting VoxForge archives extraction ..."
for a in ${DATA_ZIP}/*.zip; do
  unzip -d ${DATA_EXTRACT} $a
done

rm -rf ${DATA_ZIP}
