import urllib2
from bs4 import BeautifulSoup
import sys
import math

bedroom = ['_1-bedroom', '_2-bedroom', '_3-bedroom']


baseUrl = 'http://www.rent.com/south-carolina/charleston/apartments_condos_houses_townhouses%s?%s'
response = urllib2.urlopen(baseUrl % (sys.argv[1], sys.argv[2]))
html = BeautifulSoup(response, 'html.parser')
pageTotal = math.ceil(html.find('span', {'class':'total-listings-count'}).get_text() / 20)

#for bed in bedroom:
#    for i in range(pageTotal):


items = html.find_all('div', {'class':'prop li-srp'})
prices = []
addressList = []
for item in items:
    link = item.a['href']
    res = urllib2.urlopen('http://www.rent.com'+link)
    ht = BeautifulSoup(res, 'html.parser')
    address = ht.find('span', {'itemprop':'streetAddress'}).get_text()
    addressList.append(address)
    price = item.find('p', {'class':'prop-rent bullet-separator strong'}).get_text()
    prices.append(price)

print addressList
print prices
