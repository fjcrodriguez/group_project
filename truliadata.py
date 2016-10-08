import urllib2
from bs4 import BeautifulSoup
import math
import csv
import time
import random


def fetch(url,delay=(2,5)):
    """Simulate human random clicking 2..5 seconds then fetch URL.
    Returns the actual page source fetched and the HTML object."""

    time.sleep(random.randint(delay[0], delay[1]))
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
    except ValueError as e:
        print str(e)
        return '', BeautifulSoup('', "html.parser")
    except:
        return '', BeautifulSoup('', "html.parser")

    pagedata = response.read()
    html = BeautifulSoup(pagedata, "html.parser")
    return (pagedata,html)

city = ['newyork', 'chicago', 'charleston', 'lasvegas', 'seattle', 'sfbay', 'washingtondc', 'neworleons',
            'palmstrings', 'sandiego',
            'stlouis', 'flagstaff', 'honololu', 'miami', 'semo', 'boston', 'savannah', 'orlando', 'portland',
            'honolulu', 'staugustine',
            'nashville', 'losangeles', 'sanantonio', 'austin']

proptype = ['rea', 'apa']


cities = []
prices = []
addressList = []
rentbuy = []
zipcode = []
numBed = []
numBath = []

def parse_craigslist():
    for name in city:
        price, html = fetch("https://%s.craigslist.org/search/%s?s=%d&bathrooms=1&bedrooms=1")
        for
        i = 1
        for row in soup[1].find_all(class_="row"):
            pricetag = row.find_all(class_="price")
            if len(pricetag) > 0:
                print pricetag[0].text, i
                i += 1


parse_craigslist()






for name in city:
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

output = [addressList, zipcode, prices, rentbuy, cities, numBed, numBath]
with open('craigslist.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(output)