from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField()
    content = models.TextField()
    date = models.DateTimeField(default=now)

    def __str__(self):
        return f"Historique de {self.user.username} - {self.date}"


class ScrapedContent(models.Model):
    type = models.CharField(max_length=10)  # 'text' ou 'image'
    content = models.TextField()  # texte ou chemin de l'image
    created_at = models.DateTimeField(auto_now_add=True)