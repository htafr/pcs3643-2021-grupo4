from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.db.models import Q

from django.contrib.auth.models import User

from leilao_fbv.models import Vendedor, VendedorDAO, Comprador, CompradorDAO, Leiloeiro, LeiloeiroDAO
from .models import Leilao, LeilaoDAO, Lote, LoteDAO, Lance, LanceDAO
from leilao_fbv_user import models

####################################################################################
### Lote ###########################################################################
####################################################################################

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
    form, lote = LoteDAO.lote_update(request=request, pk=pk, template_name=template_name)
    if form.is_valid():
        form.save()
        lote.state = 'Pendente'
        lote.save()
        return redirect('leilao_fbv_user:lote_list')
    return render(request, template_name, {'form':form})

@login_required
def update_pending_lote(request, pk, template_name='leilao_fbv_user/lote_analise.html'):
    form, lote = LoteDAO.lote_pending(request=request, pk=pk, template_name=template_name)
    if form.is_valid():
        form.save()

        
        status_lote = form.cleaned_data.get('state')


        if status_lote == 'Aprovado':
            lote_verificacao = Lote.objects.get(pk=pk)
            valor_reserva = lote_verificacao.reserve_price
            taxa_vendedor, taxa_comprador = determina_comissoes(valor_reserva)
            # inclui no lote taxa de comissao e valor da comissao quando o lote eh aprovado
            # item usado para cobrar em qualquer leilao realizado (arrematado, nao arrematado e cancelado)
            lote_verificacao.taxa_comissao_vendedor = taxa_vendedor
            lote_verificacao.valor_comissao_vendedor = (taxa_vendedor / 100) * float(valor_reserva)
            print(taxa_vendedor, valor_reserva)
            lote_verificacao.save()

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
    return render(request, template_name, {'lote':lote})

####################################################################################
### Leilao #########################################################################
####################################################################################

@login_required
def create_leilao(request, pk, template_name='leilao_fbv_user/leilao_form.html'):
    form, lote = LeilaoDAO.leilao_create(request=request, pk=pk, template_name=template_name)
    if form.is_valid():
        ### Adiciona user no forms
        form.instance.user = request.user

        ### Cria leilao a partir do forms
        leilao = form.save(commit=False)
        leilao.lote_id = pk
        leilao.user_id = request.user.id

        # pega info do lote
        lote = Lote.objects.get(pk=pk)
        # atualiza infos de comissao do vendedor - valor de reserva
        # taxa e comissao add quando lote eh aprovado pelo leiloeiro
        leilao.taxa_comissao_vendedor = lote.taxa_comissao_vendedor
        leilao.valor_comissao_vendedor = lote.valor_comissao_vendedor


        ### Cria lance inicial para preencher o atributo da classe Leilao
        ### ESSE LANCE INICIAL NÃO DEVE FAZER PARTE DO RELATÓRIO
        lance = LanceDAO.init_lance(leilao.lote.start_price)
        lance.user = request.user
        lance.save()

        ### Passa o id do lance para o leilao
        leilao.lance_id = lance.id
        leilao.save()

        ### Passa o id do leilao criado para o lance
        ### dessa forma ele pode ser ligado ao leilao
        lance.leilao_id = leilao.id
        lance.save()

        lote.has_leilao = True
        lote.save()
        return redirect('leilao_fbv_user:redirect_user')

    context = {
        'form': form,
        'lote': lote,
    }
    return render(request, template_name, context)

@login_required
def show_leilao(request, pk, template_name='leilao_fbv_user/show_leilao.html'):
    leilao = LeilaoDAO.get_leilao(request=request, pk=pk, template_name=template_name)
    lances = sorted(Lance.objects.filter(leilao_id = pk), key=lambda t: t.valor, reverse=False)
    return render(request, template_name, {'leilao': leilao, 'lances': lances})

