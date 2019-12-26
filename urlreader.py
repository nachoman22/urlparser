import requests
from bs4 import BeautifulSoup
import csv

with open('output.csv', 'w', newline='') as output:
	writer = csv.writer(output)
	writer.writerow(["Link", "Price", "Address", "Surface", "Location"])

with open('output.err', 'w', newline='') as errout:
	writer = csv.writer(errout)
	writer.writerow(["Missing values for the following links"])

with open('apts.txt', 'r') as reader:
	for line in reader:
		url = line.rstrip('\n')
		response = requests.get(url)
		soup = BeautifulSoup(response.content, "html.parser")
		myprice = soup.find("span", {"class": "price-tag-fraction"})
		myaddress = soup.find("h2", {"class": "map-address"})
		mysurface = soup.find("dd", {"class": "align-surface"})
		mylocation = soup.find("h3", {"class": "map-location"})

		if myprice != None and myaddress != None and mysurface != None and mylocation != None:
			print("Data recorded for", url)
			with open('output.csv', 'a', newline='') as output:
				writer = csv.writer(output)
				writer.writerow([url, myprice.text, myaddress.text, mysurface.text, mylocation.text])
		else:
			print("Missing value on the output for", url)
			with open('output.err', 'a', newline='') as errout:
				writer = csv.writer(errout)
				writer.writerow([url])