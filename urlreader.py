import requests
from bs4 import BeautifulSoup

with open('apts.txt', 'r') as reader:
	for line in reader:
		url = line.rstrip('\n')
		response = requests.get(url)
		print(response.request.url)
		soup = BeautifulSoup(response.content, "html.parser")
		myprice = soup.find("span", {"class": "price-tag-fraction"})
		print(myprice)
		myaddress = soup.find("h2", {"class": "map-address"})
		print(myaddress)
		mysurface = soup.find("dd", {"class": "align-surface"})
		print(mysurface)
		mylocation = soup.find("h3", {"class": "map-location"})
		print(mylocation)
