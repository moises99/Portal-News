echo "Instalando dependências..."
pip install -r requirements.txt

echo "Executando migrações do banco..."
python manage.py migrate --noinput

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput --clear
