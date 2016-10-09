import urllib2
from bs4 import BeautifulSoup
import math
import csv
import time

baseURL = 'https://www.trulia.com/for_sale/San_Francisco,CA/1p_beds/1p_baths/'
request = urllib2.Request(baseURL, headers={'User-Agent': "Resistance is futile"})
response = urllib2.urlopen(request)
html = BeautifulSoup(response, 'html.parser')
items = html.find_all('div', {'class': 'smlCol12 lrgCol8 ptm cardContainer'})
for item in items:
    link = item.a['href']
    #zip = link[-5:]
    newURL = 'https://www.trulia.com' + link
    newReq = urllib2.Request(newURL, headers={'User-Agent': "Resistance is futile"})
    newRep = urllib2.urlopen(newReq)
    newhtml = BeautifulSoup(newRep, 'html.parser')
    #price = str(newhtml.find('div', {'class':'h2 typeReversed typeDeemphasize man pan noWrap'}).get_text()).strip()
    bedBath = item.find(class_="cardDetails man ptm phm")
    numOfBed = bedBath.find(class_="iconBed").parent.text
    numOfBath = bedBath.find(class_='iconBath').parent.text
    print numOfBed, numOfBath
