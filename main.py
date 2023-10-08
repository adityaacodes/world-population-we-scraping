from bs4 import BeautifulSoup
import requests

url = "https://www.worldometers.info/world-population/"


def scrape(url):
    response = requests.get(url)
    response = response.text
    soup = BeautifulSoup(response, 'html.parser')
    return soup


scraped = scrape(url)
