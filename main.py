from bs4 import BeautifulSoup
import requests
from csv import writer
import os

url = "https://www.worldometers.info/world-population/"


def scrape(url):
    response = requests.get(url)
    response = response.text
    soup = BeautifulSoup(response, 'html.parser')
    return soup


scraped = scrape(url)

tabl = scraped.find('table', id="popbycountry")

header = []  # Created empty list
# Extract Header Row
for i in tabl.find_all('th'):
    header.append(i.text)

path = os.path.join(os.getcwd(), "world_population_by_country.csv")

with open(path, 'wt', newline='', encoding='utf-8') as csv_file:
    csv_writer = writer(csv_file, delimiter='|')
    csv_writer.writerow(header)  # write header
    # Write data to csv file
    for row in tabl.find_all('tr')[1:]:
        td = row.find_all('td')
        r = [i.text.replace('\n', '') for i in td]
        csv_writer.writerow(r)