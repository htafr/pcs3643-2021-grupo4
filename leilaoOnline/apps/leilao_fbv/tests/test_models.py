from django.test import TestCase
from leilao_fbv.models import Vendedor, Comprador, Leiloeiro

# Create your tests here.

##############################################################################
# Teste Vendedor #############################################################
##############################################################################

class VendedorModelTest(TestCase):
	@classmethod
	def setUpTestData(self):
		"""Test form is invalid if renewal_date is before today."""
		Vendedor.objects.create(name='Otaviu', username='Offreitas', email='offreitas@usp.br',
							password='pcs-3643', address='Av. Luciano Gualberto, 205', birth_date='2000-05-02',
							rg='569882154', cpf='62659431622', bank='Nubank',
							agency='123456951',account_number='1451562315')
	
	def test_vendedor_name(self):
		vendedor = Vendedor.objects.get(id=1)
		field_label = vendedor._meta.get_field('name').verbose_name
		self.assertEquals(field_label, 'name')

	def test_vendedor_username(self):
		vendedor = Vendedor.objects.get(id=1)
		field_label = vendedor._meta.get_field('username').verbose_name
		self.assertEquals(field_label, 'username')

	def test_vendedor_email(self):
		vendedor = Vendedor.objects.get(id=1)
		field_label = vendedor._meta.get_field('email').verbose_name
		self.assertEquals(field_label, 'email')

	def test_vendedor_password(self):
		vendedor = Vendedor.objects.get(id=1)
		field_label = vendedor._meta.get_field('password').verbose_name
		self.assertEquals(field_label, 'password')

	def test_vendedor_address(self):
		vendedor = Vendedor.objects.get(id=1)
		field_label = vendedor._meta.get_field('address').verbose_name
		self.assertEquals(field_label, 'address')

	def test_vendedor_birth_date(self):
		vendedor = Vendedor.objects.get(id=1)
		field_label = vendedor._meta.get_field('birth_date').verbose_name
		self.assertEquals(field_label, 'birth date')

	def test_vendedor_rg(self):
		vendedor = Vendedor.objects.get(id=1)
		field_label = vendedor._meta.get_field('rg').verbose_name
		self.assertEquals(field_label, 'rg')

	def test_vendedor_cpf(self):
		vendedor = Vendedor.objects.get(id=1)
		field_label = vendedor._meta.get_field('cpf').verbose_name
		self.assertEquals(field_label, 'cpf')

	def test_vendedor_bank(self):
		vendedor = Vendedor.objects.get(id=1)
		field_label = vendedor._meta.get_field('bank').verbose_name
		self.assertEquals(field_label, 'bank')

	def test_vendedor_agency(self):
		vendedor = Vendedor.objects.get(id=1)
		field_label = vendedor._meta.get_field('agency').verbose_name
		self.assertEquals(field_label, 'agency')

	def test_vendedor_account_number(self):
		vendedor = Vendedor.objects.get(id=1)
		field_label = vendedor._meta.get_field('account_number').verbose_name
		self.assertEquals(field_label, 'account number')


##############################################################################
# Teste Comprador ############################################################
##############################################################################

class CompradorModelTest(TestCase):
	@classmethod
	def setUpTestData(self):
		"""Test form is invalid if renewal_date is before today."""
		Comprador.objects.create(name='comprador', username='comprante', email='compra@compra.br',
							password='pcs-3643', address='Av. da Comprante, 161', birth_date='2000-05-02',
							rg='999999999', cpf='44444444444', card_number='123456789')
	
	def test_comprador_name(self):
		comprador = Comprador.objects.get(id=1)
		field_label = comprador._meta.get_field('name').verbose_name
		self.assertEquals(field_label, 'name')

	def test_comprador_username(self):
		comprador = Comprador.objects.get(id=1)
		field_label = comprador._meta.get_field('username').verbose_name
		self.assertEquals(field_label, 'username')

	def test_comprador_email(self):
		comprador = Comprador.objects.get(id=1)
		field_label = comprador._meta.get_field('email').verbose_name
		self.assertEquals(field_label, 'email')

	def test_comprador_password(self):
		comprador = Comprador.objects.get(id=1)
		field_label = comprador._meta.get_field('password').verbose_name
		self.assertEquals(field_label, 'password')

	def test_comprador_address(self):
		comprador = Comprador.objects.get(id=1)
		field_label = comprador._meta.get_field('address').verbose_name
		self.assertEquals(field_label, 'address')

	def test_comprador_birth_date(self):
		comprador = Comprador.objects.get(id=1)
		field_label = comprador._meta.get_field('birth_date').verbose_name
		self.assertEquals(field_label, 'birth date')

	def test_comprador_rg(self):
		comprador = Comprador.objects.get(id=1)
		field_label = comprador._meta.get_field('rg').verbose_name
		self.assertEquals(field_label, 'rg')

	def test_comprador_cpf(self):
		comprador = Comprador.objects.get(id=1)
		field_label = comprador._meta.get_field('cpf').verbose_name
		self.assertEquals(field_label, 'cpf')

	def test_comprador_card_number(self):
		comprador = Comprador.objects.get(id=1)
		field_label = comprador._meta.get_field('card_number').verbose_name
		self.assertEquals(field_label, 'card number')

