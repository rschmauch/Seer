import requests
from bs4 import BeautifulSoup

def contenu_site(url):
    try:
        # Envoyer une requête GET au site
        response = requests.get(url)
        response.raise_for_status()  # Vérifier si la requête a réussi (code 200)

        # Parse le HTML avec BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Récupérer tous les éléments textuels dans l'ordre
        elements = soup.find_all(['h1', 'h2', 'h3', 'p', 'li', 'a'])

        # Créer une liste de dictionnaires avec les éléments
        contenu = []
        for element in elements:
            text = element.get_text(strip=True)
            
            # Vérifier que le texte n'est pas vide et qu'il est valide
            if text:  # Ignorer les éléments sans texte
                contenu.append({
                    'name': element.name.upper(),  # Par exemple, 'H1', 'P'
                    'text': text
                })

        return contenu

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête : {e}")
        return []
