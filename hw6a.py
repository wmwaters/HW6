
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('td')
list_of_nums = []
for tag in tags:
	num_list = []
	num_list = re.findall('[0-9]+', str(tag))
	for item in num_list:
		list_of_nums.append(int(item))
print(sum(list_of_nums))
