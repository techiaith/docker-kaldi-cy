#!/usr/bin/env python
import os, csv
import path

data_dir = path.get_var('path.sh','DATA_ROOT')

with open(data_dir + "/metadata.csv","rb") as metadata :
	dr=csv.DictReader(metadata)
	for i in dr:
		print i["uid"] + " " + i["rhyw"]
