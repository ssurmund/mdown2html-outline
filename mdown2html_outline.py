#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys
import os

if len(sys.argv) != 2:
	print("ERROR: wrong number of arguements.")
	print("usage: python mdown2html_outline [directory]")
	exit(1)
else:
	directory = os.path.abspath(sys.argv[1])

from update_html import update_html
from create_outline import create_outline

script_directory = os.path.dirname(os.path.abspath(__file__))
html_style_file = os.path.join(script_directory, "styles/html.style")
outline_style_file = os.path.join(script_directory,"styles/outline.style")

update_html(directory, html_style_file)
create_outline(directory, outline_style_file)