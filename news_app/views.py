from django.shortcuts import render,redirect
from news_app.models import News
import random
from django.utils import timezone
from datetime import datetime
from django.db.models import Q
from django.http import Http404
from django.core.paginator import Paginator



# Create your views here.
def index(request):
    noticia = News.objects.filter(show=True).order_by('-id')#order_by('?')
    paginator = Paginator(noticia, 16)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'news_app/home.html',
                  {"lista_de_noticias": page_obj,
                    "title": "Portal News - Home",
                   },
                  
                  )


def search(request):
    texto_pesquisa = request.GET.get('q','').strip()
    if texto_pesquisa == "":
        return redirect('news_app:index')
    noticia = News.objects.filter(show=True).filter(
        Q(titulo__icontains = texto_pesquisa)
        )
    if len(noticia) == 0:
        return render(request,'global/nada_encontrado.html',)




    paginator = Paginator(noticia, 10) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'news_app/home.html',
                  {"lista_de_noticias": page_obj,
                   "pesquisa": texto_pesquisa,
                   "title": f"Portal News - {texto_pesquisa}",
                   }
                  )
