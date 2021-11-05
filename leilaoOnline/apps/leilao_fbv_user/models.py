from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.conf import UserSettingsHolder, settings
from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

# import para fazer a comparacao com as tabelas fora de fbv_user (onde estao os cadastros)
from leilao_fbv.models import Vendedor as Vendedor_fbv
from leilao_fbv.models import Comprador as Comprador_fbv
from leilao_fbv.models import Leiloeiro as Leiloeiro_fbv

CATEGORY_CHOICES = (
    ('Automotivos e Peças','Automotivos e Peças'),
    ('Beleza e Cuidados Pessoais', 'Beleza e Cuidados Pessoais'),
    ('Esporte','Esporte'),
    ('Brinquedos e Jogos','Brinquedos e Jogos'),
    ('Cozinha','Cozinha'),
    ('Eletrônicos', 'Eletrônicos'),
    ('Games e Consoles', 'Games e Console'),
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

MONTH_CHOICES = (
    ('Janeiro', 'Janeiro'),
    ('Fevereiro', 'Fevereiro'),
    ('Março', 'Março'),
    ('Abril', 'Abril'),
    ('Maio', 'Maio'),
    ('Junho', 'Junho'),
    ('Julho', 'Julho'),
    ('Agosto', 'Agosto'),
    ('Setembro', 'Setembro'),
    ('Outubro', 'Outubro'),
    ('Novembro', 'Novembro'),
    ('Dezembro', 'Dezembro'),
)
DAY_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27'),
    ('28', '28'),
    ('29', '29'),
    ('30', '30'),
    ('31', '31'),
)

YEAR_CHOICES = (
    ('2021', '2021'),
    ('2022', '2022'),
)

####################################################################################
### Lote ###########################################################################
####################################################################################

class Lote(models.Model):
    
    name = models.CharField(max_length=200, default='')
    summary = models.CharField(max_length=512, default='')
    qty = models.IntegerField(default=1)
    category = models.CharField(max_length=64, choices=CATEGORY_CHOICES, default='')
    condition = models.CharField(max_length=64, choices=CONDITION_CHOICES, default='')
    min_value = models.DecimalField(default=10.00, decimal_places=2, max_digits=16)
    opening_month = models.CharField(max_length=16, choices=MONTH_CHOICES, default='')
    opening_day = models.CharField(max_length=2, choices=DAY_CHOICES, default=1)
    opening_year = models.CharField(max_length=4, choices=YEAR_CHOICES, default=2021)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True)
    
    def __str__(self):
        return self.name

    def set_user(self, user):
        self.user = user

    def get_absolute_url(self):
        return reverse('leilao_fbv_user:lote_edit', kwargs={'pk': self.pk})

class LoteForm(ModelForm):
    class Meta:
        model = Lote
        fields = ['name', 'summary', 'qty',
                  'category', 'condition', 'min_value',
                  'opening_month', 'opening_day', 'opening_year']

class LoteDAO(models.Model):
    
    def lote_list(request, template_name):
        if request.user.is_superuser:
            lote = Lote.objects.all()
        else:
            lote = Lote.objects.filter(user=request.user)
        data = {}
        data['object_list'] = lote
        return data

    def available_list(request, template_name):
        lote = Lote.objects.all()
        data = {}
        data['object_list'] = lote
        return data

    def lote_create(request, template_name):
        lote = Lote().set_user(request.user)
        form = LoteForm(request.POST or None)
        return form

    def lote_update(request, pk, template_name):
        if request.user.is_superuser:
            lote= get_object_or_404(Lote, pk=pk)
        else:
            lote= get_object_or_404(Lote, pk=pk, user=request.user)
        form = LoteForm(request.POST or None, instance=lote)
        return form

    def lote_delete(request, pk, template_name):
        if request.user.is_superuser:
            lote= get_object_or_404(Lote, pk=pk)
        else:
            lote= get_object_or_404(Lote, pk=pk, user=request.user)
        return lote

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
    def leiloeiro_list(request, template_name):
        lote = Leiloeiro.objects.all()
        data = {}
        data['object_list'] = lote
        return data
    
    def leiloeiro_create(request, template_name):
        form = LeiloeiroForm(request.POST or None)
        return form
    
    def leiloeiro_update(request, pk, template_name):
        leiloeiro = get_object_or_404(Leiloeiro, pk=pk)
        form = LoteForm(request.POST or None, instance=leiloeiro)
        return form

    def leiloeiro_delete(request, pk, template_name):
        leiloeiro = get_object_or_404(Leiloeiro, pk=pk)
        return leiloeiro

    def leiloeiro_filter(request, username):
        bool_user = Leiloeiro_fbv.objects.filter(username = username).exists()
        print("Entrou Username Leiloeiro filter", username, bool_user)
        return bool_user

