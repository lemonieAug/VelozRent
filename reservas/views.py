from django.shortcuts import render, redirect, get_object_or_404
from veiculos.models import Carro
from datetime import datetime

def adicionar_ao_carrinho(request, carro_id):
    carro = get_object_or_404(Carro, id=carro_id)
    data_inicio = request.POST.get('data_inicio')
    data_fim = request.POST.get('data_fim')

    if not data_inicio or not data_fim:
        return redirect('ver_carrinho')  # ou página anterior com mensagem de erro

    carrinho = request.session.get('carrinho', {})

    carrinho[str(carro_id)] = {
        'data_inicio': data_inicio,
        'data_fim': data_fim
    }

    request.session['carrinho'] = carrinho
    return redirect('ver_carrinho')

def remover_do_carrinho(request, carro_id):
    carrinho = request.session.get('carrinho', {})
    carrinho.pop(str(carro_id), None)
    request.session['carrinho'] = carrinho
    return redirect('ver_carrinho')

def ver_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    carros = []

    for carro_id, datas in carrinho.items():
        carro = get_object_or_404(Carro, id=int(carro_id))
        data_inicio = datetime.strptime(datas['data_inicio'], '%Y-%m-%d').date()
        data_fim = datetime.strptime(datas['data_fim'], '%Y-%m-%d').date()
        dias = (data_fim - data_inicio).days + 1
        total = dias * carro.preco_diario

        carros.append({
            'carro': carro,
            'data_inicio': data_inicio,
            'data_fim': data_fim,
            'dias': dias,
            'total': total
        })

    total_geral = sum(item['total'] for item in carros)

    return render(request, 'reservas.html', {
        'carros': carros,
        'total_geral': total_geral
    })

def confirmar_reserva(request):
    if not request.user.is_authenticated:
        return redirect('login')

    from .models import Reserva, ItemReserva

    carrinho = request.session.get('carrinho', {})
    if not carrinho:
        return redirect('ver_carrinho')

    reserva = Reserva.objects.create(usuario=request.user)

    for carro_id, datas in carrinho.items():
        carro = get_object_or_404(Carro, id=int(carro_id))
        ItemReserva.objects.create(
            reserva=reserva,
            carro=carro,
            data_inicio=datas['data_inicio'],
            data_fim=datas['data_fim']
        )

    # Limpa o carrinho
    request.session['carrinho'] = {}
    return redirect('ver_carrinho')

def reservar_carro(request, carro_id):
    carro = get_object_or_404(Carro, id=carro_id)
    return render(request, 'reservas/confirmar_reserva.html', {'carro': carro})
