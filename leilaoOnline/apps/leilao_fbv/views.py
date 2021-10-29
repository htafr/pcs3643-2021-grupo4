from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Vendedor, VendedorDAO, Comprador, CompradorDAO

# ####################################################################################
# ### Lote ###########################################################################
# ####################################################################################

def list_lote(request, template_name='leilao_fbv/lote_list.html'):
    pass
#     data = LoteDAO.lote_list(request, template_name=template_name)
#     return render(request, template_name, data)

# def create_lote(request, template_name='leilao_fbv/lote_form.html'):
#     form = LoteDAO.lote_create(request, template_name=template_name)
#     if form.is_valid():
#         form.save()
#         return redirect('leilao_fbv:lote_list')
#     return render(request, template_name, {'form':form})

# def update_lote(request, pk, template_name='leilao_fbv/lote_form.html'):
#     form = LoteDAO.lote_update(request, pk=pk, template_name=template_name)
#     if form.is_valid():
#         form.save()
#         return redirect('leilao_fbv:lote_list')
#     return render(request, template_name, {'form':form})

# def delete_lote(request, pk, template_name='leilao_fbv/lote_confirm_delete.html'):
#     lote = LoteDAO.lote_delete(request, pk=pk, template_name=template_name)
#     if request.method=='POST':
#         lote.delete()
#         return redirect('leilao_fbv:lote_list')
#     return render(request, template_name, {'object':lote})


####################################################################################
### Perfil #########################################################################
####################################################################################

def select_perfil(request, template_name='leilao_fbv/perfil_form.html'):
    return render(request, template_name)

####################################################################################
### Comprador  #####################################################################
####################################################################################

def create_comprador(request, template_name='leilao_fbv/comprador_form.html'):
    form = CompradorDAO.comprador_create(request, template_name=template_name)
    if form.is_valid():
        form.save()
        user = User.objects.create_user(form.data['username'], form.data['email'], form.data['password'])
        user.save()
        return redirect('/')
    return render(request, template_name, {'form':form})

def redirect_comprador(request, template_name='leilao_fbv_user/comprador_page.html'):
    pass

####################################################################################
### Vendedor #######################################################################
####################################################################################

# def list_vendedor(request, template_name='leilao_fbv/vendedor_list.html'):
#     data = VendedorDAO.vendedor_list(request, template_name=template_name)
#     return render(request, template_name, data)

def create_vendedor(request, template_name='leilao_fbv/vendedor_form.html'):
    form = VendedorDAO.vendedor_create(request, template_name=template_name)
    if form.is_valid():
        form.save()
        user = User.objects.create_user(form.data['username'], form.data['email'], form.data['password'])
        user.save()
        return redirect('/')
    return render(request, template_name, {'form':form})

def redirect_vendedor(request, template_name='leilao_fbv_user/vendedor_page.html'):
    pass

# def update_vendedor(request, pk, template_name='leilao_fbv/vendedor_form.html'):
#     form = VendedorDAO.vendedor_update(request, pk=pk, template_name=template_name)
#     if form.is_valid():
#         form.save()
#         return redirect('leilao_fbv:vendedor_list')
#     return render(request, template_name, {'form':form})

# def delete_vendedor(request, pk, template_name='leilao_fbv/vendedor_confirm_delete.html'):
#     vendedor = VendedorDAO.vendedor_delete(request, pk=pk, template_name=template_name)
#     if request.method=='POST':
#         vendedor.delete()
#         return redirect('leilao_fbv:vendedor_list')
#     return render(request, template_name, {'object':vendedor})