#!/usr/bin/env python

import os,sets
from argparse import ArgumentParser

questions = set()

dest_dir = 'data/local/dict'
with open(dest_dir + '/extra_questions.txt','w') as extraquestions:
    for question in questions:
        extraquestions.write(question + '\n')

