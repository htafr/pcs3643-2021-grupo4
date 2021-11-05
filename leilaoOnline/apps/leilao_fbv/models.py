from typing import Tuple
from django.db import models
from django.urls import reverse
from apps import settings
from datetime import date
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.apps import apps

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

BANK_CHOICES = (
    ('Itau Unibanco S.A.','Itau Unibanco S.A.'),
    ('Banco do Brasil S.A.', 'Banco do Brasil S.A.'),
    ('Banco Bradesco S.A.','Banco Bradesco S.A.'),
    ('Caixa Economica Federal','Caixa Economica Federal'),
    ('Banco Santander (Brasil) S.A.','Banco Santander (Brasil) S.A.'),
    ('NuBank', 'NuBank'),
    ('C6','C6'),
    ('Banco Inter S.A.', 'Banco Inter S.A.'),
)

####################################################################################
### Vendedor #######################################################################
####################################################################################

class Vendedor(models.Model):
    name = models.CharField(max_length=256)
    username = models.CharField(max_length=16, default='', unique=True)
    email = models.CharField(max_length=256, default='', unique=True)
    password = models.CharField(max_length=16, default='')
    address = models.CharField(max_length=256)
    birth_date = models.DateField(default=date.today)
    rg = models.CharField(max_length=9, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    bank = models.CharField(max_length=64, choices=BANK_CHOICES, default='')
    agency = models.IntegerField(default=1)
    account_number = models.CharField(max_length=64, unique=True)
    
class VendedorForm(ModelForm):
    class Meta:
        model = Vendedor
        fields = ['name', 'username', 'email', 'password',
                  'address', 'birth_date', 'rg',
                  'cpf', 'bank', 'agency',
                  'account_number']

class VendedorDAO(models.Model):
    def vendedor_create(request, template_name):
        form = VendedorForm(request.POST or None)
        return form

####################################################################################
### Comprador ######################################################################
####################################################################################

class Comprador(models.Model):
    name = models.CharField(max_length=256)
    username = models.CharField(max_length=16, default='', unique=True)
    email = models.CharField(max_length=256, default='', unique=True)
    password = models.CharField(max_length=16, default='')
    address = models.CharField(max_length=256)
    birth_date = models.DateField(default=date.today)
    rg = models.CharField(max_length=9, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    card_number = models.CharField(max_length=16, default='')
    
class CompradorForm(ModelForm):
    class Meta:
        model = Comprador
        fields = ['name', 'username', 'email', 'password',
                  'address', 'birth_date', 'rg',
                  'cpf', 'card_number']

class CompradorDAO(models.Model):
    def comprador_create(request, template_name):
        form = CompradorForm(request.POST or None)
        return form


####################################################################################
### Leiloeiro ######################################################################
####################################################################################
        
class Leiloeiro(models.Model):
    name = models.CharField(max_length=256)
    username = models.CharField(max_length=16, default='', unique=True)
    email = models.CharField(max_length=256, default='', unique=True)
    password = models.CharField(max_length=16, default='')
    address = models.CharField(max_length=256)
    birth_date = models.DateField(default=date.today)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    bank = models.CharField(max_length=64, choices=BANK_CHOICES, default='')
    agency = models.IntegerField(default=1)
    account_number = models.CharField(max_length=64)
    salary = models.DecimalField(default=10, decimal_places=2, max_digits=8)
    
class LeiloeiroForm(ModelForm):
    class Meta:
        model = Leiloeiro
        fields = ['name', 'username','password',
                  'email','address', 'birth_date',
                  'rg', 'cpf', 'bank', 'agency',
                  'account_number', 'salary']

class LeiloeiroDAO(models.Model):
    def leiloeiro_create(request, template_name):
        form = LeiloeiroForm(request.POST or None)
        return form