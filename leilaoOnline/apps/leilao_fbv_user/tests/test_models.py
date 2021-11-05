from django.test import TestCase, Client
from django.contrib.auth.models import User
from leilao_fbv_user.models import Lote
from datetime import date

# Create your tests here.

class LoteModelTest(TestCase):
	@classmethod
	def setUpTestData(self):
		"""Test form is invalid if renewal_date is before today."""
		user = User.objects.create(username="testuser")
		user.set_password('pcs-3643')
		user.save()
		client = Client()
		client.login(username='testuser', password='pcs-3643')
		Lote.objects.create(name='Livros', summary='Um lote de livros', qty='1',
							category='Livro', condition='Novo', min_value='10.00',
							opening_month='Novembro', opening_day='28', opening_year='2021', user=user)

	def test_lote_name(self):
		lote = Lote.objects.get(id=1)
		field_label = lote._meta.get_field('name').verbose_name
		self.assertEquals(field_label, 'name')

	def test_lote_summary(self):
		lote = Lote.objects.get(id=1)
		field_label = lote._meta.get_field('summary').verbose_name
		self.assertEquals(field_label, 'summary')

	def test_lote_qty(self):
		lote = Lote.objects.get(id=1)
		field_label = lote._meta.get_field('qty').verbose_name
		self.assertEquals(field_label, 'qty')

	def test_lote_category(self):
		lote = Lote.objects.get(id=1)
		field_label = lote._meta.get_field('category').verbose_name
		self.assertEquals(field_label, 'category')

	def test_lote_condition(self):
		lote = Lote.objects.get(id=1)
		field_label = lote._meta.get_field('condition').verbose_name
		self.assertEquals(field_label, 'condition')
	
	def test_lote_min_value(self):
		lote = Lote.objects.get(id=1)
		field_label = lote._meta.get_field('min_value').verbose_name
		self.assertEquals(field_label, 'min value')

	def test_lote_opening_date(self):
		lote = Lote.objects.get(id=1)
		field_label = lote._meta.get_field('opening_month').verbose_name
		self.assertEquals(field_label, 'opening month')

	def test_lote_opening_date(self):
		lote = Lote.objects.get(id=1)
		field_label = lote._meta.get_field('opening_day').verbose_name
		self.assertEquals(field_label, 'opening day')

	def test_lote_opening_date(self):
		lote = Lote.objects.get(id=1)
		field_label = lote._meta.get_field('opening_year').verbose_name
		self.assertEquals(field_label, 'opening year')
