#from django.http import HttpResponse
from django.shortcuts import render

from categoria.models import Categoria
from veiculos.models import Carro

def home(request):
    #return HttpResponse('index.html')
    #return render(request, 'index.html')
    categorias = Categoria.objects.all()
    return render(request, 'index.html', {'categorias': categorias})

def carros_disponiveis(request):
    categorias = Categoria.objects.all()
    carros = Carro.objects.all()
    return render(request, 'carros.html', {'categorias': categorias , 'carros': carros})

def faq(request):
    return render(request, 'faq.html')

def login_usuario(request):
    return render(request, 'login.html')
