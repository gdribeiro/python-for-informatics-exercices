#!/bin/python

# Chapter 12 - Python for Informatics Exercises
# Sockets

# impot socket Library
import socket
import re


url = raw_input('url: ')
if len(url) < 1: url = 'http://www.py4inf.com/code/'
srv_port = 80

print 'URL: ',url

# Search for www. from the beginning of the url until the last caractere
# before the slash to get the host
# Import NOT get the slash, the connection doesn't work if the slash is present
srv = re.findall('(www.+?)/', url)[0]

# Creates the socket with AF_INET(internet) and SOCK_STREAM(TCP Protocol)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Connecting to ...'
print 'HOST: ', srv, ' PORT: ',srv_port
# Try to connect to the server
try:
    # Open theconnection to the server serv and port
    mysock.connect((srv, srv_port))
except:
    print 'Connection could not be established.'
    exit()

print 'Requesting the web page:','GET ' + url + ' HTTP/1.0\n\n'
# Send a GET request for teh
mysock.send('GET ' + url + ' HTTP/1.0\n\n')


while True:
    # reads data from the socket with the nuber of bytes in the .recv(*n-bytes*)
    data = mysock.recv(768)
    # checks if any data was actually read from the buffer
    if ( len(data) < 1 ) : break
    # prints it
    print data

# Closes the connection
mysock.close()
