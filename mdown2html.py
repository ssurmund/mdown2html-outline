#!/usr/bin/python
# -*- coding: utf-8 -*- 

import markdown

html_header_top = """
<html>
<meta charset="UTF-8">
<style>
"""

html_header_bottom = """
</style>
<body>
"""

html_footer= """
</body>
</html>
"""

def mdown2html(input, style):
	html_body = markdown.markdown(input, extensions=['toc'])
	return (html_header_top + style + html_header_bottom + html_body + html_footer)
