# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.random_number_page, name='random_number_page'),
]