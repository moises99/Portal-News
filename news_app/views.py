from django.shortcuts import render
from news_app.models import News
import random
from django.utils import timezone
from datetime import datetime
# Create your views here.
def index(request):
    noticia = News.objects.filter(show=True).order_by('?')[:372]
   
    return render(request,'news_app/home.html',
                {
                    "lista_de_noticias": noticia,
                 })