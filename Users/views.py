from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class Profile(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_user"] = self.request.user  # Pasamos el usuario autenticado al template
        delta = self.request.user.last_login - self.request.user.date_joined
        years = delta.days // 365
        months = (delta.days % 365) // 30
        days = (delta.days % 365) % 30
        context["user_time"] = {
            "years": years,
            "months": months,
            "days": days,
        }
        return context

