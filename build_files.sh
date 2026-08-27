echo "Executando migrações do banco..."
python3.12 manage.py migrate --noinput

echo "Coletando arquivos estáticos..."
python3.12 manage.py collectstatic --noinput --clear
