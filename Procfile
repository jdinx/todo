web: gunicorn --chdir django_todo/ mysite.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate