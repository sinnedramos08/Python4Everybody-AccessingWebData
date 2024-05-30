#XML library
import xml.etree.ElementTree as ET

#Multi line String
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

#Create an XML element tree object
tree = ET.fromstring(data)
print('Name:', tree.find('name').text) #Get Text between the tag name
print('Attr:', tree.find('email').get('hide')) #Get the value of the attribute "hide" from the tag "email"
