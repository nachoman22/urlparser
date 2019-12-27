import requests
from bs4 import BeautifulSoup
import csv
import logging

logging.basicConfig(filename='urlreader.log',level=logging.INFO)

with open('report.csv', 'w', newline='') as report:
	writer = csv.writer(report)
	writer.writerow(["Link", "Price", "Address", "Surface", "Location"])

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
			logging.info('Data recorded for: ' + url)
			with open('report.csv', 'a', newline='') as report:
				writer = csv.writer(report)
				writer.writerow([url, myprice.text, myaddress.text, mysurface.text, mylocation.text])
		else:
			logging.warning('Missing value on the report for: ' + url)
