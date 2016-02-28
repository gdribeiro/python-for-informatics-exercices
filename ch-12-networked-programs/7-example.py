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
    # writes to the disk before retrieve more data from the buffer
    # decreasing the memory usage
    # Although it increases the disk access what can slow down some stuff
    # so the best would be to have a buffer variable and after some amount of data
    # write it to the disk
    fhand.write(info)

print size,'characters copied.'
fhand.close()

# This is a beeter implementation of the same stuff
# import os
# import urllib
#
# print 'Please enter a URL like http://www.py4inf.com/cover.jpg'
# urlstr = raw_input().strip()
# img = urllib.urlopen(urlstr)
#
# # Get the last "word"
# words = urlstr.split('/')
# fname = words[-1]
#
# # Don't overwrite the file
# if os.path.exists(fname) :
#     if raw_input('Replace '+fname+' (Y/n)?') != 'Y' :
#         print 'Data not copied'
#         exit()
#     print 'Replacing',fname
#
# fhand = open(fname, 'w')
# size = 0
# while True:
#     info = img.read(100000)
#     if len(info) < 1 : break
#     size = size + len(info)
#     fhand.write(info)
#
# print size,'characters copied to',fname
# fhand.close()
