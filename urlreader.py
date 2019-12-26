import requests
from bs4 import BeautifulSoup
import csv

with open('output.csv', 'w', newline='') as output:
	writer = csv.writer(output)
	writer.writerow(["Link", "Price", "Address", "Surface", "Location"])

with open('apts.txt', 'r') as reader:
	for line in reader:
		url = line.rstrip('\n')
		response = requests.get(url)
		print("Working...")
		#print(response.request.url)
		soup = BeautifulSoup(response.content, "html.parser")
		myprice = soup.find("span", {"class": "price-tag-fraction"})
		#print(myprice.text)
		myaddress = soup.find("h2", {"class": "map-address"})
		#print(myaddress.text)
		mysurface = soup.find("dd", {"class": "align-surface"})
		#print(mysurface.text)
		mylocation = soup.find("h3", {"class": "map-location"})
		#print(mylocation.text)

		with open('output.csv', 'a', newline='') as output:
			writer = csv.writer(output)
			writer.writerow([url, myprice.text, myaddress.text, mysurface.text, mylocation.text])