import requests
from bs4 import BeautifulSoup
import sys

# Configurer la sortie pour UTF-8
sys.stdout.reconfigure(encoding='utf-8')

r = requests.get('http://www.scrapethissite.com/pages/simple/')
print(r.status_code)

def parse_country():
    r = requests.get('http://www.scrapethissite.com/pages/simple/')
    soup = BeautifulSoup(r.text, 'html.parser')

    # La méthode prettify() permet d'afficher le contenu de manière lisible, c'est pas obligatoire
    # print(soup.prettify())

    countries_cards = soup.find_all('div', class_='col-md-4 country')
    for card in countries_cards:
        country_name = card.find('h3').text.strip()
        # La méthode strip() permet d'enlever les espaces, c'est pas obligatoire
        print(country_name)

parse_country()
