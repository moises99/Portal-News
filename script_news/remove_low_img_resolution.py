import sqlite3
def oculta_urls():
    with sqlite3.connect('../db.sqlite3',timeout=10) as con:
        cursor = con.cursor()
        cursor.execute('UPDATE news_app_news SET show = False WHERE url_imagem LIKE "%16%"')