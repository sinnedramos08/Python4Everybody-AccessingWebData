import socket

mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #instance of socket object
#Connects the program to the server and socket
mysock.connect(("data.pr4e.org",80)) #connect method from socket class 

#Create an HTTP GET Request
command_GET= "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode() 
#\r\n\r\n means keyboard press enter enter
#Encode - converts string to collection of bytes
mysock.send(command_GET)

#Ready to get data from the socket after the GET request

while True:
    data=mysock.recv(1024) #Receive data from the socket, max size is 512 bytes
    if (len(data)<1):
        break
    print(data.decode()) #Decode the data (without \r \n and other special characters)

mysock.close()

'''
Answers:
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "1d3-54f6609240717"
Content-Length: 467
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Content-Type: text/plain
'''