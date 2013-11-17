#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys
from StringIO import StringIO

import os
import codecs

from find_all_files import find_all_files
from mdown2html import mdown2html 


# redirect output for this script into output variable
output = StringIO()
sys.stdout = output


def create_filesystem_tree(file_list):
	filesystem_tree = {}
	for path in file_list:
		dct = filesystem_tree
		for path_part in path.split('/')[1:]:
			dct = dct.setdefault(path_part, {})
	return filesystem_tree


def print_filesystem_tree_markdown(filesystem_tree, file_list, tab=None):
	if not tab: 
		tab = ""
	for k,v in sorted(filesystem_tree.items()):
		if not v:
			path = filter(lambda x: k in x, file_list)[0]
			name = path.split('/')[-1].split('.')[0]
			print(tab   + "- " + "["+name+"]" + "("+path+")")
		else:
			print(tab + "- " + "**" + str(k) + "**")
			print_filesystem_tree_markdown(v, file_list, tab + "    ")		


def print_markdown(name, filesystem_tree, file_list):
	# print name as title
	print(name)
	print(len(name)*"=" + "\n")

	# print filesystem tree as list
	print_filesystem_tree_markdown(filesystem_tree, file_list)


def create_outline(dir_root, html_style_file):
	# change current working directory to dir_root
	os.chdir(dir_root)

	# set name for outline
	outline_name = os.path.abspath(dir_root).split('/')[-1]

	# set markdown and html files for outline
	mdfile = os.path.join(dir_root, "outline.mdown")
	htmlfile = os.path.join(dir_root, "outline.html")

	# remove outline html file, so it is not part of the outline
	try:
		os.remove(htmlfile)
	except OSError:
		pass

	# read directory tree and get all html files
	html_files = find_all_files('.', ['*.html'])

	# create tree datastructure based on html file list
	filesystem_tree = create_filesystem_tree(html_files)

	# print markdown completely
	print_markdown(outline_name, filesystem_tree, html_files)

	# write markdown to file
	with codecs.open(mdfile, mode='w', encoding="utf-8") as outfile:
		outfile.write(output.getvalue())

	# read style for creating the outline
	with codecs.open(html_style_file, mode='r', encoding="utf-8") as stylefile:
		style = stylefile.read()

	# read markdown outline file and create html 
	with codecs.open(mdfile, mode='r', encoding="utf-8") as inputfile:
		mdown = inputfile.read()
		html = mdown2html(mdown, style)
		
	# wirte new html outline to file
	with codecs.open(htmlfile, mode='w', encoding="utf-8") as outputfile:
		outputfile.write(html)
