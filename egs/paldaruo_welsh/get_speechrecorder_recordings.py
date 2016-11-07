#!/usr/bin/env python
import sys, os, csv, path, utils, shutil, codecs
import xml.etree.cElementTree as ET
import xml.dom.minidom as Pretty

if __name__ == '__main__':

	try:
		speechrecorder_projects_home = str(sys.argv[1])
		project_name = str(sys.argv[2])
		dest_dir = str(sys.argv[3])

		if not project_name: raise 
		if not speechrecorder_projects_home: raise
		if not dest_dir: raise 
	except:
		print >> sys.stderr, "Usage %s <project_name> <speechrecorder_projects_home> <dest_name>" % sys.argv[0]
		sys.exit(0)

	source_dir_struct = utils.get_directory_structure(os.path.join(speechrecorder_projects_home,project_name))

	for speaker_dir in source_dir_struct[project_name]:
		fullpath = os.path.join(speechrecorder_projects_home, project_name, speaker_dir)
		if (os.path.isdir(fullpath)):
			print speaker_dir	
			speaker_dest_dir=os.path.join(dest_dir,speaker_dir)
			shutil.rmtree(speaker_dest_dir)
			os.makedirs(speaker_dest_dir)

			# copy pob ffolder
			for wav in source_dir_struct[project_name][speaker_dir]:
				print wav
				wav_target_filename = wav.replace(speaker_dir,'')
				shutil.copy(os.path.join(fullpath,wav),os.path.join(speaker_dest_dir,wav_target_filename))
				
			# ail-enwi pob ffeil wav 

			# diweddaru ffeil metadata.csv gyda enw'r ffolder (?)
	
