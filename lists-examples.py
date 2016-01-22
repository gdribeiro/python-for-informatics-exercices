#!/bin/python

# Chapter 8 examples
#
# Lists are mutable, you can change individual items in it
#lista = ['ab', 'cd', 'ef']
#print lista
#print dir(lista)
#
# a = raw_input('Type: ')
# print a
#
# cheeses = ['cheddar', 'Edam', 'Gouda']
# numbers = [17, 123]
# floats = [0.0, 3.5, 9.5]
# empty = []
# print cheeses, numbers, empty, floats
#
# allofthem = cheeses + numbers + empty + floats
# print 'this is a list with multiple tipes in it', allofthem
# print type(allofthem)

# A list within another list
# Nested lists
# a = ['a', 'b', 'c']
# b = ['d', a, 'e']
# print 'This is a nested list: ', b
#
# # Lists are mutable and can have it's items changed infividually
# a[1]= 'z'
# print b
#
# # Interesting, 'z' is in a and a is in b but ifyou do the next commands it returns
# # false, so the command in is not recurssive ;)
# ifs = 'z' in b
# print ifs
#
# # Works only for items in the first level of the list, in items of nested lists
# # it is not effective!!
# ifs = 'd' in b
# print ifs

# Traversing lists
a = ['a','b','c','d','e']
b = ['f','g','h','i','j']
c = [0,1,2,3,4,5,6,7,8,9]

for x in a:
    print x

# It prints the squared numbers in the list
for i in c:
    print i**2

# Usint Comprehenssive Lists
print [x**2 for x in c]

# But we didn't alter the original list so far
print c

# To change the elements in the original list we need the indices
for i in c:
    c[i]= c[i]**2
print 'The original list now has changed: ', c
