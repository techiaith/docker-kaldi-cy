#!/bin/bash

rm -rf /data/train
rm -rf /data/test

./make_speaker2gender.py
./make_utt2spk.py
./make_wav.py
./make_text.py
