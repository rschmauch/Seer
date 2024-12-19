from django.shortcuts import render, redirect
from deep_translator import GoogleTranslator
from django.http import HttpRequest
from core.scraping.scraping_functionality import contenu_site

COLORS = [{"name":"ry","display": "Red and Yellow"},{"name":"rb","display": "Red and Blue"}]
LANGUAGES = [{"name":"en","display": "English"},{"name":"fr","display": "Français"}]

def view_accueil(request: HttpRequest):
    return render(request, './page/acceuil.html', {"COLORS": COLORS,"LANGUAGES": LANGUAGES}) 

def view_history(request: HttpRequest):
    return render(request, './page/history.html', {"COLORS": COLORS,"LANGUAGES": LANGUAGES}) 

def view_parametres(request: HttpRequest):
    return render(request, './page/parametres.html',{"COLORS": COLORS,"LANGUAGES": LANGUAGES} )

def view_scraping(request):
    if request.method == 'POST':
        url = request.POST.get('link')
        language = request.POST.get('language', 'fr') 

        # Scraping du contenu
        contenu = contenu_site(url)
        
        
        if contenu:
            for element in contenu:
                if element.get('text'):  
                    try:
                        # Effectuer la traduction avec Google Translator via deep_translator
                        translated_text = GoogleTranslator(source='auto', target=language).translate(element['text'])
                        element['text'] = translated_text  # Remplacer le texte original par la traduction
                    except Exception as e:
                        print(f"Erreur de traduction pour {element['text']}: {e}")
        
        return render(request, 'page/acceuil.html', {'contenu': contenu,"COLORS": COLORS,"LANGUAGES": LANGUAGES})
    
    return redirect('view_accueil')