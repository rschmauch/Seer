from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from deep_translator import GoogleTranslator
from django.http import HttpRequest
from core.scraping.scraping_functionality import contenu_site
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.conf import settings 

COLORS = [{"name":"ry","display": "Red and Yellow"},{"name":"rb","display": "Red and Blue"}]
LANGUAGES = [{"name":"en","display": "English"},{"name":"fr","display": "Français"},{"name":"de","display": "Deutsch"}]

def view_accueil(request: HttpRequest):
    return render(request, './page/acceuil.html', {"COLORS": COLORS,"LANGUAGES": LANGUAGES}) 

def view_history(request: HttpRequest):
    return render(request, './page/history.html', {"COLORS": COLORS,"LANGUAGES": LANGUAGES}) 

def view_parametres(request: HttpRequest):
    return render(request, './page/parametres.html',{"COLORS": COLORS,"LANGUAGES": LANGUAGES} )

def view_login(request: HttpRequest):
    return render(request, './page/login.html',{"COLORS": COLORS,"LANGUAGES": LANGUAGES} )

@login_required
def view_acceuil_user(request: HttpRequest):
    return render(request, './page/acceuil_user.html', {"user": request.user} )

def view_scraping(request):
    if request.method == 'POST':
        url = request.POST.get('link')
        language = request.POST.get('language', 'fr')

        # Scraping du contenu
        contenu = contenu_site(url, settings.MEDIA_ROOT)
        
        if contenu:
            for element in contenu:
                if element.get('text') and element.get('type') == 'text':
                    try:
                        translated_text = GoogleTranslator(source='auto', target=language).translate(element['text'])
                        element['text'] = translated_text
                    except Exception as e:
                        print(f"Erreur de traduction pour {element['text']}: {e}")
        
        return render(request, './page/acceuil.html', {
            'contenu': contenu,
            'COLORS': COLORS,
            'LANGUAGES': LANGUAGES,
            'MEDIA_URL': settings.MEDIA_URL
        })
    
    return redirect('view_accueil')

def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Le nom d'utilisateur existe déjà.")
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Compte créé avec succès.")
            return redirect("view_login")

    return render(request, "page/login.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authentification de l'utilisateur
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Connexion réussie
            login(request, user)
            return redirect("view_acceuil_user")  # Redirige vers la page d'accueil utilisateur
        else:
            # Échec de connexion
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
            return redirect("login_user")  # Recharge la page de connexion pour afficher l'erreur

    return render(request, "page/login.html")