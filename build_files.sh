echo "Executando migrações do banco..."
python manage.py migrate --noinput

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput --clear
