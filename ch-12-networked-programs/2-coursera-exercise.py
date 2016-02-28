#!/bin/python


# Chapter 12 - Python for Informatics Examples
# urllib

# impot socket Library
import urllib
from BeautifulSoup import *

url = raw_input('Enter the url: ')
if len(url) < 1: url = "http://python-data.dr-chuck.net/comments_230559.html"

html = urllib.urlopen(url).read()

# Here the magic happens
soup = BeautifulSoup(html)
# With this we retrieve all teh Anchor tags <a></a> from the html file
tags = soup('span')

s = 0
# Using BeautifulSoup is possible to extract diffets attributes form each tag
for tag in tags:
    # Extracts the content of the tag
     s= s + int(tag.contents[0])

print s
