import requests
from bs4 import BeautifulSoup
import os
import shutil
from urllib.parse import urljoin, urlparse
import uuid

def clean_scraped_images(base_path):
    images_dir = os.path.join(base_path, 'scraped_images')
    if os.path.exists(images_dir):
        shutil.rmtree(images_dir)  # Supprime le dossier et son contenu
    os.makedirs(images_dir)  # Recrée le dossier vide

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
    return filename

def contenu_site(url, media_root):
    try:
        # Nettoyer le dossier des anciennes images avant de commencer
        clean_scraped_images(media_root)
        
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

        # Sauvegarder les images même si on ne les affiche pas
        images = soup.find_all('img')
        for img in images:
            src = img.get('src')
            if src:
                img_url = urljoin(url, src)
                save_image(img_url, media_root)

        return contenu

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête : {e}")
        return []