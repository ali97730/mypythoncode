import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
#for Xml
import xml.etree.ElementTree as ET
import ssl
#from beautiful soup
from bs4 import BeautifulSoup


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#
url = "http://py4e-data.dr-chuck.net/comments_838524.xml"
html = urlopen(url, context=ctx).read()

html = urlopen(url).read()
tree= ET.fromstring(html)
lst = tree.findall('comments/comment')
summation=0
for item in lst:
    #print(item.find('count').text)
    summation+=int(item.find('count').text)

print(summation)
