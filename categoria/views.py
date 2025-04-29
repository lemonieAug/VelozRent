from django.shortcuts import render, get_object_or_404
from .models import Categoria

def carros_por_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    return render(request, 'carros_por_categoria.html', {'categoria': categoria})
