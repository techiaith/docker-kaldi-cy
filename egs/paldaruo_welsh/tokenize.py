#!/usr/bin/env python

import sys, os, errno, re, codecs
from argparse import ArgumentParser

def tokenize_file(infile, outfile, **args):

	out_file = codecs.open(outfile,'wb+', encoding='utf-8')
	
	with codecs.open(infile,'r', encoding='utf-8') as in_file:
		for line in in_file.readlines():
			upper=line.rstrip('\n').upper()
			tokens = tuple(re.findall(r"(?:^|\b).(?:\B.)*",upper))

			upper=[]
			for token in tokens:
				if token.isalpha():
					upper.append(token)

			out_file.write(' '.join(upper) + "\n")
	
	out_file.close()

if __name__ == "__main__":
	
	parser = ArgumentParser(description="Trosi ffeil i gyd i upper, ei docyneiddio a'i baratoi ar gyfer hyfforddi model iaith")

	parser.add_argument('-i', '--in', dest="infile", required=True, help="y ffeil ar gyfer priflythrennu")
	parser.add_argument('-o', '--out', dest="outfile", required=True, help="i ble dylid cadw'r ffeil wedi'i priflythrennu")
	parser.set_defaults(func=tokenize_file)

	args=parser.parse_args()
	args.func(**vars(args))

