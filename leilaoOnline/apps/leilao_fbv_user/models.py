from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.urls import reverse
from django.conf import UserSettingsHolder, settings
from datetime import date, datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

####################################################################################
### Choices ########################################################################
####################################################################################
CATEGORY_CHOICES = (
    ('Administração, Negócios e Economia','Administração, Negócios e Economia'),
    ('Arte, Cinema e Fotografia', 'Arte, Cinema e Fotografia'),
    ('Artesanato, Casa e Estilo de Vida','Artesanato, Casa e Estilo de Vida'),
    ('Autoajuda','Autoajuda'),
    ('Biografias e Histórias Reais','Biografias e Histórias Reais'),
    ('Calendários e Anuários', 'Calendários e Anuários'),
    ('Ciências', 'Ciências'),
    ('Livro','Livro'),
    ('Computação, Informática e Mídias Digitais', 'Computação, Informática e Mídias Digitais'),
    ('Cristandade','Cristandade'),
    ('Crônicas, Humor e Entretenimento', 'Crônicas, Humor e Entretenimento'),
    ('Direito', 'Direito'),
    ('Educação', 'Educação'),
    ('Educação dos Filhos e Família', 'Educação dos Filhos e Família'),
    ('Educação, Referência e Didáticos', 'Educação, Referência e Didáticos'),
    ('Engenharia e Transporte', 'Engenharia e Transporte'),
    ('Esportes e Lazer', 'Esportes e Lazer'),
    ('Fantasia, Horror, e Ficção Científica', 'Fantasia, Horror, e Ficção Científica'),
    ('Gastronomia e Culinária', 'Gastronomia e Culinária'),
    ('História', 'História'),
    ('HQs, Mangás e Graphic Novels', 'HQs, Mangás e Graphic Novels'),
    ('Infantil', 'Infantil'),
    ('Jovens e Adolescentes', 'Jovens e Adolescentes'),
    ('LGBT', 'LGBT'),
    ('Literatura e Ficção', 'Literatura e Ficção'),
    ('Medicina', 'Medicina'),
    ('Policial, Suspense e Mistério', 'Policial, Suspense e Mistério'),
    ('Política, Filosofia e Ciências Sociais', 'Política, Filosofia e Ciências Sociais'),
    ('Preparação para Provas', 'Preparação para Provas'),
    ('Religião e Espiritualidade', 'Religião e Espiritualidade'),
    ('Romance', 'Romance'),
    ('Saúde e Família', 'Saúde e Família'),
    ('Turismo e Guias de Viagem', 'Turismo e Guias de Viagem'),
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
    ('Mês', 'Mês'),
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
    ('Dia', 'Dia'),
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
    ('Ano', 'Ano'),
    ('2021', '2021'),
    ('2022', '2022'),
    ('2023', '2023'),
    ('2024', '2024'),
    ('2025', '2025'),
    ('2026', '2026'),
    ('2027', '2027'),
)

LEILAO_CHOICES = (
    ("ATIVO", "Ativo"),
    ("FINALIZADO","Finalizado"),
    ("ESPERA", "Espera")
)

LOTE_CHOICES = (
    ('Pendente', 'Pendente'),
    ('Negado', 'Negado'),
    ('Aprovado', 'Aprovado'),
)

####################################################################################
### Lote ###########################################################################
####################################################################################

class Lote(models.Model):
    ### Para o vendedor preencher
    name = models.CharField(max_length=64, default='', blank=False)
    summary = models.CharField(max_length=512, default='', blank=False)
    quantity = models.IntegerField(default=1, blank=False)
    category = models.CharField(max_length=64, choices=CATEGORY_CHOICES, default='', blank=False)
    author = models.CharField(max_length=64, default='', blank=False)
    publisher = models.CharField(max_length=64, default='', blank=False)
    edition = models.CharField(max_length=64, default='', blank=False)
    number_of_pages = models.CharField(max_length=64, default='', blank=False)
    condition = models.CharField(max_length=64, choices=CONDITION_CHOICES, default='', blank=False)
    reserve_price = models.DecimalField(default=10.00, decimal_places=2, max_digits=16, blank=False)

    ### Para o leiloeiro preencher
    start_price = models.DecimalField(default=10.00, decimal_places=2, max_digits=16)
    minimum_bid = models.DecimalField(default=10.00, decimal_places=2, max_digits=16)
    state = models.CharField(max_length=16, choices=LOTE_CHOICES, default='Pendente')

    ### Preenchido automaticamente
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def set_user(self, user):
        self.user = user

    def get_absolute_url(self):
        return reverse('leilao_fbv_user:lote_edit', kwargs={'pk': self.pk})

