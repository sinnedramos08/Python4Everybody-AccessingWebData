from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Initial url and position inputs
url = input("Enter url: ") 
url_count = int(input("Enter count: "))
url_position = int(input("Enter position: "))-1
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')

#initial print retrieve for the input url
print("Retrieving:", url)
#Repeat n times based on url_count
counter=0
while(counter<url_count):
    tag=tags[url_position] #Get the nth element in the tags list based on the soup object
    url=tag.get('href', None) #Get the nth element url
    print("Retrieving:",url) #Print the Retrieving url based on specification

    #Redo opening the next url and doing the soup object for next element
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags=soup("a")
    
    counter=counter+1