##############################################################################
# Teste Leiloeiro ############################################################
##############################################################################

class LeiloeiroModelTest(TestCase):
	@classmethod
	def setUpTestData(self):
		"""Test form is invalid if renewal_date is before today."""
		Leiloeiro.objects.create(name='leiloeiro', username='leilante', email='leiloeiro@leilao.br',
							password='pcs-3643', address='Av. do leilao, 161', birth_date='2000-05-02',
							rg='989898989', cpf='40404040404', bank='Nubank',
							agency='133456951',account_number='1411562315',salary='2500')
	
	def test_leiloeiro_name(self):
		leiloeiro = Leiloeiro.objects.get(id=1)
		field_label = leiloeiro._meta.get_field('name').verbose_name
		self.assertEquals(field_label, 'name')

	def test_leiloeiro_username(self):
		leiloeiro = Leiloeiro.objects.get(id=1)
		field_label = leiloeiro._meta.get_field('username').verbose_name
		self.assertEquals(field_label, 'username')

	def test_leiloeiro_password(self):
		leiloeiro = Leiloeiro.objects.get(id=1)
		field_label = leiloeiro._meta.get_field('password').verbose_name
		self.assertEquals(field_label, 'password')

	def test_leiloeiro_email(self):
		leiloeiro = Leiloeiro.objects.get(id=1)
		field_label = leiloeiro._meta.get_field('email').verbose_name
		self.assertEquals(field_label, 'email')

	def test_leiloeiro_address(self):
		leiloeiro = Leiloeiro.objects.get(id=1)
		field_label = leiloeiro._meta.get_field('address').verbose_name
		self.assertEquals(field_label, 'address')

	def test_leiloeiro_birth_date(self):
		leiloeiro = Leiloeiro.objects.get(id=1)
		field_label = leiloeiro._meta.get_field('birth_date').verbose_name
		self.assertEquals(field_label, 'birth date')

	def test_leiloeiro_rg(self):
		leiloeiro = Leiloeiro.objects.get(id=1)
		field_label = leiloeiro._meta.get_field('rg').verbose_name
		self.assertEquals(field_label, 'rg')

	def test_leiloeiro_cpf(self):
		leiloeiro = Leiloeiro.objects.get(id=1)
		field_label = leiloeiro._meta.get_field('cpf').verbose_name
		self.assertEquals(field_label, 'cpf')

	def test_leiloeiro_bank(self):
		leiloeiro = Leiloeiro.objects.get(id=1)
		field_label = leiloeiro._meta.get_field('bank').verbose_name
		self.assertEquals(field_label, 'bank')

	def test_leiloeiro_agency(self):
		leiloeiro = Leiloeiro.objects.get(id=1)
		field_label = leiloeiro._meta.get_field('agency').verbose_name
		self.assertEquals(field_label, 'agency')

	def test_leiloeiro_account_number(self):
		leiloeiro = Leiloeiro.objects.get(id=1)
		field_label = leiloeiro._meta.get_field('account_number').verbose_name
		self.assertEquals(field_label, 'account number')

	def test_leiloeiro_salary(self):
		leiloeiro = Leiloeiro.objects.get(id=1)
		field_label = leiloeiro._meta.get_field('salary').verbose_name
		self.assertEquals(field_label, 'salary')