#!/bin/python

# #!/bin/python

# Chapter 12 - Python for Informatics Examples
# Sockets

# impot socket Library
import socket

# Opens a connection over the internet AF_INET with TCP protocol SOCK_STREAM
# And asks toconnect to the server www.py4inf.com at the port 80
# standard for HTTP protocol
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
# Requests the file
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

page= str()
# The loop reads data from teh socket
while True:
    # reads data from the socket with the nuber of bytes in the .recv(*n-bytes*)
    data = mysock.recv(50)
    # checks if any data was actually read from the buffer
    if ( len(data) < 1 ) : break
    # if we just concatanate the data into another variable
    # we won't be printing the buffer and just the whole page
    # after the download finishes no matter the size of the buffer
    page = page + data

# Prints it
print page
# Close the socket connection
mysock.close()
