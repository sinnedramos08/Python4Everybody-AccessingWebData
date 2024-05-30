import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url= input("Enter Location: ")
print("Retrieving", url)

uh = urllib.request.urlopen(url, context=ctx)
data=uh.read()
print(f'Retrieved {len(data)} characters')

tree=ET.fromstring(data)
counts=tree.findall(".//count")

print("Count:",len(counts))

counter=0
sum=0
while(counter<len(counts)):
    sum=sum+int(counts[counter].text)
    counter=counter+1

print("Sum:",sum)
