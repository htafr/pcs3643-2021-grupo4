from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from django.contrib.auth.models import User

from .models import Leilao, LeilaoDAO, Lote, LoteDAO, Vendedor, VendedorDAO, Comprador, CompradorDAO, LeiloeiroDAO
from .models import Lance

@login_required
def list_lote(request, template_name='leilao_fbv_user/lote_list.html'):
    data = LoteDAO.lote_list(request=request, template_name=template_name)
    return render(request, template_name, data)

@login_required
def list_available(request, template_name='leilao_fbv_user/available_lote.html'):
    data = LoteDAO.available_list(request=request, template_name=template_name)
    return render(request, template_name, data)

@login_required
def list_pending_lote(request, template_name='leilao_fbv_user/lote_pendente.html'):
    data = LoteDAO.lote_list_pending(request=request, template_name=template_name)
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
def update_pending_lote(request, pk, template_name='leilao_fbv_user/lote_analise.html'):
    form, lote = LoteDAO.lote_pending(request=request, pk=pk, template_name=template_name)
    if form.is_valid():
        form.save()
        return redirect('leilao_fbv_user:lote_pending_list')

    context = {
        'form': form,
        'lote': lote,
    }
    return render(request, template_name, context)
    
@login_required
def delete_lote(request, pk, template_name='leilao_fbv_user/lote_confirm_delete.html'):
    lote = LoteDAO.lote_delete(request=request, pk=pk, template_name=template_name)
    if request.method=='POST':
        lote.delete()
        return redirect('leilao_fbv_user:lote_list')
    return render(request, template_name, {'object':lote})

####################################################################################
### Leilao #########################################################################
####################################################################################

@login_required
def create_leilao(request, pk, template_name='leilao_fbv_user/leilao_form.html'):
    form, lote = LeilaoDAO.leilao_create(request=request, pk=pk, template_name=template_name)
    if form.is_valid():
        form.instance.user = request.user
        leilao = form.save(commit=False)
        leilao.lote_id = pk
        leilao.user_id = request.user.id
        leilao.save()
        return redirect('leilao_fbv_user:redirect_user')

    context = {
        'form': form,
        'lote': lote,
    }
    return render(request, template_name, context)

@login_required
def show_leilao(request, pk, template_name='leilao_fbv_user/show_leilao.html'):
    leilao = get_object_or_404(Leilao, pk=pk)
    lances = Lance.objects.all()
    data = {}
    data['leilao'] = leilao
    data['lista_de_lances'] = sorted(lances, key=lambda t: t.valor, reverse=True)
    return render(request, template_name, data)

@login_required
def start_leilao(request, pk, template_name='leilao_fbv_user/show_leilao.html'):
    leilao = get_object_or_404(Leilao, pk=pk)
    leilao.status_leilao = 'ATIVO'
    leilao.save()
    return redirect('leilao_fbv_user:show_leilao', pk=pk)

@login_required
def end_leilao(request, pk, template_name='leilao_fbv_user/show_leilao.html'):
    leilao = get_object_or_404(Leilao, pk=pk)
    leilao.status_leilao = 'FINALIZADO'
    leilao.save()
    return redirect('leilao_fbv_user:show_leilao', pk=pk)

@login_required
def list_leilao(request, template_name='leilao_fbv_user/leilao_list.html'):
    leiloes = Leilao.objects.all()
    leiloes_espera = Leilao.objects.filter(status_leilao='ESPERA')
    leiloes_ativos = Leilao.objects.filter(status_leilao='ATIVO')
    leiloes_finalizados = Leilao.objects.filter(status_leilao='FINALIZADO')
    lances = Lance.objects.all()

    data = {}
    data['lista_leiloes_espera'] = leiloes_espera
    data['lista_leiloes_ativos'] = leiloes_ativos
    data['lista_leiloes_finalizados'] = leiloes_finalizados
    data['lista_lances'] = sorted(lances, key=lambda t: t.valor, reverse=True)

    return render(request, template_name, data)

@login_required
def update_leilao(request, pk, template_name='leilao_fbv_user/leilao_form.html'):
    form = LeilaoDAO.leilao_update(request=request, pk=pk, template_name=template_name)
    if form.is_valid():
        form.save()
        return redirect('leilao_fbv_user:leilao_list')
    return render(request, template_name, {'form':form})

