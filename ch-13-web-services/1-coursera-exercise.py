#!/bin/python


# Chapter 13 - Python for Informatics


import urllib
# imports the xml library as ET, just gives it a easier name to type
# throughout the code
import xml.etree.ElementTree as ET

url = raw_input('Enter the url: ')
if len(url) < 1: url = 'http://python-data.dr-chuck.net/comments_230556.xml'

# u is a file handler for the webpage so it can be accessed as a file
u = urllib.urlopen(url)
# .read() extracts the html from the file handler
# in this case we are reading a xml file
data = u.read()

# extracts the tree from the xml file
tree = ET.fromstring(data)

# XPath selector string looks through the entire
# tree of XML for any tag named 'count'
counts = tree.findall('.//count')

soma = 0
for item in counts:
    # gets the text component of the tag
    soma += int(item.text)

print soma



# lat = results[0].find('geometry').find('location').find('lat').text
# lng = results[0].find('geometry').find('location').find('lng').text
# location = results[0].find('formatted_address').text
#
# print 'lat',lat,'lng',lng
# print location
