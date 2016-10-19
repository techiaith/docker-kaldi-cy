#!/usr/bin/env python
import os, path, utils

data_dir = path.get_var('path.sh','DATA_ROOT')
utt2spk_file = open('data/train/utt2spk','w')

audio_data_files = utils.get_directory_structure(data_dir)

for speaker in audio_data_files['paldaruo_audio']:
	
	if (os.path.isdir(data_dir + "/" + speaker)):

		for wav in audio_data_files['paldaruo_audio'][speaker]:

			if (wav.startswith("silence")):
				continue

			fileid = speaker + "_" + wav.split('.')[0]

			print fileid + " " + speaker	
			utt2spk_file.write(fileid + " " + speaker + "\n")

utt2spk_file.close()

