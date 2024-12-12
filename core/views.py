from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.http import HttpRequest
from core.scraping.scraping_functionality import contenu_site

COLORS = [{"name":"ry","display": "Red and Yellow"},{"name":"rb","display": "Red and Blue"}]
LANGUAGES = [{"name":"en","display": "English"},{"name":"fr","display": "Français"}]

def view_accueil(request: HttpRequest):
    return render(request, './page/acceuil.html') 

def view_history(request: HttpRequest):
    return render(request, './page/history.html') 

def view_parametres(request: HttpRequest):
    return render(request, './page/parametres.html',{"COLORS": COLORS,"LANGUAGES": LANGUAGES} )

def view_scraping(request):
    if request.method == 'POST':
        url = request.POST.get('link')
        contenu = contenu_site(url)
        return render(request, 'page/acceuil.html', {'contenu': contenu})
    return redirect('view_accueil')