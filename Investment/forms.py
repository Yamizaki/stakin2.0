from django import forms
from .models import InvestmentAccount

class InvestmentAccountForm(forms.ModelForm):
    class Meta:
        model = InvestmentAccount
        fields = ["account_name"]  # Solo los campos que el usuario debe llenar
