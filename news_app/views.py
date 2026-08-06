from django.shortcuts import render
from news_app.models import News
# Create your views here.
def index(request):
    noticia = News.objects.filter(show=True).order_by('-id')
    # print(noticia)
    return render(request,'news_app/home.html',
                {"lista_de_noticias": noticia})