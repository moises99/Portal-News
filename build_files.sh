echo "Instalando dependências..."
pip install -r requirements.txt

echo "Executando migrações do banco..."
python3.14 manage.py migrate --noinput

echo "Coletando arquivos estáticos..."
python3.14 manage.py collectstatic --noinput --clear
