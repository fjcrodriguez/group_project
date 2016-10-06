import urllib2
from bs4 import BeautifulSoup
import math
import csv

baseUrl = 'http://www.rent.com/%s/%s/apartments_condos_houses_townhouses%s'

cityState = [('new-york', 'new-york'), ('illinois', 'chicago'), ('south-carolina', 'charleston'), ('nevada', 'las-vegas'),
             ('washington', 'seattle'), ('california', 'san-francisco'), ('district-of-columbia', 'washington'),
             ('louisiana', 'new-orleans'), ('california', 'palm-springs'), ('california', 'san-diego'), ('missouri', 'saint-louis'),
             ('arizona', 'sedona'), ('hawaii', 'honolulu'), ('florida', 'miami-beach'), ('missouri', 'branson'),
             ('massachusetts', 'boston'), ('georgia', 'savannah'), ('florida', 'orlando'), ('oregon', 'portland'),
             ('hawaii', 'lahaina'), ('florida', 'saint-augustine'), ('tennessee', 'nashville'), ('california', 'los-angeles'),
             ('texas', 'san-antonio'), ('texas', 'austin')]
bedroom = ['_1-bedroom', '_2-bedroom', '_3-bedroom']
citys = []
prices = []
addressList = []
rentbuy = []
zipcode = []
numBed = []
numBath = []
for city in cityState:
    for bed in bedroom:
        URL = baseUrl % (city[0], city[1], bed)
        response = urllib2.urlopen(URL)
        html = BeautifulSoup(response, 'html.parser')
        totalCount = int(html.find('span', {'class': 'total-listings-count'}).get_text())
        if totalCount >= 20:
            pageTotal = math.ceil(int(html.find('span', {'class': 'total-listings-count'}).get_text()) / 20)
        else:
            pageTotal = 1
        for i in range(int(pageTotal)):
            newURL = URL + '?page=' + str(i+1)
            response = urllib2.urlopen(newURL)
            html = BeautifulSoup(response, 'html.parser')
            items = html.find_all('div', {'class': 'prop li-srp'})
            for item in items:
                citys.append(city[1])
                rentbuy.append('rent')
                link = item.a['href']
                res = urllib2.urlopen('http://www.rent.com' + link)
                ht = BeautifulSoup(res, 'html.parser')
                address = str(ht.find('span', {'itemprop': 'streetAddress'}).get_text())
                addressList.append(address[0:address.index(' ')])
                postal = str(ht.find('span', {'itemprop': 'postalCode'}).get_text())
                zipcode.append(postal)
                price = str(item.find('p', {'class': 'prop-rent bullet-separator strong'}).get_text())
                if 'From' in price:
                    prices.append(int(price[6:]))
                elif ' ' not in price:
                    prices.append(int(price[1:]))
                else:
                    prices.append(int(price[1:price.index(' ')]))
                numOfBed = str(item.find('span', {'class': 'prop-beds bullet-separator'}).get_text())
                numBed.append(int(numOfBed[0]))
                numOfBath = str(item.find('span', {'class': 'prop-baths bullet-separator'}).get_text())
                numBath.append(int(numOfBath[0]))

output = [addressList, zipcode, prices, rentbuy, citys, numBed, numBath]
with open('rent_com.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(output)