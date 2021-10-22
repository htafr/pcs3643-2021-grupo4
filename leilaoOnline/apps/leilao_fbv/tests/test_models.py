from django.test import TestCase
from leilao_fbv.models import Vendedor

# Create your tests here.

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