#!/bin/python

# #!/bin/python

# Chapter 12 - Python for Informatics Examples
# urllib

# impot socket Library
import urllib

# Opens a file handler for the webpage so it can be managed as a file
# Wonders of Python :D
fhand = urllib.urlopen('http://www.py4inf.com/code/')
for line in fhand:
    print line.strip()
