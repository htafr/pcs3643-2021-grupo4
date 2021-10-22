from django.urls import include, path
from django.contrib import admin

import theme.views

urlpatterns = [
    path('', theme.views.home),
    path('leilao_fbv/', include('leilao_fbv.urls')),
    path('leilao_fbv_user/', include('leilao_fbv_user.urls')),

    # Enable built-in authentication views
    path('accounts/', include('django.contrib.auth.urls')),    
    # Enable built-in admin interface
    path('admin/', admin.site.urls),
]
