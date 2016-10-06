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

def parse_craigslist(url):
    soup = fetch(url)
    i = 1
    for row in soup[1].find_all(class_="row"):
        pricetag = row.find_all(class_="price")
        if len(pricetag) > 0:
            print pricetag[0].text, i
            i += 1


url_temp = 'http://www.city-data.com/city/%s.html'

cities = ['New-York-New-York', 'Chicago-Illinois', 'Charleston-South-Carolina', 'Las Vegas-Nevada', 'Seattle-Washington', 'San-Francisco-California',
           'Washington-District-of-Columbia', 'New-Orleans-Louisiana', 'Palm-Springs-California', 'San-Diego-California', 'St.-Louis-Missouri', 'Sedona-Arizona',
          'Honolulu-Hawaii', 'Miami-Beach-Florida', 'Branson-Missouri', 'Boston-Massachusetts', 'Savannah-Georgia', 'Orlando-Florida', 'Portland-Oregon',
          'Lahaina-Hawaii', 'Saint-Augustine-Florida', 'Nashville-Tennessee', 'Los-Angeles-California', 'San-Antonio-Texas', 'Austin, Texas']
















