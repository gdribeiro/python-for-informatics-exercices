#!/bin/python

# #!/bin/python

# Chapter 12 - Python for Informatics Examples
# Sockets

# impot socket Library
import socket
import time

# Opens a connection over the internet AF_INET with TCP protocol SOCK_STREAM
# And asks toconnect to the server www.py4inf.com at the port 80
# standard for HTTP protocol
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
# Requests the file
mysock.send('GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n')
# The loop reads data from teh socket
count = 0
picture = "";
while True:
    data = mysock.recv(5120)
    if ( len(data) < 1 ) : break
    time.sleep(0.25)
    count = count + len(data)
    print len(data),count
    picture = picture + data

mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find("\r\n\r\n");
print 'Header length',pos
print picture[:pos]
# Skip past the header and save the picture data
picture = picture[pos+4:]
# wb in open() tell to open a binary file in writing mode
fhand = open("stuff.jpg","wb")
fhand.write(picture);
fhand.close()
