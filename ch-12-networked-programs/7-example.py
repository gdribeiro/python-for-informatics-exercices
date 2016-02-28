#!/bin/python


# Chapter 12 - Python for Informatics Examples
# urllib

import urllib

# This program downloads a binary file (i.e. .jpg file) and writes it to the
# disk without having to wait all the file to be dowloaded
img = urllib.urlopen('http://www.py4inf.com/cover.jpg')
fhand = open('cover.jpg', 'w')

size = 0

while True:
    # the big number in the buffer just works to read everything that is in
    # the buffer at the moment
    info = img.read(100000)
    if len(info) < 1 : break
    size = size + len(info)
    fhand.write(info)

print size,'characters copied.'
fhand.close()
