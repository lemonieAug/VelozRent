"""
URL configuration for VelozRent project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static #para rodar imagens
from VelozRent import settings #para rodar imagens
from . import views  # Importa views.py principal (para home, faq, login)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),               # Home
    #path('carros/', views.carros_disponiveis, name='carros'),  # Página geral de carros disponíveis
    path('faq/', views.faq, name='faq'),              # FAQ
    path('login/', views.login_usuario, name='login'), # Login

    # Aqui o que muda:
    path('carros/', include('veiculos.urls')),  # Deixa o veiculos.urls cuidar dos carros_por_categoria

    path('usuarios/', include('usuarios.urls')),  # Deixa o usuarios.urls cuidar do login, logout, etc.

    path('reservas/', include('reservas.urls')),  # Deixa o reservas.urls cuidar do carrinho, adicionar, remover, etc.
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #para rodar imagens com gambiarra

#Parei em 38
