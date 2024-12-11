from django.shortcuts import render
from django.http import HttpRequest


def view_accueil(request: HttpRequest):
    return render(request, './page/acceuil.html') 

def view_parametres(request: HttpRequest):
    return render(request, './page/parametres.html') 