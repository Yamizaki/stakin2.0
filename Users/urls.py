from django.urls import path, include 
from . import views
urlpatterns = [
    path('', views.Profile.as_view(), name='profile'),
]
