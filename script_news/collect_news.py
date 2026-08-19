from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep
from datetime import datetime
import sqlite3
from rich.progress import track
from remove_low_img_resolution import oculta_urls
import psycopg


def colect_news(tempo):
    listp = []
    listt = []
    options=Options()
    options.add_argument("--headless=new")
    driver = webdriver.Firefox(options=options)
    driver.get('https://www.bing.com/news')
    tempo = tempo
    for c in track(range(tempo),description="Aguardando página...",total=tempo):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #Rolagem automatica da Pagina
        sleep(1)
    qtd_elementos = len(driver.find_elements(By.XPATH,"//div[@class='news-card newsitem cardcommon nosnip']"))
    for c in track(range(qtd_elementos),description="Coletando informações...",total=qtd_elementos):
        meus_elementos = driver.find_elements(By.XPATH,"//div[@class='news-card newsitem cardcommon nosnip']")[c] #ELEMENTO PAI
        meus_elementos2 = meus_elementos.find_element(By.TAG_NAME,"img")#ELEMENTO FILHO
        titulo = meus_elementos.get_attribute('title')
        url = meus_elementos.get_attribute('url')
        urlimg = meus_elementos2.get_attribute('src')
        listt.append(titulo.replace('"','').replace("'",""))
        listt.append(url)
        listt.append(urlimg.replace('128&h','500&h').replace('128&c','500&c').replace('qlt=90','qlt=100'))
        listacopia = listt[:]
        listp.append(listacopia)
        listt.clear()
    driver.quit()
    return listp

def consultssql():
    with psycopg.connect(host="172.23.24.35",port=5432,dbname="porta_news",user="moises",password="123456") as con:
        cursor = con.cursor()
        lista_sql = []
        cursor.execute('SELECT * FROM news_app_news')
        for row in cursor.fetchall():
            ts = row[1]
            lista_sql.append(ts)
    return lista_sql


def inserindo_dados():
    cont = 0
    listp = colect_news(tempo = 60)
    lista_sql = consultssql()
    for listp in track(listp,description='Inserindo dados na base'):
        data_hj = datetime.now()
        t = True
        if listp[0] not in lista_sql:

            try:
                with psycopg.connect(host="172.23.24.35",port=5432,dbname="porta_news",user="moises",password="123456") as con:
                    cursor = con.cursor()
                    cursor.execute(f"INSERT INTO news_app_news (titulo,url_noticia,url_imagem,data_criacao,show) VALUES ('{listp[0]}','{listp[1]}','{listp[2]}','{data_hj.strftime('%Y-%m-%d %H:%M:%S')}',{t})")
                cont+=1
            except  Exception as e:
                print('Dados nao Inseridos',e)
    oculta_urls()
    print(f'Total de {cont} novas notícas.')


while True:
    tempo = 600 #10 minutos 
    inserindo_dados()
    for t in range(tempo,0,-1):
        print(f'{t}s até a proxíma coleta..',end="\r",flush=False)
        sleep(1)
    

