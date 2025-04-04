# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count - '))
pos = int(input('Enter position - '))

seq_names = ""

while(count):
    # for i in range(0,pos):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    # print(tags[pos-1].contents[0])
    url = tags[pos-1].get('href',None)
    seq_names = seq_names + " " + tags[pos-1].contents[0]
    count = count - 1

last_name = seq_names.split()[len(seq_names.split())-1]

print(seq_names)
print(last_name)
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')


# Retrieve all of the anchor tags
# tags = soup('a')
# while
# for tag in tags:
#     print(tag.get('href', None))