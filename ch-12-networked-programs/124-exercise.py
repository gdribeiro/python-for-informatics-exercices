#!/bin/python


# Chapter 12 - Python for Informatics Exercises
# urllib
# BeautifulSoup

import urllib
from BeautifulSoup import *


url = raw_input('Enter the url: ')
if len(url) < 1: url = "http://pythonlearn.com/"

html = urllib.urlopen(url).read()

# Parses the html into a BeautifulSoup object
soup = BeautifulSoup(html)
# Extracts the tags
tags = soup('p')

print len(tags)

for t in tags:
    print t.contents[0]
