#!/bin/python

# Chapter 12 - Python for Informatics Exercises
# Sockets

# impot socket Library
import urllib
import re


url = raw_input('url: ')
if len(url) < 1: url = 'http://www.py4inf.com/code/'

# Retrieves the url and gets the html file
try:
    # Opens a file handler for the web page
    fhandler = urllib.urlopen(url)
    # Purts the content of the url to into a variable
    # works for small files and reasonable text files
    html = fhandler.read()
except:
    print '404'
    exit()

print html[:3000]
print 'Number of characters:', len(html)
