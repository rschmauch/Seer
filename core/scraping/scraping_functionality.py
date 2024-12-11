import requests
from bs4 import BeautifulSoup
# import sys
# Configurer la sortie pour UTF-8
# sys.stdout.reconfigure(encoding='utf-8')

url_demo = 'http://www.scrapethissite.com/pages/simple/'
def contenu_site(url):
    try:
        # Envoyer une requête GET au site
        response = requests.get(url)
        response.raise_for_status()  # Vérifier si la requête a réussi (code 200)

        # Parse le HTML avec BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Récupérer tous les éléments textuels dans l'ordre
        elements = soup.find_all(['h1', 'h2', 'h3', 'p', 'li', 'a'])

        print("\nContenu du site dans l'ordre :\n")
        for element in elements:
            text = element.get_text(strip=True)
            if text:  # Ignorer les éléments sans texte
                print(f"{element.name.upper()}: {text}")
    
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête : {e}")

    

contenu_site(url_demo)
