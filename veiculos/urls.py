# veiculos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    #path('<slug:slug>/', views.carros_por_categoria, name='carros_por_categoria'),
    path('', views.carros_disponiveis, name='carros'),  # Página de listagem de carros
    path('<slug:slug>/', views.detalhe_carro, name='detalhe_carro'),  # Página de detalhe do carro
]
