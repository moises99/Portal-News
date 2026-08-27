import sqlite3
from rich.progress import track
from time import sleep
lista_alterada = []
lista_orignal = []
with sqlite3.connect('../db.sqlite3',timeout=10) as con:  
    cursor = con.cursor()
    cursor.execute('SELECT * FROM news_app_news')
    for row in track(cursor.fetchall(),description ="Alterando urls..."):
        ts = row[4]
        lista_orignal.append(str(ts))
        tss = (str(ts).replace('128&h','500&h').replace('128&c','500&c').replace('qlt=90','qlt=100'))
        cursor.execute(f'UPDATE news_app_news SET url_imagen="{tss}" WHERE url_imagen = "{ts}" ')
