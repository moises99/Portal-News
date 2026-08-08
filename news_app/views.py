from django.shortcuts import render
from news_app.models import News
import random
from django.utils import timezone
from datetime import datetime
from django.db.models import Q
from django.http import Http404,HttpResponse



# Create your views here.
def index(request):
    noticia = News.objects.filter(show=True).order_by('?')
   
    return render(request,'news_app/home.html',
                {
                    "lista_de_noticias": noticia,
                 })


def search(request):
    texto_pesquisa = request.GET.get('q','').strip().title()
    noticia = News.objects.filter(show=True).filter(
        Q(titulo__icontains = texto_pesquisa)
        )
    if len(noticia) == 0:
       raise Http404()
    
    return render(request,'news_app/home.html',
                {   "lista_de_noticias": noticia,
                    "pesquisa": texto_pesquisa,
                    })