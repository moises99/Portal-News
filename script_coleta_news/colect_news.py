from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from time import sleep
from datetime import datetime
import sqlite3
from rich.progress import track



#ANTES DE EXECULTAR ESSE SCRIPT NECESSÁRIOS CRIAR A BASE DE DADOS E TABELAS USANDO O ARQUIVO DE MODELS
data_hj = datetime.now()
con = sqlite3.connect('../db.sqlite3')
cursor = con.cursor()
# cursor.execute('DELETE FROM news_app_news')
# cursor.execute('DELETE FROM sqlite_sequence')
def colect_news():
    options=Options()
    options.add_argument("--headless=new")
    driver = webdriver.Edge(options=options)
    driver.get('https://www.bing.com/news')
    tempo = 60
    for c in track(range(tempo),description="Coletando Notícias...",total=tempo):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #Rolagem automatica da Pagina
        #print(f'Coletando as Noticias, Aguarde: {tempo-c}s', end="\r",flush=False)
        sleep(1)

    qtd_elementos = len(driver.find_elements(By.XPATH,"//div[@class='news-card newsitem cardcommon nosnip']"))
    for c in track(range(qtd_elementos),description="Inserindo dados no base...",total=qtd_elementos):
        meus_elementos = driver.find_elements(By.XPATH,"//div[@class='news-card newsitem cardcommon nosnip']")[c] #ELEMENTO PAI
        meus_elementos2 = meus_elementos.find_element(By.TAG_NAME,"img")#ELEMENTO FILHO
        titulo = meus_elementos.get_attribute('title')
        url = meus_elementos.get_attribute('url')
        urlimg = meus_elementos2.get_attribute('src')
        t = True
        try:
            cursor.execute(f'INSERT INTO news_app_news(titulo,url_noticia,url_imagen,data_criacao,show) VALUES ("{titulo}","{url}","{urlimg}","{data_hj.strftime("%Y-%m-%d %H:%M:%S")}",{t})')
            print(f'TITULO : {titulo} [OK]')
        except  Exception as e:
            print('Dados nao Inseridos',e)
    print(qtd_elementos)

    con.commit()
    con.close()
colect_news()