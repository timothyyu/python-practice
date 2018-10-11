# Example of request/response cycle with HTTP proctol
import socket
# internet layer and link layer implement transport layer
    # transport (end-to-end) layer
    # connection socket, connection to particular port
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Create socket/use this library (,stream/create endpoint type stream)
    # mysock object returned - makes the doorway, but nothing connected yet
mysock.connect(('data.pr4e.org', 80))
     # ((HOST, PORT))
     # makes the connection on port 80 and establishes socket

# call methods on socket object (send/recieve)
    # HTTP --> Server does recieve first, you do send first 
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
        # recieve up to 512 characters
    if len(data) < 1:
        # no data recieved --> end of file/end of transmission
        break

    print(data.decode(),end='')
        # Recieved in UTF-8 format (most likely) --> data.decode()-> Unicode
# close socket connection
mysock.close()
