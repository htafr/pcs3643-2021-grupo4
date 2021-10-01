from django.db import models
from django.urls import reverse
from apps import settings
from datetime import date
from django import forms

CATEGORY_CHOICES = (
    ('Automotivos e Peças','Automotivos e Peças'),
    ('Beleza e Cuidados Pessoais', 'Beleza e Cuidados Pessoais'),
    ('Esporte','Esporte'),
    ('Brinquedos e Jogos','Brinquedos e Jogos'),
    ('Cozinha','Cozinha'),
    ('Eletrônicos', 'Eletrônicos'),
    ('Games e Consoles', 'Games e Consoles'),
    ('Livro','Livro'),
    ('Papelaria e Escritório', 'Papelaria e Escritório'),
    ('Pet Shop','Pet Shop'),
    ('Roupas Calçados e Acessórios', 'Roupas Calçados e Acessórios'),
)

CONDITION_CHOICES = (
    ('Novo','Novo'),
    ('Usado','Usado'),
)

class Lote(models.Model):
    name = models.CharField(max_length=200)
    summary = models.CharField(max_length=512, default='')
    qty = models.IntegerField(default=1)
    category = models.CharField(max_length=64, choices=CATEGORY_CHOICES, default='')
    condition = models.CharField(max_length=64, choices=CONDITION_CHOICES, default='')
    min_value = models.DecimalField(default=10, decimal_places=2, max_digits=16)
    opening_date = models.DateField(default=date.today)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('leilao_fbv:lote_edit', kwargs={'pk': self.pk})