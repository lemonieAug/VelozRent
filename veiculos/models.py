# veiculos/models.py

from django.db import models
from categoria.models import Categoria  # importa da sua outra app

class Carro(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco_diario = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='carros/', blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.nome
    
