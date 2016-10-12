import urllib2
from bs4 import BeautifulSoup
import time
import random
import math
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
        #print str(e)
        return '', BeautifulSoup('', "html.parser")
    except:  # toss out any other issue
        return '', BeautifulSoup('', "html.parser")
    #response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    return (html,soup)


def parseHN():
    # list = ['NY/New-York', 'IL/Chicago', 'SC/Charleston', 'NV/Las-Vegas', 'WA/Seattle', 'CA/San-Francisco',
    #         'DC/Washington','LA/New-Orleans', 'CA/Palm-Springs', 'CA/San-Diego', 'MO/Saint-Louis', 'AZ/Sedona', 'HI/Honolulu',
    #                 'FL/Miami-Beach/agent-broker', 'MO/Branson', 'MA/Boston', 'GA/Savannah/', 'FL/Orlando/agent-broker',
    #                 'OR/Portland', 'HI/Lahaina', 'FL/Saint-Augustine-Beach/agent-broker', 'TN/Nashville',
    #                 'CA/Los-Angeles', 'TX/San-Antonio', 'TX/Austin']
    list = ['NY/New-York']

    prices = []
    bedrooms = []
    bathrooms = []
    citystate = []
    direccion = []
    type = []
    for i in range(len(list)):
        page, html = fetch("http://www.homefinder.com/%s" % list[i])
        totalads = ''
        for item in html.find_all(class_='listingsFound'):
            totalads = item.text.encode('ascii', 'ignore')
        totalads = totalads.replace(',', '')
        totalpages = [int(s) for s in totalads.split() if s.isdigit()]
        totalpages = math.ceil(totalpages[0]/20.0)
        #print totalpages
        j = 1
        while j <= 5:
            page, html = fetch("http://www.homefinder.com/%s/?page=%d" % (list[i], j))
            for item in html.find_all(class_='resultsBands'):
                if item.find(class_='price') is not None and item.find(class_='beds') is not None and item.find(class_='baths') is not None and item.find('span', {'itemprop':'name'}) is not None and item.find(class_='cityStZip') is not None:
                    price = item.find(class_ ='price')
                    price = price.text.encode('ascii', 'ignore')
                    price = price.replace('$','')
                    price = price.replace(',','')
                    bedroom = item.find(class_='beds').text.encode('ascii', 'ignore')
                    city = item.find(class_='cityStZip').text.encode('ascii','ignore')
                    address = item.find('span',{'itemprop':'name'}).text.encode('ascii','ignore')
                    bathroom = item.find(class_='baths').text.encode('ascii', 'ignore')
                    direccion.append(address)
                    citystate.append(city)
                    prices.append(price)
                    bedrooms.append(bedroom)
                    bathrooms.append(bathroom)
                    type.append('sale')
            j += 1

    prc = []
    for i in range(len(prices)):
        prc.append(re.findall('\d+', prices[i])[0])

    zipcode = []
    for i in citystate:
        zipcode.append(i[-6:-1])

    city = []
    for i in citystate:
        city.append(i.split(','))

    cities = []
    for i in city:
        cities.append(i[0].strip())

    totalbeds = []
    for i in bedrooms:
        totalbeds.append(i[0])

    totalbaths = []
    for i in bathrooms:
        totalbaths.append(i[0])

    type = ['Buy' for i in range(len(zipcode))]

    return zip(direccion, zipcode, prc, type, cities, totalbeds, totalbaths)

# print direccion, zipcode, prices, type, cities, bedrooms, bathrooms
#
# print len(direccion), len(zipcode), len(prices), len(type), len(cities), len(bedrooms), len(bathrooms)


