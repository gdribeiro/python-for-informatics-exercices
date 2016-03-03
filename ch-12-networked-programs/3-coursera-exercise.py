#!/bin/python


# Chapter 12 - Python for Informatics Examples
# urllib

# impot socket Library
import urllib
from BeautifulSoup import *

url = raw_input('Enter the url: ')
if len(url) < 1: url = "http://python-data.dr-chuck.net/known_by_Darragh.html"
again = 7
pos = 18

# Read all the html into a string variable
# Ironically we call this variable html here
html = urllib.urlopen(url).read()

# Here the magic happens
soup = BeautifulSoup(html)
# With this we retrieve all teh Anchor tags <a></a> from the html file
tags = soup('a')

# Using BeautifulSoup is possible to extract diffets attributes form each tag
for i in range(0, again-1):
    url = tags[pos-1].get('href', None)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')
name = tags[pos-1].contents[0]
print name
