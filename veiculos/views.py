# veiculos/views.py

from django.shortcuts import render, get_object_or_404
from categoria.models import Categoria

def carros_por_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    return render(request, 'index.html', {
        'categoria': categoria,
        'categorias': Categoria.objects.all()
    })

from veiculos.models import Carro

def carros_disponiveis(request):
    carros = Carro.objects.all()
    categorias = Categoria.objects.all()

    slug_categoria = request.GET.get('categoria')

    if slug_categoria:
        carros = carros.filter(categoria__slug=slug_categoria)

    return render(request, 'carros.html', {
        'carros': carros,
        'categorias': categorias
    })

def detalhe_carro(request, slug):
    carro = get_object_or_404(Carro, slug=slug)
    return render(request, 'carro-detalhe.html', {'carro': carro})