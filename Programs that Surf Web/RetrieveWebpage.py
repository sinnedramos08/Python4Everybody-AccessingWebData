import urllib.request, urllib.parse, urllib.error
import ssl

#Ignore SSL Certificate Error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#Opens and read the URL and store the texty in a file handle
fh= urllib.request.urlopen(r"https://picoctf.org/about.html")

#No headers and metadata
#Treats the content of the url like a file



for line in fh:
    print(line.decode().strip())

