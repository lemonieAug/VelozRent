#from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse('index.html')
    return render(request, 'index.html')

def carros_disponiveis(request):
    return render(request, 'carros.html')

def faq(request):
    return render(request, 'faq.html')

def login_usuario(request):
    return render(request, 'login.html')
