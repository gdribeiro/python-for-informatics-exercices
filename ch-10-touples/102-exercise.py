#!/bin/python



name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

ddd = dict()

for line in handle:
    if not line.startswith('From '): continue
    line = line.split()
    line = line[5]
    line = line.split(':')
    value = line[0]
    ddd[value] = ddd.get(value, 0) + 1


lst = list()

for k,v in ddd.items():
    lst.append( (k,v) )

lst.sort()

for k,v in lst[:100]:
    print k,v
