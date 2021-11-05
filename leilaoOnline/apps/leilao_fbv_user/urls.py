from django.urls import path

from . import views

app_name = 'leilao_fbv_user'

urlpatterns = [

	##############################################################################
	### Lote #####################################################################
	##############################################################################

	# path('', views.lote_list, name='lote_list'),
	# path('new/', views.lote_create, name='lote_new'),
	# path('edit/<int:pk>/', views.lote_update, name='lote_edit'),
	# path('delete/<int:pk>/', views.lote_delete, name='lote_delete'),

	path('user_lotes/', views.list_lote, name='lote_list'),
	path('alllotes/', views.list_available, name='available_lote'),
	path('new/', views.create_lote, name='lote_new'),
	path('edit/<int:pk>/', views.update_lote, name='lote_edit'),
	path('delete/<int:pk>/', views.delete_lote, name='lote_delete'),

	##############################################################################
	### Login Usuario #############################################################
	##############################################################################
	path('user_page/', views.redirect_user, name='redirect_user'),

	##############################################################################
	### Vendedor #################################################################
	##############################################################################

	path('', views.list_vendedor, name='vendedor_list'),
	path('new/', views.create_vendedor, name='vendedor_new'),
	
	##path('vendedor_page/', views.redirect_user, name='redirect_user'),
	# path('edit/<int:pk>/', views.update_vendedor, name='vendedor_edit'),
	# path('delete/<int:pk>/', views.delete_vendedor, name='vendedor_delete'),

	##############################################################################
	### Comprador ################################################################
	##############################################################################

	# path('', views.list_comprador, name='comprador_list'),
	# path('new/', views.create_comprador, name='comprador_new'),
	path('user_page/', views.redirect_comprador, name='redirect_user'),
	# path('edit/<int:pk>/', views.update_comprador, name='comprador_edit'),
	##path('comprador_page/', views.redirect_comprador, name='redirect_user')
	# path('delete/<int:pk>/', views.delete_comprador, name='comprador_delete'),
]