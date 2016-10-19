#!/usr/bin/env python
import os, path, utils

data_dir = path.get_var('path.sh','DATA_ROOT')
text_file = open('data/train/text','w')

audio_data_files = utils.get_directory_structure(data_dir)

prompts = {}
with open(data_dir + "/samples.txt",'rb') as prompts_file:
	for line in prompts_file:
		elements = line.rstrip().split(' ',1)
		key = elements[0].replace('*/','')
		prompts[key]=elements[1]	
		

for speaker in audio_data_files['paldaruo_audio']:
	if (os.path.isdir(data_dir + "/" + speaker)):
		for wav in audio_data_files['paldaruo_audio'][speaker]:
			if (wav.startswith("silence")): continue
			wav_noext = wav.split('.')[0]
			fileid = speaker + "_" + wav_noext
			text = prompts[wav_noext]
			print fileid + "\t" + text
			text_file.write(fileid + ' ' + text + '\n')			

text_file.close()

