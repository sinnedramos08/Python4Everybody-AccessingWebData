import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user') #find all 'user' tag inside the 'users' parent tag complex type
print(lst) #returns an index type (probably a memory address) of list where the the 'user' tag is located
print('User count:', len(lst))


for item in lst:
    print('Name', item.find('name').text) #find the text inside the name tag
    print('Id', item.find('id').text) #find the text inside the id tag
    print('Attribute', item.get('x')) #get the value of the attribute x inside the user tag