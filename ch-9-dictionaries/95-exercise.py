#!/bin/python

fname = raw_input('Enter the file name: ')
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fhand = open(fname, 'r')
except:
    print 'Python was unable to open the file %s' % fname
    exit()

dic = dict()

for line in fhand:
    if not line.startswith('From '): continue
    line = line.split()
    line = line[1].split('@')
    word = line[1]
    dic[word] = dic.get(word, 0) + 1

sender = None
count = None

# dic.items() returns a tupple that can be iterated through the key value pairs
for key,value in dic.items():
    if count is None or value > count:
        sender = key
        count = value

print 'All the domain names: ', dic

print 'The domain name with most occurence: ', sender, count
