from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):                                                       #Contient par défaut un mot de passe et des fonctions d'authentification
    email = models.EmailField(primary_key=True,unique=True,verbose_name="email")    #Stockage de l'email
    preferences = models.ForeignKey(verbose_name="preferences")                     #Stockage des préférences

    USERNAME_FIELD = "email"                                            #Pour définir l'email comme identifiant

class Preferences(models.Model):
    colorscheme = models.IntegerField(verbose_name="colorscheme")                    #Champ pour stocker le jeu de couleur voulu
    alwaysToText = models.BooleanField(default=False,verbose_name="alwaystotext")    #Champ pour stocker s'il faut activer l'option de mise en texte par défaut
    Language = models.CharField(max_length=5,blank=False, verbose_name="language")   #Champ pour stocker le language de l'utilisateur