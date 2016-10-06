import urllib2
from bs4 import BeautifulSoup
import time
import random
import math
import requests
import re

def fetch(url,delay=(2,5)):
    """
    Simulate human random clicking 2..5 seconds then fetch URL.
    Returns the actual page source fetched and the HTML object.
    """
    time.sleep(random.randint(delay[0],delay[1])) # wait random seconds
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
    except ValueError as e:
        print str(e)
        return '', BeautifulSoup('', "html.parser")
    except:  # toss out any other issue
        return '', BeautifulSoup('', "html.parser")
    #response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    return (html,soup)

#one way to do it but its not counting for empty data so the zip is incorrect
def parseHN():
    i = 1
    prices = []
    bedrooms = []
    bathrooms = []
    while i < 63:
        page,html = fetch("http://www.homefinder.com/CA/San-Francisco/?page=%d" % i)
        print i
        for price in html.find_all(class_='price'):
            prices.append(price.text.encode('ascii','ignore'))
        for bed in html.find_all(class_='beds'):
            if len(bed.text) is None:
                bedrooms.append('--')
            else:
                bedrooms.append(bed.text.encode('ascii','ignore'))
        for bath in html.find_all(class_='baths'):
            bathrooms.append(bath.text.encode('ascii','ignore'))
        i += 1
    test = zip(prices, bedrooms, bathrooms)
    return test

#different way to do it but still don't know how to divide the data
def parseHN():
    i = 1
    data = []
    while i < 63:
        page,html = fetch("http://www.homefinder.com/CA/San-Francisco/?page=%d" % i)
        print i
        for item in html.find_all(class_= ['price','beds','baths']):
            data.append(item.text.encode('ascii','ignore'))
        i += 1
    return data

print parseHN()

