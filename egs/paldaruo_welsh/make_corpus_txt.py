#!/usr/bin/env python
import os, path, utils, csv, codecs

def make_corpus_text_file(source_dir, prompts_file, destination):

	prompts = utils.get_prompts(os.path.join(source_dir,prompts_file))
	text_file = codecs.open(os.path.join(destination,'corpus.txt'),'w', encoding='utf-8')

	for key,value in prompts.items():
		text_file.write(value + '\n')
		
	text_file.close()

testdata_dir = path.get_var('path.sh','TEST_ROOT')
target_dir = 'data/local'
make_corpus_text_file(testdata_dir, 'samples.txt', target_dir)

