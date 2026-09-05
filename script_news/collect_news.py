from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from time import sleep
from datetime import datetime
from rich.progress import track
import sqlite3
import sqlite3
import os
import requests
from bs4 import BeautifulSoup


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'db.sqlite3')


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
                    # if len(listp) == 0 or titulo not in listp[0]:
                    listt.append(titulo.replace('"','').replace("'",""))
                    listt.append(link)
                    listt.append(imagem.replace('128&h','500&h').replace('128&c','500&c').replace('qlt=90','qlt=100'))
                    listacopia = listt[:]
                    listp.append(listacopia)
                    listt.clear()
                    
            else:
                print('STATUS DA REQUISIÇÃO : ',response.status_code)
        except Exception as e:
            ...
        sleep(2)

    return listp

def consultssql():
    with sqlite3.connect(DB_PATH) as con:
        cursor = con.cursor()
        lista_sql = []
        cursor.execute('SELECT * FROM news_app_news')
        for row in cursor.fetchall():
            ts = row[1]
            lista_sql.append(ts)
    return lista_sql

def oculta_urls():
    with sqlite3.connect(DB_PATH) as con:
        cursor = con.cursor()
        cursor.execute("UPDATE news_app_news SET show = False WHERE url_imagem LIKE '%16%'")

def inserindo_dados():
    cont = 0
    listp = colect_news()
    lista_sql = consultssql()
    for listp in track(listp,description='Inserindo dados na base'):
        data_hj = datetime.now()
        t = True
        if listp[0] not in lista_sql:
            try:
                with sqlite3.connect(DB_PATH) as con:
                    cursor = con.cursor()
                    cursor.execute(f"INSERT INTO news_app_news (titulo,url_noticia,url_imagem,data_criacao,show) VALUES ('{listp[0]}','{listp[1]}','{listp[2]}','{data_hj.strftime('%Y-%m-%d %H:%M:%S')}',{t})")
                cont+=1
            except  Exception as e:
                print('Dados nao Inseridos',e)
    
    oculta_urls()
    print(f'Total de {cont} novas notícas.')

def cn():
    while True:
        tempo = 600 #10 minutos 
        inserindo_dados()
        for t in range(tempo,0,-1):
            print(f'{t}s até a proxíma coleta..',end="\r",flush=False)
            sleep(1)
    