class LoteForm(ModelForm):
    class Meta:
        model = Lote
        fields = ['name', 'summary', 'quantity', 'category',
                  'author', 'publisher', 'edition', 'number_of_pages',
                  'condition', 'reserve_price']

class LotePendingForm(ModelForm):
    class Meta:
        model = Lote
        fields = ['start_price', 'minimum_bid', 'state']

class LoteDAO(models.Model):
    def lote_list(request, template_name):
        if request.user.is_staff:
            lote = Lote.objects.all()
        else:
            lote = Lote.objects.filter(user=request.user)
        data = {}
        data['object_list'] = lote
        return data

    def lote_list_pending(request, template_name):
        lote = Lote.objects.filter(state='Pendente')
        data = {}
        data['object_list'] = lote
        return data

    def available_list(request, template_name):
        lote = Lote.objects.filter(state='Aprovado')
        data = {}
        data['object_list'] = lote
        return data

    def lote_create(request, template_name):
        lote = Lote().set_user(request.user)
        form = LoteForm(request.POST or None)
        return form

    def lote_update(request, pk, template_name):
        if request.user.is_staff:
            lote= get_object_or_404(Lote, pk=pk)
        else:
            lote= get_object_or_404(Lote, pk=pk, user=request.user)
        form = LoteForm(request.POST or None, instance=lote)
        return form

    def lote_delete(request, pk, template_name):
        if request.user.is_staff:
            lote= get_object_or_404(Lote, pk=pk)
        else:
            lote= get_object_or_404(Lote, pk=pk, user=request.user)
        return lote

    def lote_pending(request, pk, template_name):
        lote = get_object_or_404(Lote, pk=pk)
        form = LotePendingForm(request.POST or None, instance=lote)
        return form, lote

####################################################################################
### Lance ##########################################################################
####################################################################################

