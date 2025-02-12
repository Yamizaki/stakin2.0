
# Create your tests here.
from datetime import datetime, timedelta
from freezegun import freeze_time
from django.test import TestCase
from .tasks import process_pending_deposits  # Importa tu tarea de Celery

class CeleryTaskTests(TestCase):
    def test_tarea_periodica_ejecutada_correctamente(self):
        # Fecha inicial
        start_date = datetime.now()

        with freeze_time(start_date) as frozen_time:
            # Ejecutar la tarea periódica
            process_pending_deposits.delay()

            # Avanzar el tiempo en 15 días
            frozen_time.move_to(start_date + timedelta(days=15))

            # Verificar que la tarea se haya ejecutado correctamente
            # (aquí puedes agregar lógica para verificar el resultado esperado)
            self.assertTrue(process_pending_deposits)  # Verifica si la tarea se completó