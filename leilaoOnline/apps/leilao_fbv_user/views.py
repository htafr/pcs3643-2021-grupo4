from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Lote, LoteDAO, Vendedor, VendedorDAO, Comprador, CompradorDAO

@login_required
def list_lote(request, template_name='leilao_fbv_user/lote_list.html'):
    data = LoteDAO.lote_list(request=request, template_name=template_name)
    return render(request, template_name, data)

@login_required
def list_available(request, template_name='leilao_fbv_user/available_lote.html'):
    data = LoteDAO.available_list(request=request, template_name=template_name)
    return render(request, template_name, data)
    
@login_required
def create_lote(request, template_name='leilao_fbv_user/lote_form.html'):
    form = LoteDAO.lote_create(request=request, template_name=template_name)
    if form.is_valid():
        form.instance.user = request.user
        lote = form.save(commit=False)
        lote.save()
        return redirect('leilao_fbv_user:lote_list')
    return render(request, template_name, {'form':form})
    
@login_required
def update_lote(request, pk, template_name='leilao_fbv_user/lote_form.html'):
    form = LoteDAO.lote_update(request=request, pk=pk, template_name=template_name)
    if form.is_valid():
        form.save()
        return redirect('leilao_fbv_user:lote_list')
    return render(request, template_name, {'form':form})
    
@login_required
def delete_lote(request, pk, template_name='leilao_fbv_user/lote_confirm_delete.html'):
    lote = LoteDAO.lote_delete(request=request, pk=pk, template_name=template_name)
    if request.method=='POST':
        lote.delete()
        return redirect('leilao_fbv_user:lote_list')
    return render(request, template_name, {'object':lote})
    
####################################################################################
### Vendedor #######################################################################
####################################################################################
@login_required
def redirect_vendedor(request, template_name='leilao_fbv_user/vendedor_page.html'):
    return render(request, 'leilao_fbv_user/vendedor_page.html')

def list_vendedor(request, template_name='leilao_fbv/vendedor_list.html'):
    data = VendedorDAO.vendedor_list(request, template_name=template_name)
    return render(request, template_name, data)

def create_vendedor(request, template_name='leilao_fbv/vendedor_form.html'):
    form = VendedorDAO.vendedor_create(request, template_name=template_name)
    if form.is_valid():
        form.save()
        user = User.objects.create_user(form.data['username'], form.data['email'], form.data['password'])
        return redirect('leilao_fbv:lote_list')
    return render(request, template_name, {'form':form})

def update_vendedor(request, pk, template_name='leilao_fbv/vendedor_form.html'):
    form = VendedorDAO.vendedor_update(request, pk=pk, template_name=template_name)
    if form.is_valid():
        form.save()
        return redirect('leilao_fbv:vendedor_list')
    return render(request, template_name, {'form':form})

def delete_vendedor(request, pk, template_name='leilao_fbv/vendedor_confirm_delete.html'):
    vendedor = VendedorDAO.vendedor_delete(request, pk=pk, template_name=template_name)
    if request.method=='POST':
        vendedor.delete()
        return redirect('leilao_fbv:vendedor_list')
    return render(request, template_name, {'object':vendedor})
    
####################################################################################
### Comprador ######################################################################
####################################################################################
@login_required
def redirect_comprador(request, template_name='leilao_fbv_user/comprador_page.html'):
    return render(request, 'leilao_fbv_user/comprador_page.html')

# def list_comprador(request, template_name='leilao_fbv/comprador_list.html'):
#     data = CompradorDAO.vendedor_list(request, template_name=template_name)
#     return render(request, template_name, data)

def create_comprador(request, template_name='leilao_fbv/comprador_form.html'):
    form = CompradorDAO.vendedor_create(request, template_name=template_name)
    if form.is_valid():
        form.save()
        user = User.objects.create_user(form.data['username'], form.data['email'], form.data['password'])
        return redirect('leilao_fbv:lote_list')
    return render(request, template_name, {'form':form})

# def update_comprador(request, pk, template_name='leilao_fbv/comprador_form.html'):
#     form = CompradorDAO.vendedor_update(request, pk=pk, template_name=template_name)
#     if form.is_valid():
#         form.save()
#         return redirect('leilao_fbv:comprador_list')
#     return render(request, template_name, {'form':form})

# def delete_comprador(request, pk, template_name='leilao_fbv/comprador_confirm_delete.html'):
#     comprador = CompradorDAO.vendedor_delete(request, pk=pk, template_name=template_name)
#     if request.method=='POST':
#         comprador.delete()
#         return redirect('leilao_fbv:comprador_list')
#     return render(request, template_name, {'object':comprador})