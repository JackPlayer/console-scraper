# scraper.py
import requests 
import pprint

URL = 'http://www.nhl66.ir/'

page = requests.get(URL)

pprint.pprint(page.text)