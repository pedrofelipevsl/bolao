from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class User(AbstractUser):
    nome = models.TextField()
    credito = models.FloatField()
    premiacaoGanha = models.FloatField()

class SelecaoDesafiante():
    nome = models.TextField()
    qtd_titulos = models.IntegerField()

class SelecaoVisitante():
    nome = models.TextField()
    qtd_titulos = models.IntegerField()

class Partida():
    selecao_visitante = models.ForeignKey(SelecaoVisitante, on_delete=models.CASCADE)
    selecao_desafiante = models.ForeignKey(SelecaoDesafiante, on_delete=models.CASCADE)
    
