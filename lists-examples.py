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
# # Interesting, 'z' is in a and a is in b but if you do the next commands it returns
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
c = [0,1,2,3,4,5,6,7,8,9, 255]

# for x in a:
#     print x
#
# # It prints the squared numbers in the list
# for i in c:
#     print i**2
#
# # Usint Comprehenssive Lists
# print [x**2 for x in c]
#
# # But we didn't alter the original list so far
# print c
#
# # To change the elements in the original list we need the indices
# for i in range(len(c)):
#     c[i]= c[i]**2
# print 'The original list now has changed: ', c

# Combining lists

print a
print b
print c
# the * operator permits to repeat a list a desred number of times
# z= 2 * a+b * 3
# # The operation of concatenation with + does not alterates the orignal lists
# print z
# print a
# print b
#
# # the list method .append() does change the original list
# # it appends elements to a list
# a.append('z')
# print a
#
# # .extend() does a similar things than .append() but it does it with a list
# # the result is that all the elemets of the list passed as argument will be attached
# # to the list that
# a.extend(b)
# print b
# print a

# the .sort() method sorts the list accordinly with it's rules
b.extend(a)
print b
b.sort()
print b
# As we can see it is possible to sort a list taht contains multiple types
# and it works right, at least for ints and strings
b.extend(c)
print b
b.sort()
print b

# .pop() deletes the value passed in the function which is the index
# if no number is passed .pop() deletes the last element in the list
popped = b.pop(0)
print popped

# if the value doesn't need to be retrieved from the list you can use
# .del() which just deletes the item using its index

del b[4]
print b


# To delete an item you know but the index is not known you should use .remove()
b.remove(255)
print b

# To delete more than one element from the list in seqence it can be used the
# slicing of a list with del which chops off part of the list
del b[3:5]
print b

# We can separate a string in characteres and for a list with them
s = raw_input('Enter a string: ')
l = list(s)
print 'This is a list made of the characteres of the string: ', l

# We also can split strings using .split() based in a desired characters
s = raw_input('Enter a string: ')
l = raw_input('Enter the delimiter: ')

t = s.split(l)
print t

# we can also join strings in a list using a delimiter
# It can be thought of as the opposite of the .split()
# Althought it is called by the string that will be used limit the stirngs in the list
l = raw_input('Enter the delimiter: ')
t = l.join(t)
print t
