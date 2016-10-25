#!/usr/bin/env python

import os,sets
from argparse import ArgumentParser

phoneset = set()
phoneset_add = phoneset.add

dest_dir = 'data/local/dict'

with open(dest_dir + '/lexicon.txt','rb') as lex:

    for line in lex:
        (key, val) = line.split(' ',1)
        val = val.lstrip().rstrip()
        phonemes = val.split(' ')

        [x for x in phonemes if not (x in phoneset or phoneset_add(x))]

sorted_phones = sorted(phoneset, key=lambda s: s.lower())

with open(dest_dir + '/nonsilence_phones.txt','w') as nonsilence:
    for phone in sorted_phones:
	if phone=='SPN': continue
        nonsilence.write(phone + '\n')

str_phones = ', '.join(sorted_phones)
print str_phones
