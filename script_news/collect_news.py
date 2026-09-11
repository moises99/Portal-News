from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from time import sleep
from datetime import datetime
from rich.progress import track
import sqlite3
import os
import requests
from bs4 import BeautifulSoup
import django
import sys

#Configura o caminho reconhecer os imports
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# Define o módulo de configurações do projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news.settings')
django.setup()

# Agora você pode importar os models normalmente
from news_app.models import News
data_hj = datetime.now()


#[OK]
def colect_news():
    listp = []
    listt = []
    for index in track(range(8,26),description=" [yellow]Realizando as requisições... ",transient=True):
        try:
            url = (f'https://www.bing.com/news/feed/infinitescrollajax?fcvid=11AB92FC6C326685139485E56D1D67F0&PageIndex={index}&NewsBrowseDataVersion=mkt_dataversion-4-chieeeap002edf4_v1.0&InfiniteScroll=1')
            response = requests.get(url)
            if response.status_code == 200:
                pagina = BeautifulSoup(response.text, "html.parser")
                manchetes = pagina.select("div.news-card-body")
                for e,manchete in enumerate(manchetes):
                    titulo_el = manchete.select_one("a.title")
                    titulo = titulo_el.get_text(strip=True)
                    imagem_el = manchete.select_one(".image img")
                    imagem = imagem_el.get("src")
                    link = titulo_el.get("href")
                    if imagem[:20] != 'https://www.bing.com':
                        imagem = f'https://www.bing.com{imagem}'
                    listt.append(titulo.replace('"','').replace("'",""))
                    listt.append(link)
                    listt.append(imagem.replace('128&h','500&h').replace('128&c','500&c').replace('qlt=90','qlt=100'))
                    listacopia = listt[:]
                    listp.append(listacopia)
                    listt.clear()
                    
            else:
                ...
                #print('STATUS DA REQUISIÇÃO : ',response.status_code)
        except Exception as e:
            ...
        sleep(2)
    return [{'titulo':noticias[0],'url_noticia':noticias[1], 'url_imagem':noticias[2]} for noticias in listp]

def inserindo_dados():
    cont = 0
    cont2 = 0
    listp = colect_news()
    for listp in track(listp,description='Inserindo dados na base'):
        noticia_exite = News.objects.filter(titulo = listp["titulo"])
        data_hj = datetime.now()
        if noticia_exite:
            print(f'JÁ EXISTE: {noticia_exite}')
            cont2 +=1
        else:
            try:
                noticia = News.objects.create(titulo = listp["titulo"],url_noticia = listp["url_noticia"], 
                                url_imagem = listp["url_imagem"],
                                data_criacao = f'{data_hj.strftime('%Y-%m-%d %H:%M:%S')}',
                                show = True )
                cont+=1
            except  Exception as e:
                print('Dados nao Inseridos',e)
    
    #oculta_urls()
    print(f'Total de {cont}  notícas novas.')
    print(f'Total de {cont2} noticías repetidas.')



def rotina_coleta_de_noticias():
    while True:
        tempo = 600 #10 minutos 
        inserindo_dados()
        for t in range(tempo,0,-1):
            print(f'{t}s até a proxíma coleta..',end="\r",flush=False)
            sleep(1)


rotina_coleta_de_noticias()