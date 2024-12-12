from django.shortcuts import render
from django.http import HttpRequest

COLORS = [{"name":"ry","display": "Red and Yellow"},{"name":"rb","display": "Red and Blue"}]
LANGUAGES = [{"name":"en","display": "English"},{"name":"fr","display": "Français"}]


def view_accueil(request: HttpRequest):
    return render(request, './page/acceuil.html') 

def view_parametres(request: HttpRequest):
    return render(request, './page/parametres.html',{"COLORS": COLORS,"LANGUAGES": LANGUAGES} ) 