class Lance(models.Model):
    valor = models.DecimalField(default=10.00, decimal_places=2, max_digits=16, blank=False)
    leilao_id = models.IntegerField(default=0, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Verificar isso depois
    def __str__(self):
        return '{0} - R${1}'.format(self.user.username, self.valor)
    
    def init(self, valor):
        self.valor = valor
        return self

class LanceForm(ModelForm):
    class Meta:
        model = Lance
        fields = ['valor']        

class LanceDAO(models.Model):
    def init_lance(valor):
        lance = Lance().init(valor)
        return lance

    def get_lance(user_id):
        lance = Lance.objects.filter(user_id=user_id)
        data = {}
        data = lance
        return data

####################################################################################
### Leilao #########################################################################
####################################################################################

class Leilao(models.Model):
    name = models.CharField(max_length=64, default='', blank=False)
    opening_date = models.DateField(auto_now=True)
    close_date = models.DateField(auto_now=True)
    status_leilao = models.CharField(max_length=16, choices=LEILAO_CHOICES, blank=False, null=False)

    ### Atributos Classes
    lote = models.OneToOneField(Lote, on_delete=models.CASCADE)
    lance = models.ForeignKey(Lance, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class LeilaoForm(ModelForm):
    class Meta:
        model = Leilao
        fields = ['name', 'status_leilao']

class LeilaoDAO(models.Model):
    def leilao_create(request, pk, template_name):
        ### Encontra o lote com pk
        lote = get_object_or_404(Lote, pk=pk)

        form = LeilaoForm(request.POST or None)
        return form, lote

    def leilao_list_all(request, template_name):
        leilao = Leilao.objects.all()
        data = {}
        data['object_list'] = leilao
        return data

    def leilao_list_avail(request, template_name):
        leilao = Leilao.objects.filter(status_leilao='Ativo')
        data = {}
        data['object_list'] = leilao
        return data

    def get_participating_leilao(request, user_id, template_name):
        lances = LanceDAO.get_lance(user_id=user_id)
        lances_list = list(lances)
        participating = []

        if lances_list:
            for lance in lances_list:
                try:
                    leilao = Leilao.objects.get(pk=lance.leilao_id)

                    if leilao not in participating:
                        participating.append(leilao)
                except:
                    leilao = None

        return participating

    def get_won_leilao(request, user_id, template_name):
        lances = LanceDAO.get_lance(user_id=user_id)
        lances_list = list(lances)

        finished_leiloes = Leilao.objects.filter(status_leilao='Finalizado')

        won = []

        if lances_list:
            for lance in lances_list:
                try:
                    leilao = finished_leiloes.get(pk=lance.leilao_id)
                    if leilao not in won:
                        won.append(leilao)
                except:
                    leilao = None

        return won
    
    def get_leilao(request, pk, template_name):
        leilao = get_object_or_404(Leilao, pk=pk)
        return leilao

    def leilao_delete(request, pk, template_name):
        if request.user.is_staff:
            leilao = get_object_or_404(Leilao, pk=pk)
        else:
            leilao = get_object_or_404(Leilao, pk=pk, user=request.user)
        return leilao

    def leilao_update(request, pk, template_name):
        if request.user.is_staff:
            leilao = get_object_or_404(Leilao, pk=pk)
        else:
            leilao = get_object_or_404(Leilao, pk=pk, user=request.user)
        leilao.close_date = date.today()
        form = LeilaoForm(request.POST or None, instance=leilao)
        return form

    def make_bid(request, pk, template_name):
        leilao = get_object_or_404(Leilao, pk=pk)
        form = LanceForm(request.POST or None)
        return form, leilao

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


### No futuro o leiloeiro só podera ser cadastrado por membros da equipe

####################################################################################
### Leiloeiro ######################################################################
####################################################################################

# class Leiloeiro(models.Model):
#     name = models.CharField(max_length=256)
#     username = models.CharField(max_length=16, default='', unique=True)
#     email = models.CharField(max_length=256, default='', unique=True)
#     password = models.CharField(max_length=16, default='')
#     address = models.CharField(max_length=256)
#     birth_date = models.DateField(default=date.today)
#     rg = models.CharField(max_length=9)
#     cpf = models.CharField(max_length=11)
#     bank = models.CharField(max_length=64, choices=BANK_CHOICES, default='')
#     agency = models.IntegerField(default=1)
#     account_number = models.CharField(max_length=64)
#     salary = models.DecimalField(default=10, decimal_places=2, max_digits=8)
    
# class LeiloeiroForm(ModelForm):
#     class Meta:
#         model = Leiloeiro
#         fields = ['name', 'username','password',
#                   'email','address', 'birth_date',
#                   'rg', 'cpf', 'bank', 'agency',
#                   'account_number', 'salary']

# class LeiloeiroDAO(models.Model):
#     def leiloeiro_list(request, template_name):
#         lote = Leiloeiro.objects.all()
#         data = {}
#         data['object_list'] = lote
#         return data
    
#     def leiloeiro_create(request, template_name):
#         form = LeiloeiroForm(request.POST or None)
#         return form
    
#     def leiloeiro_update(request, pk, template_name):
#         leiloeiro = get_object_or_404(Leiloeiro, pk=pk)
#         form = LoteForm(request.POST or None, instance=leiloeiro)
#         return form

#     def leiloeiro_delete(request, pk, template_name):
#         leiloeiro = get_object_or_404(Leiloeiro, pk=pk)
#         return leiloeiro

#     def leiloeiro_filter(request, username):
#         bool_user = Leiloeiro_fbv.objects.filter(username = username).exists()
#         # print("Entrou Username Leiloeiro filter", username, bool_user)
#         return bool_user