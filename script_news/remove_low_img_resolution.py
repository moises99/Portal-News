import psycopg
def oculta_urls():
    with psycopg.connect(host="172.23.24.35",port=5432,dbname="porta_news",user="moises",password="123456") as con:
        cursor = con.cursor()
        cursor.execute("UPDATE news_app_news SET show = False WHERE url_imagem LIKE '%16%'")