import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
i = 0

for tag in tags:
	if i==3:
		url_list = re.findall('[a-zA-Z0-9]+', str(tag))
		urlstr = str(url_list[0])
		print(urlstr)
		break
	i+=1
j = 0
while j < 4:
	html = urllib.request.urlopen(urlstr, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	i = 0
	for tag in tags:
		if i==3:
			url_list = re.findall('[a-zA-Z0-9]+', str(tag))
			urlstr = str(url_list[0])
			print(urlstr)
			break
		i+=1
	j+=1