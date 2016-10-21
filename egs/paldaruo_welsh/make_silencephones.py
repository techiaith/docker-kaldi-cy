#!/usr/bin/env python

import os,sets
from argparse import ArgumentParser

phoneset = set()
optional_phoneset = set()

phoneset.add('sil')
optional_phoneset.add('sil')

dest_dir = 'data/local/dict'
with open(dest_dir + '/silence_phones.txt','w') as silence:
    for phone in phoneset:
        silence.write(phone + '\n')

with open(dest_dir + '/optional_silence.txt','w') as optsilence:
    for phone in optional_phoneset:
	optsilence.write(phone + '\n')
