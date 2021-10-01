from django.urls import path

from leilao_fbv import views

app_name = 'leilao_fbv'

urlpatterns = [
	path('', views.lote_list, name='lote_list'),
	path('new/', views.lote_create, name='lote_new'),
	path('edit/<int:pk>/', views.lote_update, name='lote_edit'),
	path('delete/<int:pk>/', views.lote_delete, name='lote_delete'),
]