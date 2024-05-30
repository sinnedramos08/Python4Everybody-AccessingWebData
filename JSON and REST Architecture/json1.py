import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''
print(data)
info = json.loads(data)
print(info)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
