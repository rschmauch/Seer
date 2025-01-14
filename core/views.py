from django.shortcuts import render, redirect
from deep_translator import GoogleTranslator
from django.http import HttpRequest
from core.scraping.scraping_functionality import contenu_site
from core.ai.openaiHandler import newAiThread,askAIfor

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

def view_scraping(request):
    if request.method == 'POST':
        url = request.POST.get('link')
        language = request.POST.get('language', 'fr') 

        # Scraping du contenu
        contenu = contenu_site(url)

        text = ""
        if contenu:
            for element in contenu:
                if element.get('text'): 
                    text = text+element['name']+":"+element['text']+"\n"

        # Traitement par IA:
        thread = newAiThread()
        contenu = askAIfor(text,thread)
        
        

        try:
        # Effectuer la traduction avec Google Translator via deep_translator
            contenu = GoogleTranslator(source='auto', target=language).translate(contenu)
        except Exception as e:
            print(f"Erreur de traduction pour {element['text']}: {e}")
        
        return render(request, 'page/acceuil.html', {'contenu': contenu,"COLORS": COLORS,"LANGUAGES": LANGUAGES})
    
    return redirect('view_accueil')