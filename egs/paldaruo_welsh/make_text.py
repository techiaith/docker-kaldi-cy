#!/usr/bin/env python
import os, path, utils, csv

data_dir = path.get_var('path.sh','DATA_ROOT')

train_dir = 'data/train'
test_dir = 'data/test'

audio_data_files = utils.get_directory_structure(data_dir)

prompts = {}
with open(data_dir + "/samples.txt",'rb') as prompts_file:
	for line in prompts_file:
		elements = line.rstrip().split(' ',1)
		key = elements[0].replace('*/','')
		prompts[key]=elements[1]	
		
def make_text_file(source, destination):

	text_file = open(destination + '/text','w')
	metadata_file = csv.DictReader(open(source))
	for row in metadata_file:
		speaker = row['uid']
		if (os.path.isdir(data_dir + "/" + speaker)):
			for wav in audio_data_files['paldaruo_audio'][speaker]:
				if (wav.startswith("silence")): continue
				wav_noext = wav.split('.')[0]
				fileid = speaker + "_" + wav_noext
				text = prompts[wav_noext]
				print fileid + "\t" + text
				text_file.write(fileid + ' ' + text + '\n')			

	text_file.close()

make_text_file(data_dir + '/training.csv', train_dir)
make_text_file(data_dir + '/testing.csv', test_dir)

