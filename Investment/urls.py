from django.urls import path
from .views import InvestmentAccountListView, create_investment_account

urlpatterns = [
    path("", InvestmentAccountListView.as_view(), name="account-list"),
    path("_create", create_investment_account, name="account-create"),
]
