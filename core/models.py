from django.db import models

class ScrapedContent(models.Model):
    type = models.CharField(max_length=10)  # 'text' ou 'image'
    content = models.TextField()  # texte ou chemin de l'image
    created_at = models.DateTimeField(auto_now_add=True)