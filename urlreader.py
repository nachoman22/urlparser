import requests
from bs4 import BeautifulSoup

with open('apts.txt', 'r') as reader:
	for line in reader:
		print(line, end='')
		response = requests.get(line)
		soup = BeautifulSoup(response.content, "html.parser")
		myprice = soup.find("span", {"class": "price-tag-fraction"})
		print(myprice)
		myaddress = soup.find("h2", {"class": "map-address"})
		print(myaddress)
		mysurface = soup.find("dd", {"class": "align-surface"})
		print(mysurface)
		mylocation = soup.find("h3", {"class": "map-location"})
		print(mylocation)