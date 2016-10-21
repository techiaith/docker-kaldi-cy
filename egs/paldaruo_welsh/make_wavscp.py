#!/usr/bin/env python
import os, path, utils, csv

data_dir = path.get_var('path.sh','DATA_ROOT')

train_dir = 'data/train'
test_dir = 'data/test'

audio_data_files = utils.get_directory_structure(data_dir)

def make_wavscp_file(source, destination):

	wavscp_file = open(destination + '/wav.scp','w')
	metadata_file = csv.DictReader(open(source))
	
	for row in metadata_file:
		speaker = row['uid']	
		if (os.path.isdir(data_dir + "/" + speaker)):
			for wav in audio_data_files['paldaruo_audio'][speaker]:
				if (wav.startswith("silence")): continue
				fileid = speaker + "_" + wav.split('.')[0]
				absolutepath = data_dir + "/" + speaker + "/" + wav
				print fileid + " " + absolutepath	
				wavscp_file.write(fileid + " " + absolutepath + "\n")

	wavscp_file.close()

make_wavscp_file(data_dir + '/training.csv', train_dir)
make_wavscp_file(data_dir + '/testing.csv', test_dir)

