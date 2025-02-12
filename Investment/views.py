from django.views.generic import ListView
from .models import InvestmentAccount

class InvestmentAccountListView(ListView):
    model = InvestmentAccount
    template_name = "investment_account_list.html"  # Ruta al template
    context_object_name = "accounts"  # Nombre de la variable en el template