@login_required
def list_leilao_all(request, template_name='leilao_fbv_user/leilao_list_all.html'):
    data = LeilaoDAO.leilao_list_all(request=request, template_name=template_name)
    return render(request, template_name, data)

@login_required
def list_leilao_avail(request, template_name='leilao_fbv_user/leilao_list_avail.html'):
    data = LeilaoDAO.leilao_list_avail(request=request, template_name=template_name)
    return render(request, template_name, data)

@login_required
def show_participating_leilao(request, template_name="leilao_fbv_user/show_participating_leilao.html"):
    user_id = request.user.id
    leiloes = LeilaoDAO.get_participating_leilao(request=request, user_id=user_id, template_name=template_name)
    return render(request, template_name, {'leiloes': leiloes})

@login_required
def show_won_leilao(request, template_name="leilao_fbv_user/show_won_leilao.html"):
    user_id = request.user.id
    leiloes = LeilaoDAO.get_won_leilao(request=request, user_id=user_id, template_name=template_name)
    return render(request, template_name, {'leiloes': leiloes})

@login_required
def show_cancel_request(request, template_name="leilao_fbv_user/show_cancel_request.html"):
    leiloes = LeilaoDAO.get_cancel_request(request=request, template_name=template_name)
    return render(request, template_name, {'leiloes': leiloes})

@login_required
def update_leilao(request, pk, template_name='leilao_fbv_user/leilao_form.html'):
    form = LeilaoDAO.leilao_update(request=request, pk=pk, template_name=template_name)
    if form.is_valid():
        form.save()
        status_leilao = form.cleaned_data.get('status_leilao')
        if status_leilao == 'FINALIZADO':
            leilao = Leilao.objects.get(pk=pk)
            leilao_id = leilao.id
            lances = Lance.objects.filter(leilao_id=leilao_id)
            lances = list(lances)
            lote = Lote.objects.get(pk=leilao.lote_id)
             
            ultimo_valor = lances[-1]
            ultimo_valor = ultimo_valor.valor

            taxa_vendedor, taxa_comprador = determina_comissoes(ultimo_valor)

            comissao_vendedor = (taxa_vendedor / 100) * float(ultimo_valor)
            comissao_comprador = (taxa_comprador / 100) * float(ultimo_valor)

            leilao.taxa_comissao_comprador = taxa_comprador
            #leilao.taxa_comissao_vendedor = taxa_vendedor
            leilao.valor_comissao_comprador = comissao_comprador
            #leilao.valor_comissao_vendedor = comissao_vendedor
            
            if ultimo_valor >= lote.reserve_price:
                leilao.arrematado = True

            leilao.save()

        elif status_leilao == 'ATIVO':
            leilao = Leilao.objects.get(pk=pk)
            # alterar situacao de arremate do leilao caso seja aberto noavemente.
            leilao.arrematado = 0

            ## arrematado: finalizado e ultimo lance acima do valor de reserva
            ## nao arrematado: finalizado e ultimo lance abaixo do valor de reserva

            leilao.save()

        return redirect('leilao_fbv_user:list_leilao_avail')
    return render(request, template_name, {'form':form})

@login_required
def confirm_cancellation(request, pk, template_name='leilao_fbv_user/ask_cancellation.html'):
    leilao = LeilaoDAO.get_leilao(request=request, pk=pk, template_name=template_name)
    if request.method == 'POST':
        leilao.cancelar = True
        leilao.save()
        return redirect('leilao_fbv_user:my_avail_leiloes')
    return render(request, template_name, {'leilao':leilao})

@login_required
def delete_leilao(request, pk, template_name='leilao_fbv_user/leilao_confirm_delete.html'):
    leilao, lote = LeilaoDAO.leilao_delete(request=request, pk=pk, template_name=template_name)
    if request.method=='POST':
        lote.has_leilao = False
        lote.save()
        leilao.delete()
        return redirect('leilao_fbv_user:list_leilao_all')
    return render(request, template_name, {'leilao':leilao})

