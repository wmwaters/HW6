import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

urlstart = (input('Enter - ')).strip()
times = int(input('Enter Count - '))
i = int(input('Enter Position - '))
print(urlstart)
for time in range(times):
	html = urllib.request.urlopen(urlstart).read()
	soup = BeautifulSoup(html,'lxml')
	tags = soup('a')
	urlstart = tags[i - 1].get('href', None)
	print(tags[i - 1].get('href', None))