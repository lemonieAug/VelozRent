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

from django.shortcuts import render
from categoria.models import Categoria
from .models import Carro

def carros_disponiveis(request):
    carros = Carro.objects.all()
    categorias = Categoria.objects.all()

    slug_categoria = request.GET.get('categoria')

    modelo = request.GET.get('modelo')

    if modelo:
        carros = carros.filter(nome__icontains=modelo)


    # Defina antes do try para evitar UnboundLocalError
    preco_min = request.GET.get('preco_min')
    preco_max = request.GET.get('preco_max')

    if slug_categoria:
        carros = carros.filter(categoria__slug=slug_categoria)


    try:
        if preco_min:
            preco_min_valor = float(preco_min)
            carros = carros.filter(preco_diario__gte=preco_min_valor)
    except ValueError:
        pass

    try:
        if preco_max:
            preco_max_valor = float(preco_max)
            carros = carros.filter(preco_diario__lte=preco_max_valor)
    except ValueError:
        pass

    precos = list(carros.values_list('preco_diario', flat=True))
    preco_minimo = min(precos) if precos else None
    preco_maximo = max(precos) if precos else None

    return render(request, 'carros.html', {
        'carros': carros,
        'categorias': categorias,
        'preco_minimo': preco_minimo,
        'preco_maximo': preco_maximo
    })

def detalhe_carro(request, slug):
    carro = get_object_or_404(Carro, slug=slug)
    return render(request, 'carro-detalhe.html', {'carro': carro})