####################################################################################
### Vendedor #######################################################################
####################################################################################

class Vendedor(models.Model):
    name = models.CharField(max_length=256)
    username = models.CharField(max_length=16, default='')
    email = models.CharField(max_length=256, default='')
    password = models.CharField(max_length=16, default='')
    address = models.CharField(max_length=256)
    birth_date = models.DateField(default=date.today)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    bank = models.CharField(max_length=64, choices=BANK_CHOICES, default='')
    agency = models.IntegerField(default=1)
    account_number = models.CharField(max_length=64)
    
class VendedorForm(ModelForm):
    class Meta:
        model = Vendedor
        fields = ['name', 'username', 'email', 'password',
                  'address', 'birth_date', 'rg',
                  'cpf', 'bank', 'agency',
                  'account_number']

class VendedorDAO(models.Model):

    def vendedor_list(request, template_name):
        vendedor = Vendedor.objects.all()
        data = {}
        data['object_list'] = vendedor
        return data

    def vendedor_create(request, template_name):
        form = VendedorForm(request.POST or None)
        return form
    
    def vendedor_update(request, pk, template_name):
        vendedor = get_object_or_404(Vendedor, pk=pk)
        form = LoteForm(request.POST or None, instance=vendedor)
        return form

    def vendedor_delete(request, pk, template_name):
        vendedor = get_object_or_404(Vendedor, pk=pk)
        return vendedor
    
    def vendedor_filter(request, username):
        bool_user = Vendedor_fbv.objects.filter(username = username).exists()
        print("Entrou Username vendedor filter", username, bool_user)
        return bool_user

####################################################################################
### Comprador ######################################################################
####################################################################################

class Comprador(models.Model):
    name = models.CharField(max_length=256)
    username = models.CharField(max_length=16, default='')
    email = models.CharField(max_length=256, default='')
    password = models.CharField(max_length=16, default='')
    address = models.CharField(max_length=256)
    birth_date = models.DateField(default=date.today)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    card_number = models.CharField(max_length=16, default='')
    
class CompradorForm(ModelForm):
    class Meta:
        model = Comprador
        fields = ['name', 'username', 'email', 'password',
                  'address', 'birth_date', 'rg',
                  'cpf', 'card_number']

class CompradorDAO(models.Model):

    def comprador_list(request, template_name):
        comprador = Comprador.objects.all()
        data = {}
        data['object_list'] = comprador
        return data

    def comprador_create(request, template_name):
        form = CompradorForm(request.POST or None)
        return form
    
    def comprador_update(request, pk, template_name):
        comprador = get_object_or_404(Comprador, pk=pk)
        form = LoteForm(request.POST or None, instance=comprador)
        return form

    def comprador_delete(request, pk, template_name):
        comprador = get_object_or_404(Comprador, pk=pk)
        return comprador

    def comprador_filter(request, username):
        bool_user = Comprador_fbv.objects.filter(username = username).exists()
        print("Entrou Username comprador filter", username, bool_user)
        return bool_user

####################################################################################
### WIP: Relatorio #################################################################
####################################################################################

# class Relatorio(models.Model):
#     leilao = models.IntegerField(default=1)
#     lote = models.CharField(max_length=256)
#     vendas = models.CharField(max_length=256)
#     receita = models.CharField(max_length=256)
#     custos = models.CharField(max_length=256)
#     lucro = models.CharField(max_length=256)
#     periodo = models.DateField(default=date.today)
#     vendedor = models.CharField(max_length=256)
#     comprador = models.CharField(max_length=256)
#     lances = models.CharField(max_length=256)
#     vencedor = models.CharField(max_length=256)