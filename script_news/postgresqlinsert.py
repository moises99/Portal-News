import psycopg
from datetime import datetime
# conn = psycopg.connect(
#     host="172.23.24.35",
#     port=5432,
#     dbname="seu_banco",
#     user="postgres",
#     password="sua_senha"
# )

# cursor = conn.cursor()

# cursor.execute("SELECT version()")

# print(cursor.fetchone())

# conn.close()
with psycopg.connect(host="172.23.24.35",port=5432,dbname="porta_news",user="moises",password="123456") as con:
    cursor = con.cursor()
    data_hj = datetime.now()
    t = True
    #cursor.execute(f"INSERT INTO news_app_news (titulo,url_noticia,url_imagem,data_criacao,show) VALUES ('Globo Esporte SP. João Fonseca faz 2-0 no número 14 do mundo e avança em Montreal 9999','https://globoplay.globo.com/v/14851661/','https://www.bing.com/th?id=ONUT.ykW76Ysag7-fL5_-3J4XUQ&pid=News&w=500&h=500&c=14&rs=2&qlt=100','{data_hj.strftime('%Y-%m-%d %H:%M:%S')}',{t})")
    cursor.execute('SELECT * FROM news_app_news')
    for row in cursor.fetchall():
        tss = row
        print(tss)



# 'INSERT INTO users (first_name, last_name, email) 
# VALUES ('John', 'Doe', 'john.doe@example.com');'