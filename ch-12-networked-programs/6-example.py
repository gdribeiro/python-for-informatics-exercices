#!/bin/python


# Chapter 12 - Python for Informatics Examples
# urllib

# impot socket Library
import urllib
from BeautifulSoup import *


url = raw_input('Enter the url: ')
if len(url) < 1: url = "http://www.dr-chuck.com/page1.htm"

html = urllib.urlopen(url).read()

# Here the magic happens
soup = BeautifulSoup(html)
# With this we retrieve all teh Anchor tags <a></a> from the html file
tags = soup('a')

# Using BeautifulSoup is possible to extract diffets attributes form each tag
for tag in tags:
    # Print the tag
    print 'TAG: ', tag
    # Thir extracts teh hhref attribute from the anchor tag
    print 'URL:', tag.get('href', None)
    # Extracts the content of the tag
    print 'Content: ', tag.contents[0]
    print 'Attributes: ', tag.attrs
