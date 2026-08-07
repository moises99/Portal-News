# SITE DE NOTICIAS EM DESENVOLVIMENTO

### Instale os pacotes necessários
pip install -r requirements.txt

## Crie a base de dados 
py manage.py makemigrations  
py manage.py migrate  

### Popular base de dados
Na pasta script_coleta_news execulte o arquivo colect_news.py
py colect_news.py  


### Execulte a aplicação Django
Na raiz do projeto execute:  
py manage.py runserver  
