

# 📰 Projeto de Notícias

Projeto desenvolvido com **Django** para gerenciamento e exibição de notícias.

## 📋 Pré-requisitos

Antes de iniciar, certifique-se de ter o **Python** instalado em sua máquina.

### 1. Instale o Python

Baixe e instale a versão mais recente do Python pelo site oficial:

https://www.python.org/

Para verificar se a instalação foi realizada corretamente:

```bash
py --version
```

---

## 🚀 Instalação

### 2. Crie um ambiente virtual

Na pasta raiz do projeto, execute:

```bash
py -m venv venv
```

Ative o ambiente virtual:

**Windows:**

```bash
venv\Scripts\activate
```

---

### 3. Instale as dependências

Com o ambiente virtual ativado, instale os pacotes necessários:

```bash
pip install -r requirements.txt
```

---

## 🗄️ Banco de dados

### 4. Crie e aplique as migrações

Execute os comandos abaixo na raiz do projeto:

```bash
py manage.py makemigrations
py manage.py migrate
```

Esses comandos irão criar e atualizar as tabelas necessárias no banco de dados.

---

## 📰 Coleta de notícias

### 5. Popule o banco de dados

Entre na pasta responsável pela coleta das notícias:

```bash
cd script_news
```

Execute o script:

```bash
py collect_news.py
```

Após a execução, as notícias coletadas serão inseridas no banco de dados.

## ▶️ Executando o projeto

### 6. Inicie o servidor Django
Abra um no terminal.

Volte para a raiz do projeto:

```bash
cd ..
```

Execute o servidor:

```bash
py manage.py runserver
```

Por padrão, o Django ficará disponível em:

http://127.0.0.1:8000/

Abra o endereço no navegador para acessar a aplicação.

---

## 📁 Estrutura básica do projeto

```text
projeto/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── script_coleta_news/
│   └── colect_news.py
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
└── ...
```

## 🔄 Fluxo de execução

A sequência recomendada para configurar o projeto é:

```text
1. Instalar o Python
       ↓
2. Criar o ambiente virtual
       ↓
3. Ativar o ambiente virtual
       ↓
4. Instalar as dependências
       ↓
5. Criar/aplicar as migrações
       ↓
6. Executar a coleta de notícias
       ↓
7. Iniciar o servidor Django
```

---

## 🛠️ Tecnologias utilizadas

* Python
* Django
* SQLite
* HTML
* CSS

