from django.shortcuts import render, redirect
from django.http import HttpRequest
from core.scraping.scraping_functionality import contenu_site

def view_accueil(request: HttpRequest):
    return render(request, './page/acceuil.html') 

def view_scraping(request):
    if request.method == 'POST':
        url = request.POST.get('link')
        contenu = contenu_site(url)
        return render(request, 'page/acceuil.html', {'contenu': contenu})
    return redirect('view_accueil')