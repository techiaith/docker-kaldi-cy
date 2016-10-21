#!/usr/bin/env python
import os, path, utils, csv

data_dir = path.get_var('path.sh','DATA_ROOT')

train_dir = 'data/train'
test_dir = 'data/test'

audio_data_files = utils.get_directory_structure(data_dir)

def make_utt2spk_file(source, destination):
	
	utt2spk_file = open(destination + '/utt2spk','w')
	metadata_file = csv.DictReader(open(source))

	for row in metadata_file:
		speaker = row['uid']
		if (os.path.isdir(data_dir + "/" + speaker)):
			for wav in audio_data_files['paldaruo_audio'][speaker]:
				if (wav.startswith("silence")): continue
				fileid = speaker + "_" + wav.split('.')[0]
				print fileid + " " + speaker	
				utt2spk_file.write(fileid + " " + speaker + "\n")

	utt2spk_file.close()

make_utt2spk_file(data_dir + '/training.csv', train_dir)
make_utt2spk_file(data_dir + '/testing.csv', test_dir)
