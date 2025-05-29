from django.urls import path
from . import views

urlpatterns = [
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('adicionar/<int:carro_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover/<int:carro_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('confirmar/', views.confirmar_reserva, name='confirmar_reserva'),
    path('confirmar/<int:carro_id>/', views.reservar_carro, name='reservar_carro'),

]
