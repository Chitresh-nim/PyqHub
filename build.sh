pip install -r requirements.text
python manage.py collectstatic --noinput
python manage.py migrate