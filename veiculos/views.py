# veiculos/views.py

from django.shortcuts import render, get_object_or_404
from categoria.models import Categoria

def carros_por_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    return render(request, 'index.html', {
        'categoria': categoria,
        'categorias': Categoria.objects.all()
    })