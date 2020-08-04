import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import ssl
import json
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#
url = "http://py4e-data.dr-chuck.net/comments_838525.json"
data = urlopen(url, context=ctx).read()


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

info = json.loads(data)
# print(info)
summation =0
for item in info['comments']:
    #print('Name', item['count'])
    # print('Id', item['id'])
    # print('Attribute', item['x'])
    summation= summation +int(item['count'])
print(summation)
