worker: python manage.py makemigrations
worker: python manage.py migrate
web: gunicorn --bind 0.0.0.0:8000 backend.wsgi