import requests
from bs4 import BeautifulSoup
from csv import writer as csv_writer
import logging

logging.basicConfig(filename='urlreader.log', level=logging.INFO)

# Open file and read urls into dictionary. File descriptor is closed
# when out of the "with"
## The file is not too big, read all to memory, there are other 
## methods if it's required to keep pointer open.
with open('apts.txt', 'r') as reader:
    url_list = reader.readlines()

# Initialize list for csv rows
csv_list = []
# Main logic
for url_item in url_list:
    url = url_item.rstrip('\n')
    # Retrieve response from url and separate desired items
    # TODO: would be nice to move this to a separated function/method
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    myprice = soup.find("span", {"class": "price-tag-fraction"})
    myaddress = soup.find("h2", {"class": "map-address"})
    mysurface = soup.find("dd", {"class": "align-surface"})
    mylocation = soup.find("h3", {"class": "map-location"})

    if myprice is not None and myaddress is not None and mysurface is not None and mylocation is not None:
        logging.info('Data recorded for: ' + url)
        csv_list.append([url, myprice.text, myaddress.text, mysurface.text, mylocation.text])
    else:
        # TODO: Verify if it's necesary to add the if logic or just 
        #       add the None to the csv, it can be filtered later on 
        #       with excel or any sheet tool.
        logging.warning('Missing value on the report for: ' + url)

# TODO: Add logging maybe to the writing of the csv file.
with open('report.csv', 'w', newline='') as report:
    writer = csv_writer(report)
    # Write header
    writer.writerow(["Link", "Price", "Address", "Surface", "Location"])
    # Write rows from list
    for row in csv_list:
        writer = csv_writer(report)
        writer.writerow(row)
