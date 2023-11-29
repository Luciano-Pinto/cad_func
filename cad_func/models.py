from django.db import models
from django.utils import timezone


# Create your models here.


class Setor(models.Model):
    nome = models.CharField(max_length=255)
    data_criacao = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    data_contratacao = models.DateField(default=timezone.now)
    setor = models.ForeignKey(Setor, on_delete=models.DO_NOTHING, related_name='setor')

    def __str__(self):
        return self.nome
