from django.db import models
from Users.models import Profile
from decimal import Decimal
class InvestmentAccount(models.Model):
    # Relación con el usuario (a través del perfil)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='investment_accounts')

    # Campos básicos de la cuenta de inversión
    account_name = models.CharField(max_length=100, unique=True)  # Nombre de la cuenta
    investment_amount = models.DecimalField(max_digits=15, decimal_places=2)  # Monto inicial
    pending_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Monto pendiente
    daily_return = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # Rendimiento diario (%)
    monthly_return = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # Rendimiento mensual (%)
    date_init = models.DateField()  # Fecha de inicio
    
    # Campos adicionales que podrían ser útiles
    commission_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Comisiones actuales
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Monto total
    
    is_active = models.BooleanField(default=False)  # Estado de la cuenta   
    pending_deposit = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de última actualización

    def deposit(self, amount):
        """Registra un depósito y calcula la ganancia mensual y diaria"""
        if amount > 0:
            self.pending_deposit = True
            self.pending_amount += amount
            self.save()

    def process_pending_deposits(self):
        """Procesa los depósitos pendientes, los añade al saldo y calcula rendimientos"""
        if  self.pending_deposit:
            self.investment_amount += self.pending_amount
            self.pending_amount = 0
            self.pending_deposit = False
            self.save()
            self.calculate_returns()  # Calcula rendimientos

    def calculate_returns(self):
        """Calcula automáticamente las ganancias diaria y mensual según el saldo"""
        self.total_amount = self.investment_amount + self.commission_balance
        self.daily_return = self.investment_amount * Decimal('0.005')  
        self.monthly_return = self.daily_return * 30  # Aproximación al mes
        self.save()

    def apply_daily_profit(self):
        """Añade la ganancia diaria al balance"""
        if self.is_active:
            self.commission_balance += self.daily_return
            self.save()
        
    def __str__(self):
        return f'{self.account_name} (Usuario: {self.profile.user.username})'
    
class InvestmentTransaction(models.Model):
    # Relación con la cuenta de inversión
    investment_account = models.ForeignKey(InvestmentAccount, on_delete=models.CASCADE, related_name='transactions')

    commission_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.0) 
    
    # Campos básicos de la transacción de inversión
    transaction_type = models.CharField(max_length=50, choices=[('deposit', 'Deposit'), ('withdraw', 'Withdraw'), ('payment_return', 'Payment Return')]) 
    amount = models.DecimalField(max_digits=15, decimal_places=2)  # Monto de la transacción
    date = models.DateField()  # Fecha de la transacción

class InvestmentStaking(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='investment_stakings')
    initial_amount = models.DecimalField(max_digits=15, decimal_places=2)
    monthly_return = models.DecimalField(max_digits=5, decimal_places=2)
    
    date_init = models.DateField()
    date_finish = models.DateField()
    
    time_investment = models.CharField(max_length=10, choices=[('3', '3 Months'), ('6', '6 Months'), ('9', '9 Months'), ('12', '12 Months')], default="6")