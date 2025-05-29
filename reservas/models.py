from django.db import models
from django.contrib.auth.models import User
from veiculos.models import Carro
from datetime import timedelta

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserva #{self.id} - {self.usuario.username}"

    def total_reserva(self):
        return sum(item.total_item() for item in self.itens.all())

class ItemReserva(models.Model):
    reserva = models.ForeignKey(Reserva, related_name='itens', on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return f"{self.carro.nome} ({self.data_inicio} a {self.data_fim})"

    def dias(self):
        return (self.data_fim - self.data_inicio).days + 1

    def total_item(self):
        return self.dias() * self.carro.preco_diario