@login_required
def cancel_leilao(request, pk, template_name='leilao_fbv_user/auctioneer_cancel_auction.html'):
    leilao = LeilaoDAO.get_leilao(request=request, pk=pk, template_name=template_name)
    if request.method == 'POST':
        leilao.status_leilao = 'CANCELADO'
        leilao.cancelar = False
        leilao.save()
        return redirect('leilao_fbv_user:list_cancel_req')
    return render(request, template_name, {'leilao': leilao})

def determina_comissoes(valor):
    if valor == 0:
        taxa_vendedor = 0
        taxa_comprador = 0
    elif valor <= 1000:
        taxa_vendedor = 1
        taxa_comprador = 3
    elif valor <= 10000:
        taxa_vendedor = 2
        taxa_comprador = 4
    elif valor <= 50000:
        taxa_vendedor = 3
        taxa_comprador = 5
    elif valor <= 100000:
        taxa_vendedor = 4
        taxa_comprador = 6
    else:
        taxa_vendedor = 4
        taxa_comprador = 6
    
    #comissao_vendedor = valor * taxa_vendedor
    #comissao_comprador = valor * taxa_comprador

    #return taxa_vendedor, taxa_comprador, comissao_vendedor, comissao_comprador
    return taxa_vendedor, taxa_comprador



####################################################################################
### Lance ##########################################################################
####################################################################################

@login_required
def make_bid(request, pk, template_name='leilao_fbv_user/lance_form.html'):
    form, leilao = LeilaoDAO.make_bid(request=request, pk=pk, template_name=template_name)
    if form.is_valid():
        form.instance.user = request.user
        lance = form.save(commit=False)

        valor = form.cleaned_data.get('valor')

        if valor >= (leilao.lance.valor + leilao.lote.minimum_bid):
            lance.leilao_id = pk
            lance.save()
            leilao.lance = lance
            leilao.num_lances += 1
            if leilao.lance_inicial == 0:
                leilao.lance_inicial = valor
            leilao.save()

        return redirect('leilao_fbv_user:show_leilao', pk=leilao.id)

    context = {
        'form': form,
        'leilao': leilao,
    }
    return render(request, template_name, context)

####################################################################################
### Login User #####################################################################
####################################################################################

@login_required
def redirect_user(request):
    current_user = request.user.username

    bool_vendedor = VendedorDAO.vendedor_filter(request, current_user)
    bool_comprador = CompradorDAO.comprador_filter(request, current_user)
    bool_leiloeiro = LeiloeiroDAO.leiloeiro_filter(request, current_user)

    if (bool_vendedor):
        return redirect("leilao_fbv_user:vendedor_page")
    elif (bool_comprador):
        return redirect("leilao_fbv_user:comprador_page")
    elif (bool_leiloeiro or request.user.is_superuser):
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

@login_required
def show_my_leiloes(request, template_name='leilao_fbv_user/my_leiloes.html'):
    vendedor_id = request.user.id
    my_leiloes = LeilaoDAO.get_my_leiloes(request=request, user_id=vendedor_id, template_name=template_name)
    return render(request, template_name, {'leiloes': my_leiloes})

@login_required
def show_my_avail_leiloes(request, template_name='leilao_fbv_user/my_avail_leiloes.html'):
    vendedor_id = request.user.id
    avail_leilao = LeilaoDAO.get_my_avail_leilao(request=request, user_id=vendedor_id, template_name=template_name)
    return render(request, template_name, {'leiloes': avail_leilao})

####################################################################################
### Comprador ######################################################################
####################################################################################

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

####################################################################################
### Leiloeiro ######################################################################
####################################################################################

def redirect_leiloeiro(request, template_name='leilao_fbv_user/leiloeiro_page.html'):
    return render(request, template_name)

####################################################################################
### Relatorio ######################################################################
####################################################################################

