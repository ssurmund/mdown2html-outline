#!/usr/bin/python
# -*- coding: utf-8 -*- 

import codecs

from mdown2html import mdown2html 
from find_all_files import find_all_files

def update_html(root_dir, html_style_file):
	# get list of all markdown files in directory tree
	source_files = find_all_files(root_dir, ['*.mdown', '*.markdown'])

	# read style for creating the html files
	with codecs.open(html_style_file, mode='r', encoding="utf-8") as stylefile:
		style = stylefile.read()

	for mdfile in source_files:
		# read markdown file and create html
		with codecs.open(mdfile, mode='r', encoding="utf-8") as inputfile:
			mdown = inputfile.read()
			html = mdown2html(mdown, style)
		# write new html code to file
		htmlfile = mdfile + ".html"
		with codecs.open(htmlfile, mode='w', encoding="utf-8") as outputfile:
			outputfile.write(html)
