
# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from reservas.models import Reserva


from reservas.models import Reserva, ItemReserva
from veiculos.models import Carro
from datetime import datetime


@login_required
def confirmar_reserva(request):
    carrinho = request.session.get('carrinho', [])

    if not carrinho:
        messages.error(request, "Seu carrinho está vazio.")
        return redirect('minhas_reservas')

    reserva = Reserva.objects.create(usuario=request.user)

    for item in carrinho:
        try:
            carro_id = item['carro_id']
            data_inicio = datetime.strptime(item['data_inicio'], '%Y-%m-%d').date()
            data_fim = datetime.strptime(item['data_fim'], '%Y-%m-%d').date()

            carro = Carro.objects.get(id=carro_id)

            ItemReserva.objects.create(
                reserva=reserva,
                carro=carro,
                data_inicio=data_inicio,
                data_fim=data_fim
            )
        except Exception as e:
            print(f">>> [ERRO] Falha ao adicionar item do carrinho: {e}")

    # Limpa o carrinho após confirmar
    request.session['carrinho'] = []

    messages.success(request, "Reserva confirmada com sucesso!")
    return redirect('minhas_reservas')



def register(request):
    if request.method == 'POST':
        print(">>> [DEBUG] Formulário POST recebido")

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        print(f">>> [DEBUG] Dados recebidos: nome={nome}, email={email}")

        if senha != confirmar_senha:
            print(">>> [DEBUG] Senhas não coincidem")
            messages.error(request, 'As senhas não coincidem.')
            return redirect('register')

        if User.objects.filter(username=email).exists():
            print(">>> [DEBUG] Usuário já existe")
            messages.error(request, 'Este e-mail já está em uso.')
            return redirect('register')

        user = User.objects.create_user(
            username=email,
            email=email,
            first_name=nome,
            password=senha
        )
        print(">>> [DEBUG] Usuário criado:", user)

        login(request, user)
        return redirect('cadastro_sucesso')

    return render(request, 'register.html')


def cadastro_sucesso(request):
    return render(request, 'cadastro-sucesso.html')

@login_required
def minhas_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user).prefetch_related('itens__carro')
    return render(request, 'usuarios/minhas_reservas.html', {'reservas': reservas})
    