@login_required
def create_relatorio(request, template_name='leilao_fbv_user/relatorio_page.html'):
    data = {}
    #data['leilao_id'] = id_leilao
    return render(request, template_name, data)

@login_required
def create_relatorio_faturamento(request, pk, template_name='leilao_fbv_user/relatorio_faturamento_page.html'):
    leilao = get_object_or_404(Leilao, pk=pk)
    data = {}
    data['leilao'] = leilao
    data['lance_vencedor'] = sorted(list(Lance.objects.filter(pk=pk)), key=lambda t: t.valor, reverse=True)[0]
    #data['comissao_vendedor'] = leilao.lote.valor_reserva * leilao.taxa_comissao_vendedor

    taxa_vendedor, taxa_comprador = determina_comissoes (data['lance_vencedor'].valor)

    leilao.taxa_comissao_vendedor = taxa_vendedor
    leilao.taxa_comissao_comprador = taxa_comprador

    data['comissao_vendedor'] = data['lance_vencedor'].valor * leilao.taxa_comissao_vendedor
    data['comissao_comprador'] = data['lance_vencedor'].valor * leilao.taxa_comissao_comprador

    leilao.valor_comissao_vendedor = data['comissao_vendedor']
    leilao.valor_comissao_comprador = data['comissao_comprador']

    leilao.save()

    return render(request, template_name, data)


@login_required
def create_relatorio_desempenho(request, pk, template_name='leilao_fbv_user/relatorio_desempenho_page.html'):
    leilao = get_object_or_404(Leilao, pk=pk)
    lista_lances = list(Lance.objects.filter(pk=pk)) # verificar

    data = {}
    data['leilao'] = leilao
    data['numero_lances'] = len(lista_lances)
    data['lance_inicial'] = lista_lances[0]
    data['lance_final'] = lista_lances[-1]
    data['lance_vencedor'] = sorted(lista_lances, key=lambda t: t.valor, reverse=True)[0]
    return render(request, template_name, data)

@login_required
def list_relatorio_desempenho(request, template_name='leilao_fbv_user/relatorio_desempenho_page.html'):
    #data = LeilaoDAO.leilao_list_all(request=request, template_name=template_name)
    data = {}
    data['object_list']  = Leilao.objects.filter(Q(status_leilao='FINALIZADO') | Q(status_leilao='CANCELADO'))
    lances = Lance.objects.all()
    #print(data.count())
    #print(len(data))
    #for i in range(len(lances)):
    #teste = lances.filter(leilao_id=1)
    #print(teste)
    #return render(request, template_name, {'data':data, 'lances':lances})
    return render(request, template_name, data)

@login_required
def list_relatorio_faturamento(request, template_name='leilao_fbv_user/relatorio_faturamento_page.html'):
    #data = LeilaoDAO.leilao_list_all(request=request, template_name=template_name)
    data = {}
    data['object_list']  = Leilao.objects.filter(Q(status_leilao='FINALIZADO') | Q(status_leilao='CANCELADO'))
    return render(request, template_name, data)

############################################
######### Consolidados #####################
############################################

