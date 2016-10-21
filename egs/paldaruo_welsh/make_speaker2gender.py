#!/usr/bin/env python
import os, csv, path

data_dir = path.get_var('path.sh','DATA_ROOT')

train_dir = 'data/train'
test_dir = 'data/test'

def make_spk2gender_file(source, destination):
	print 'make_spk2gender(' + source + ', ' + destination + ')'

	spk2gender_file = open(destination + '/spk2gender.map','w')
	metadata_file = csv.DictReader(open(source))
	for row in metadata_file:
		speaker = row['uid']
		gender_cy = row['rhyw']
		if gender_cy == 'benyw': 
			gender= 'f'
		else: 
			gender= 'm'
		print speaker + ' ' + gender + ' (' + str(gender_cy) + ')'
		spk2gender_file.write(speaker + ' ' + gender + '\n')

	spk2gender_file.close()

make_spk2gender_file(data_dir + '/training.csv', train_dir)
make_spk2gender_file(data_dir + '/testing.csv', test_dir)

