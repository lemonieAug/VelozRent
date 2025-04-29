# veiculos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('carros/<slug:slug>/', views.carros_por_categoria, name='carros_por_categoria'),
]
