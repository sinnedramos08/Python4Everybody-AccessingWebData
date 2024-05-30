import json, ssl
import urllib.request, urllib.parse

url=input("Enter Location: ")

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Open the URL to get the JSON file
uh = urllib.request.urlopen(url, context=ctx)
#Decode the content file to access it for processing
data = uh.read().decode()
#print(data)

#Create a dictionary like object 
info = json.loads(data)
#print(info)

print("Retrieving:", url)
print(f"Retrieved {len(data)} characters")


#Access the comments key (list type) where the data are "stored"
comments=info["comments"]

#Get Sum and Count
sum=0
count=0
#Check each element (dictionary type) in the comment list
for elements in comments:
    count=count+1
    sum=sum+int(elements["count"])

print("Count", count)
print("Sum", sum)
