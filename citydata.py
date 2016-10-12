import urllib2
from bs4 import BeautifulSoup
import time
import random


def fetch(url, delay=(2, 5)):
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
    return pagedata, html

def parseCityData(url):
    soup = fetch(url)
    citydata = soup[1].find_all(class_='median-income')
    tabledata = citydata[0].find_all(class_='hgraph')
    income = tabledata[0].find_all(class_='a')[0].nextSibling
    return income




def getMedianIncomes():
    cities = ['New-York-New-York', 'Chicago-Illinois', 'Charleston-South-Carolina', 'Las-Vegas-Nevada',
              'Seattle-Washington', 'San-Francisco-California',
              'Washington-District-of-Columbia', 'New-Orleans-Louisiana', 'Palm-Springs-California',
              'San-Diego-California', 'St.-Louis-Missouri', 'Sedona-Arizona',
              'Honolulu-Hawaii', 'Miami-Beach-Florida', 'Branson-Missouri', 'Boston-Massachusetts', 'Savannah-Georgia',
              'Orlando-Florida', 'Portland-Oregon',
              'Lahaina-Hawaii', 'St.-Augustine-Florida', 'Nashville-Davidson-Tennessee', 'Los-Angeles-California',
              'San-Antonio-Texas', 'Austin-Texas']

    median_incomes = []
    for city in cities:
        url = 'http://www.city-data.com/city/%s.html' % city
        median_income = parseCityData(url)
        median_incomes.append((city, median_income))














