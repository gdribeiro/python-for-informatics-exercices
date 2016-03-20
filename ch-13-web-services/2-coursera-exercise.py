#!/bin/python

# Chapter 13 - Python for Informatics

import urllib
# imports the json library
import json

url = raw_input('Enter the url: ')
if len(url) < 1: url = 'http://python-data.dr-chuck.net/comments_230560.json'

# print 'Retrieving', url
u = urllib.urlopen(url)
data = u.read()
# print 'Retrieved',len(data),'characters'

try: js = json.loads(str(data))
except: js = None

# print type(js["comments"])
sum = 0
for i in js["comments"]:
    sum += i["count"]
print sum
