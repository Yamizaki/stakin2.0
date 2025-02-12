import os
from celery import Celery

# Establece la configuración de Django para Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'staking.settings')

# Crea una instancia de Celery
app = Celery('staking')

# Carga la configuración desde settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubre y registra las tareas automáticamente
app.autodiscover_tasks()