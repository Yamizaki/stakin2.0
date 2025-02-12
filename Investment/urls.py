from django.urls import path
from .views import InvestmentAccountListView

urlpatterns = [
    path("", InvestmentAccountListView.as_view(), name="account-list"),
]
