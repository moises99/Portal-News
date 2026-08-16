from django.shortcuts import render,redirect
from news_app.models import News
from django.db.models import Q
from django.http import Http404
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    data_at = News.objects.filter(show=True).order_by('-id').values_list('data_criacao').first()[0].strftime("%Hh:%Mm do dia %d/%m/%Y ")
    noticia = News.objects.filter(show=True).order_by('-id')#.order_by('?')
    #data_at = noticia.values_list('data_criacao').first()[0].strftime("%Hh:%Mm do dia %d/%m/%Y")
    paginator = Paginator(noticia, 16)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request,'news_app/home.html',
                  {"lista_de_noticias": page_obj,
                    "title": "Portal News - Home",
                    "data_at" : data_at
                   },
                  )


def search(request):
    data_at = News.objects.filter(show=True).order_by('-id').values_list('data_criacao').first()[0].strftime("%Hh:%Mm do dia %d/%m/%Y ")
    #data_at = noticiadt.values_list('data_criacao').first()[0].strftime("%Hh:%Mm do dia %d/%m/%Y ")
    #data_at = noticia.values_list('data_criacao').first()[0].strftime("%Hh:%Mm do dia %d/%m/%Y ")
    texto_pesquisa = request.GET.get('q','').strip()
    if texto_pesquisa == "":
        return redirect('news_app:index')
    noticia = News.objects.filter(show=True).filter(
        Q(titulo__icontains = texto_pesquisa)
        )

    if len(noticia) == 0:
        return render(request,'global/nada_encontrado.html',)

    paginator = Paginator(noticia, 16) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'news_app/home.html',
                  {"lista_de_noticias": page_obj,
                   "pesquisa": texto_pesquisa,
                   "title": f"Portal News - {texto_pesquisa}",
                    "data_at" : data_at
                   }
                  )
