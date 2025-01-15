"""
URL configuration for seer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import view_accueil, view_history, view_parametres, view_scraping, view_login, register_user,view_acceuil_user, login_user,view_scraping_user
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_accueil, name='view_accueil'),
    path('parametres', view_parametres, name='parmetres'),  
    path('history/', view_history, name='history'),
    path('scrape/', view_scraping, name='view_scraping'),
    path('scraping_user/', view_scraping_user, name='view_scraping_user'),
    path('login_page/', view_login, name='view_login'),
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),  
    path('acceuil_user/', view_acceuil_user, name='view_acceuil_user'), 
    path('history/', view_history, name='view_history'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

