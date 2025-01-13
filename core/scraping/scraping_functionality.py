import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse
import uuid

def save_image(url, base_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Créer un nom de fichier unique
            ext = os.path.splitext(urlparse(url).path)[1] or '.jpg'
            filename = f"{uuid.uuid4()}{ext}"
            
            # Sauvegarder l'image
            path = os.path.join('scraped_images', filename)
            full_path = os.path.join(base_path, path)
            
            # Créer le dossier s'il n'existe pas
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            
            with open(full_path, 'wb') as f:
                f.write(response.content)
            return path
    except Exception as e:
        print(f"Erreur lors de la sauvegarde de l'image : {e}")
    return None

def contenu_site(url, media_root):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        contenu = []

        # Récupérer le texte
        elements = soup.find_all(['h1', 'h2', 'h3', 'p', 'li', 'a'])
        for element in elements:
            text = element.get_text(strip=True)
            if text:
                contenu.append({
                    'type': 'text',
                    'name': element.name.upper(),
                    'text': text
                })

        # Récupérer les images
        images = soup.find_all('img')
        for img in images:
            src = img.get('src')
            if src:
                # Convertir l'URL relative en URL absolue
                img_url = urljoin(url, src)
                # Sauvegarder l'image
                saved_path = save_image(img_url, media_root)
                if saved_path:
                    contenu.append({
                        'type': 'image',
                        'name': 'IMG',
                        'src': saved_path,
                        'alt': img.get('alt', '')
                    })

        return contenu

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête : {e}")
        return []