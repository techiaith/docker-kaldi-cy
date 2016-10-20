#!/usr/bin/env python

import os,sets
from argparse import ArgumentParser

phoneset = set()

phoneset.add('sil')

dest_dir = 'data/local/dict'
with open(dest_dir + '/silence_phones.txt','w') as silence:
    for phone in phoneset:
        silence.write(phone + '\n')

