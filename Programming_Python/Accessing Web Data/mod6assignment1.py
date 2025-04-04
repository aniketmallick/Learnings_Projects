import json
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if(len(url)<1):
    url = 'http://py4e-data.dr-chuck.net/comments_2189133.json'
html = urlopen(url, context=ctx).read()
data = json.loads(html)

sum = 0
count = 0
for num in data['comments']:
    sum = sum + num['count']
    count = count + 1

print("Sum - ",sum)
print("Count - ",count)


# data = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Brent"
#   }
# ]'''

# info = json.loads(data)
# print('User count:', len(info))

# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])