@login_required
def list_relatorio_consolidado_desempenho(request, template_name='leilao_fbv_user/relatorio_consolidado_desempenho_page.html'):

    data = {}
    # leilao
    data['num_leiloes_total'] = Leilao.objects.all().count()
    data['num_leiloes_ativos'] = Leilao.objects.filter(status_leilao='ATIVO').count()
    data['num_leiloes_finalizados'] = Leilao.objects.filter(status_leilao='FINALIZADO').count()
    data['num_leiloes_cancelados'] = Leilao.objects.filter(status_leilao='CANCELADO').count()
    data['num_leiloes_arrematados'] = Leilao.objects.filter(status_leilao='FINALIZADO', arrematado=1).count()
    data['num_leiloes_nao_arrematados'] = Leilao.objects.filter(status_leilao='FINALIZADO', arrematado=0).count()
    # lotes
    data['num_lotes_total'] = Lote.objects.all().count()
    data['num_lotes_aprovados'] = Lote.objects.filter(state='Aprovado').count()
    data['num_lotes_pendentes'] = Lote.objects.filter(state='Pendente').count()
    data['num_lotes_negados'] = Lote.objects.filter(state='Negado').count()
    data['num_lotes_livros_novos'] = Lote.objects.filter(condition='Novo').count()
    data['num_lotes_livros_usados'] = Lote.objects.filter(condition='Usado').count()
    # lances
    data['num_lances_total'] = Lance.objects.all().count()
    # usuarios
    data['num_total_usuarios'] = User.objects.all().count()
    data['num_vendedores_cadastrados'] = Vendedor.objects.all().count()
    data['num_compradores_cadastrados'] = Comprador.objects.all().count()
    data['num_leiloeiros_cadastrados'] = Leiloeiro.objects.all().count()

    
    #print(data)

    return render(request, template_name, data)

@login_required
def list_relatorio_consolidado_faturamento(request, template_name='leilao_fbv_user/relatorio_consolidado_faturamento_page.html'):
    data = {}

    # receita proveniente de arremates de leiloes
    data['receita_bruta'] = 0

    # receita proveniente de arremates de leiloes + comissões compradores
    data['receita_bruta_total'] = 0
    
    # comissoes
    data['total_comissoes_compradores'] = 0
    data['total_comissoes_vendedores'] = 0
    
    # Repasse para vendedor - descontando taxa
    data['despesa_vendedores'] = 0
    

    leiloes = list(Leilao.objects.filter(Q(status_leilao='FINALIZADO') | Q(status_leilao='CANCELADO')))

    for leilao in leiloes:
        print(leilao)
        if leilao.arrematado == 1:
            lista_de_lances = sorted(Lance.objects.filter(leilao_id = leilao.id), key=lambda t: t.valor, reverse=True)
            valor_arrematado = float(lista_de_lances[0].valor)
        else:
            valor_arrematado = 0

        #print(valor_arrematado)
        taxa_vendedor, taxa_comprador = determina_comissoes(valor_arrematado)
        #print(taxa_vendedor, taxa_comprador)

        taxa_vendedor = float(taxa_vendedor / 100)
        taxa_comprador = float(taxa_comprador / 100)
        
        data['total_comissoes_compradores'] += taxa_comprador * valor_arrematado
        data['total_comissoes_vendedores'] += leilao.valor_comissao_vendedor

        data['receita_bruta'] += valor_arrematado

        data['receita_bruta_total'] += (1 + taxa_comprador) * float(valor_arrematado)

        data['despesa_vendedores'] += round(valor_arrematado - (leilao.valor_comissao_vendedor), 2)

        print(taxa_vendedor, taxa_comprador)

    data['receita_bruta'] = round(data['receita_bruta'], 2)
    data['receita_bruta_total'] = round(data['receita_bruta_total'], 2)

    data['total_comissoes_compradores'] = round(data['total_comissoes_compradores'], 2)
    data['total_comissoes_vendedores'] = round(data['total_comissoes_vendedores'], 2) 


    data['receita_liquida'] = round(data['total_comissoes_compradores'] + data['total_comissoes_vendedores'], 2)

    # taxa media de comissao
    if data['receita_bruta'] > 0:
        data['taxa_media_comprador'] = round(data['total_comissoes_compradores'] * 100 / data['receita_bruta'], 2)
        data['taxa_media_vendedor'] = round(data['total_comissoes_vendedores'] * 100 / data['receita_bruta'], 2)

    # comissao media
    if len(leiloes) > 0:
        data['comissao_media_comprador'] = round(data['total_comissoes_compradores'] / len(leiloes), 2)
        data['comissao_media_vendedor'] = round(data['total_comissoes_vendedores'] / len(leiloes), 2)

    print(data)

    return render(request, template_name, data)


