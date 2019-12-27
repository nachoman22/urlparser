import requests
from bs4 import BeautifulSoup
import csv
import logging

logging.basicConfig(filename='urlreader.log', level=logging.INFO)

# Open file and read urls into dictionary. File descriptor is closed
# when out of the "with"
with open('apts.txt', 'r') as reader:
    url_list = reader.readlines()

# Initialize list for csv rows
csv_list = []
# Main logic
for url_item in url_list:
    url = url_item.rstrip('\n')
    # Retrieve response from url and separate desired items
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    myprice = soup.find("span", {"class": "price-tag-fraction"})
    myaddress = soup.find("h2", {"class": "map-address"})
    mysurface = soup.find("dd", {"class": "align-surface"})
    mylocation = soup.find("h3", {"class": "map-location"})

    if myprice != None and myaddress != None and mysurface != None and mylocation != None:
        logging.info('Data recorded for: ' + url)
        csv_list.append([url, myprice.text, myaddress.text, mysurface.text, mylocation.text])
    else:
        logging.warning('Missing value on the report for: ' + url)

with open('report.csv', 'w', newline='') as report:
    writer = csv.writer(report)
    # Write header
    writer.writerow(["Link", "Price", "Address", "Surface", "Location"])
    # Write rows from list
    for row in csv_list:
        writer = csv.writer(report)
        writer.writerow(row)