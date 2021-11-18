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
	path('pending/', views.list_pending_lote, name='lote_pending_list'),
	path('analysis/<int:pk>/', views.update_pending_lote, name='lote_update_pending'),

	##############################################################################
	### Leilao ###################################################################
	##############################################################################

	path('list_leilao_avail/', views.list_leilao_avail, name='list_leilao_avail'),
	path('list_leilao_all/', views.list_leilao_all, name='list_leilao_all'),
	path('create_leilao/<int:pk>/', views.create_leilao, name='create_leilao'),
	path('leilao_update/<int:pk>/', views.update_leilao, name='update_leilao'),
	path('leilao_delete/<int:pk>/', views.delete_leilao, name='delete_leilao'),
	path('show_leilao/<int:pk>/', views.show_leilao, name='show_leilao'),
	path('make_bid/<int:pk>/', views.make_bid, name='make_bid'),

	##############################################################################
	### Login Usuario #############################################################
	##############################################################################
	path('user_page/', views.redirect_user, name='redirect_user'),

	##############################################################################
	### Vendedor #################################################################
	##############################################################################

	path('', views.list_vendedor, name='vendedor_list'),
	path('new/', views.create_vendedor, name='vendedor_new'),
	
	path('vendedor_page/', views.redirect_vendedor, name='vendedor_page'),
	# path('edit/<int:pk>/', views.update_vendedor, name='vendedor_edit'),
	# path('delete/<int:pk>/', views.delete_vendedor, name='vendedor_delete'),

	##############################################################################
	### Comprador ################################################################
	##############################################################################

	path('comprador_page/', views.redirect_comprador, name='comprador_page'),
	path('leiloes_participados/', views.show_participating_leilao, name='show_participating_leilao'),
	path('won_leiloes/', views.show_won_leilao, name='show_won_leilao'),
	# path('', views.list_comprador, name='comprador_list'),
	# path('new/', views.create_comprador, name='comprador_new'),
	#path('user_page/', views.redirect_comprador, name='redirect_user'),
	# path('edit/<int:pk>/', views.update_comprador, name='comprador_edit'),
	##path('comprador_page/', views.redirect_comprador, name='redirect_user')
	# path('delete/<int:pk>/', views.delete_comprador, name='comprador_delete'),

	##############################################################################
	### Leiloeiro ################################################################
	##############################################################################

	path('leiloeiro_page/', views.redirect_leiloeiro, name='leiloeiro_page'),
]