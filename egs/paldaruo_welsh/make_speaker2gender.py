#!/usr/bin/env python
import os, csv, path


data_dir = path.get_var('path.sh','DATA_ROOT')

spk2gender_file = open('data/train/spk2gender.map','w')
metadata_file = csv.DictReader(open(data_dir + '/metadata.csv'))

for row in metadata_file:
	try:
		speaker = row['uid']
		gender_cy = row['rhyw']

		if gender_cy == 'benyw':
			gender = 'f'
		else:
			gender = 'm'

		print speaker + ' ' + gender
		spk2gender_file.write(speaker + ' ' + gender + '\n')

	except:
		continue
