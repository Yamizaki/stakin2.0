from celery import shared_task
from django.utils import timezone
from Investment.models import InvestmentAccount, InvestmentTransaction
from django.db import transaction
import logging

logger = logging.getLogger(__name__)
@shared_task
def increment_account_balance():
    """
    Procesa los depósitos pendientes y los agrega a las cuentas correspondientes.
    """
    now = timezone.now()
    try:
        accounts = InvestmentAccount.objects.filter(is_active=True)
        for account in accounts:        
            # Supongamos que `initial_amount` representa los fondos pendientes
            account.apply_daily_profit()

            # Creamos un registro de transaccion 
            InvestmentTransaction.objects.create(investment_account=account, commission_balance=account.commission_balance, transaction_type="payment_return", amount=account.daily_return, date=now)
    except Exception as e:
        logger.error(f"Error al procesar las cuentas: {e}")
    return(f"COMISIONES -Procesadas {accounts.count()} cuentas a las {now}")

@shared_task
def process_pending_deposits():
    """
    Procesa los depósitos pendientes y los agrega a las cuentas correspondientes.
    """
    now = timezone.now()
    try:
        accounts = InvestmentAccount.objects.filter(pending_deposit=True)
        for account in accounts:
            # Supongamos que `initial_amount` representa los fondos pendientes
            account.process_pending_deposits()
            logger.info(f"DEPOSITO EXITOSO")
    except Exception as e:
        logger.error(f"Error al procesar las cuentas: {e}")
    return(f"DEPOSITOS - Procesadas {accounts.count()} cuentas a las {now}")
