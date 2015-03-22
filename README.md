mdown2html-outline
==================

*mdown2html-outline* is a simple Python tool to convert all markdown files in a directory tree into html files. Furthermore it creates a nice outline for these files.

**requirements:** 
The tool is developed on Ubuntu linux using Python2.7. It was not tested with Python3 so far, so there may be some small adaptions when using a new version of Python.  

**usage:** 
`python mdown2html_outline.py <rood-directory>`

As a result there is a new html file created next to each markdown file in the directory tree. Supported markdown file extensions are *.markdown*, *.mdown* and *.md*. Additionally an outline is created in the root directory containing links to each new html file.
