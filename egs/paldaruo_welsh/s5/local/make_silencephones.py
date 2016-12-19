#!/usr/bin/env python
import os,sets, path
from argparse import ArgumentParser

dest_dir = path.get_var('path.sh','KALDI_LEXICON_ROOT')

phoneset = set()
optional_phoneset = set()

phoneset.add('sil')
phoneset.add('SPN')
optional_phoneset.add('sil')

with open(os.path.join(dest_dir,'silence_phones.txt'),'w') as silence:
    for phone in phoneset:
        silence.write(phone + '\n')

with open(os.path.join(dest_dir,'optional_silence.txt'),'w') as optsilence:
    for phone in optional_phoneset:
	optsilence.write(phone + '\n')
