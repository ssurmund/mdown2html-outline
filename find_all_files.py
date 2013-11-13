#!/usr/bin/python
# -*- coding: utf-8 -*- 

import os
import fnmatch

def find_all_files(root_dir, pattern_list):
	file_list = []
	for path, dirs, files in os.walk(root_dir):
		for pattern in pattern_list:
			for filename in fnmatch.filter(files, pattern):
				file_list.append(os.path.join(path, filename))
	return file_list
	