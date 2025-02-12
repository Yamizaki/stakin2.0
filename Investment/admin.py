from django.contrib import admin
from .models import InvestmentAccount, InvestmentTransaction, InvestmentStaking
# Register your models here.
admin.site.register(InvestmentAccount)
admin.site.register(InvestmentTransaction)
admin.site.register(InvestmentStaking)