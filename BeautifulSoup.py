from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_838522.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
lst=list()
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag.contents)
    lst.append(tag.contents[0])
print(lst)  
summation=0
for i in lst:
    summation=summation+int(i)
print(summation)


