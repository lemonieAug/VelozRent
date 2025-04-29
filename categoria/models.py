from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    categoria_imagem = models.ImageField(upload_to='categorias/imagens/')
    slug = models.SlugField(max_length=100, unique=True)  # Adicionando o campo slug

    def __str__(self):
        return self.nome