@login_required
def delete_leilao(request, pk, template_name='leilao_fbv_user/leilao_confirm_delete.html'):
    leilao = LeilaoDAO.leilao_delete(request=request, pk=pk, template_name=template_name)
    if request.method=='POST':
        leilao.delete()
        return redirect('leilao_fbv_user:leilao_list')
    return render(request, template_name, {'object':leilao})

####################################################################################
### Lance ##########################################################################
####################################################################################

### Por que LanceForm?

# def realiza_lance(request, id_leilao, template_name='leilao_fbv_user/lance_form.html'):
#     leilao = get_object_or_404(Leilao, pk=id_leilao)
#     form = LanceForm(request.POST or None, leilao)
#     if form.is_valid():
#         lance = form.save(commit=False)
#         lance.leilao = leilao
#         lance.comprador = request.user
#         lance.save()
#         return redirect('leilao_fbv_user:show_leilao', pk=id_leilao)
#     return render(request, template_name, {'form':form})

####################################################################################
### Login User #####################################################################
####################################################################################
@login_required
def redirect_user(request):
#def redirect_vendedor(request, template_name='leilao_fbv_user/vendedor_page.html'):
    current_user = request.user.username
    #print(current_user)
    bool_vendedor = VendedorDAO.vendedor_filter(request, current_user)
    bool_comprador = CompradorDAO.comprador_filter(request, current_user)
    bool_leiloeiro = LeiloeiroDAO.leiloeiro_filter(request, current_user)

    if (bool_vendedor):
        #return render(request, 'leilao_fbv_user/vendedor_page.html')
        return redirect("leilao_fbv_user:vendedor_page")
        #return render(request, 'leilao_fbv_user/user_page.html')
    elif (bool_comprador):
        #return render(request, 'leilao_fbv_user/comprador_page.html')
        return redirect("leilao_fbv_user:comprador_page")
    elif (bool_leiloeiro or request.user.is_superuser):
        #return render(request, 'leilao_fbv_user/comprador_page.html')
        return redirect("leilao_fbv_user:leiloeiro_page")


####################################################################################
### Vendedor #######################################################################
####################################################################################

@login_required
def redirect_vendedor(request, template_name='leilao_fbv_user/vendedor_page.html'):
    return render(request, template_name)

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
#@login_required
#def redirect_user(request, template_name='leilao_fbv_user/comprador_page.html'):
#def redirect_comprador(request, template_name='leilao_fbv_user/comprador_page.html'):
#    return render(request, 'leilao_fbv_user/comprador_page.html')

# def list_comprador(request, template_name='leilao_fbv/comprador_list.html'):
#     data = CompradorDAO.vendedor_list(request, template_name=template_name)
#     return render(request, template_name, data)

@login_required
def redirect_comprador(request, template_name='leilao_fbv_user/comprador_page.html'):
    return render(request, template_name)

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

####################################################################################
### Leiloeiro ######################################################################
####################################################################################
def redirect_leiloeiro(request, template_name='leilao_fbv_user/leiloeiro_page.html'):
    return render(request, template_name)


####################################################################################
### Relatorio ######################################################################
####################################################################################

@login_required
def create_relatorio(request, id_leilao, template_name='leilao_fbv_user/create_relatorio.html'):
    data = {}
    data['leilao_id'] = id_leilao
    return render(request, template_name, data)

@login_required
def create_relatorio_faturamento(request, id_leilao, template_name='leilao_fbv_user/create_relatorio_desempenho.html'):
    leilao = get_object_or_404(Leilao, pk=id_leilao)
    data = {}
    data['leilao'] = leilao
    data['lance_vencedor'] = sorted(list(Lance.objects.filter(pk=id_leilao)), key=lambda t: t.valor, reverse=True)[0]
    data['comissao_vendedor'] = leilao.lote.valor_reserva * leilao.taxa_comissao_vendedor
    data['comissao_comprador'] = data['lance_vencedor'].valor * leilao.taxa_comissao_comprador
    return render(request, template_name, data)


@login_required
def create_relatorio_desempenho(request, id_leilao, template_name='leilao_fbv_user/create_relatorio_desempenho.html'):
    leilao = get_object_or_404(Leilao, pk=id_leilao)
    lista_lances = list(Lance.objects.filter(pk=id_leilao)) # verificar

    data = {}
    data['leilao'] = leilao
    data['numero_lances'] = len(lista_lances)
    data['lance_inicial'] = lista_lances[0]
    data['lance_final'] = lista_lances[-1]
    data['lance_vencedor'] = sorted(lista_lances, key=lambda t: t.valor, reverse=True)[0]
    return render(request, template_name, data)



