import socket

mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #instance of socket object
#Connects the program to the server and socket
mysock.connect(("data.pr4e.org",80)) #connect method from socket class 

#Create an HTTP GET Request
command_GET= "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode() 
#\r\n\r\n means keyboard press enter enter
#Encode - converts string to collection of bytes
mysock.send(command_GET)

#Ready to get data from the socket after the GET request

while True:
    data=mysock.recv(1024) #Receive data from the socket, max size is 512 bytes
    if (len(data)<1):
        break
    print(data) #Decode the data (without \r \n and other special characters)



mysock.close()

'''
Sample of UnDecoded Data

b'HTTP/1.1 200 OK\r\nDate: Fri, 29 Sep 2023 08:08:53 GMT\r\nServer: 
Apache/2.4.18 (Ubuntu)\r\nLast-Modified: Sat, 13 May 2017 11:22:22 
GMT\r\nETag: "a7-54f6609245537"\r\nAccept-Ranges: bytes\r\nContent-Length: 
167\r\nCache-Control: max-age=0, no-cache, no-store, must-revalidate\r\nPragma: 
no-cache\r\nExpires: Wed, 11 Jan 1984 05:00:00 GMT\r\nConnection: 
close\r\nContent-Type: text/plain\r\n\r\nBut soft what light through yonder 
window breaks\nIt is the east and Juliet is the sun\nArise fair sun and 
kill the envious moon\nWho is already sick and pale with grief\n'

'''

'''
Sample of Decoded Data

#Metadata from here:
HTTP/1.1 200 OK
Date: Fri, 29 Sep 2023 08:08:01 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "a7-54f6609245537"
Accept-Ranges: bytes
Content-Length: 167
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain
#Metadata up to here:

#Text Data from the webpage
But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief
'''