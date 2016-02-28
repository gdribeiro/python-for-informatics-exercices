#!/bin/python


# Chapter 12 - Python for Informatics Examples
# urllib

# impot socket Library
import urllib
import re

# Opens a file handler for the webpage so it can be managed as a file
# Wonders of Python :D

url = "http://www.py4inf.com/"
# Opens the webpage and reads all the data into a string html
html = urllib.urlopen(url).read()

# Parsing a webpage using regular expressions to get all teh links
# Next we will be using a library to do all this, since to write all the
# regular expressions must get repetitive
links = re.findall('href="(http://.*?)"', html)
for link in links:
    print link
