#!/bin/sh



# Iniciar Gunicorn en segundo plano
gunicorn --bind 0.0.0.0:8000 staking.wsgi:application &

python manage.py collectstatic &
# Iniciar Tailwind en modo desarrollo
cd theme/static_src && npm run dev & cd ../../ python manage.py tailwind install

# Mantener el contenedor en ejecución
wait
