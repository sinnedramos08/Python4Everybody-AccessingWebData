from bs4 import BeautifulSoup #installed in Python
import urllib.request, urllib.parse, urllib.error

url=input("Enter URL: ")
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html, 'html.parser')

#Retrieve all of the anchor tags, tags with links
tags=soup('a')

for tag in tags:
    print(tag.get("href",None))