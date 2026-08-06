from django.db import models
from django.utils import timezone


# Create your models here.

class News(models.Model):
    titulo = models.CharField(blank=True,max_length=255)
    url_noticia = models.CharField(blank=True,max_length=255)
    url_imagen = models.CharField(blank=True,max_length=255)
    data_criacao = models.DateTimeField(default=timezone.now)
    show = models.BooleanField(default=True)
    
    def __str__(self) ->str:
        return f'{self.titulo}'
