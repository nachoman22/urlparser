import requests
from bs4 import BeautifulSoup

url = "https://departamento.mercadolibre.com.ar/MLA-831154167-de-revista-espect-amplio-dpto-c-coch-y-renta-_JM"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

myprice = soup.find("span", {"class": "price-tag-fraction"})
print(myprice)
myprice.decompose()
myaddress = soup.find("h2", {"class": "map-address"})
print(myaddress)
myaddress.decompose()
mysurface = soup.find("dd", {"class": "align-surface"})
print(mysurface)
mysurface.decompose()
mylocation = soup.find("h3", {"class": "map-location"})
print(mylocation)
mylocation.decompose()
