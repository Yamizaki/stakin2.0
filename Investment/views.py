from django.views.generic import ListView
from .models import InvestmentAccount
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import InvestmentAccountForm
from django.shortcuts import redirect

class InvestmentAccountListView(LoginRequiredMixin, ListView):
    model = InvestmentAccount
    template_name = "investment_account_list.html"  
    context_object_name = "accounts" 
    
    def get_queryset(self):
        return InvestmentAccount.objects.filter(profile=self.request.user.profile)


def create_investment_account(request):
    if request.method == 'POST':
        form = InvestmentAccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.profile = request.user.profile
            account.save()
            return redirect('account-list')
    return redirect('account-list')