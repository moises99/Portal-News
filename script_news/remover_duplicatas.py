import sqlite3

with sqlite3.connect('../db.sqlite3') as con:
    cursor = con.cursor()
    cursor.execute('SELECT * FROM news_app_news')
    for row in cursor.fetchall():
        tss = row
        ts = row[1]
        if str(ts).endswith('(1)',):
            with open('ducplicadostupla.txt','a',encoding='utf-8') as q:
                q.writelines(str(f'{tss[0]}\n'))
            with open('ducplicadostupla.txt','r') as ler:
                for c in ler:
                    try:
                        cursor.execute(f'DELETE FROM news_app_news WHERE ID = {c}')
                        for row in cursor.fetchall():
                            titulo = row[1]
                            print(f'DELETADO:{c}')
                    except Exception as e:
                        print(f'Não deletado:{c} com erro {e}')

