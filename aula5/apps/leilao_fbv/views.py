from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Lote

class LoteForm(ModelForm):
    class Meta:
        model = Lote
        fields = ['name', 'summary', 'qty',
                  'category', 'condition', 'min_value',
                  'opening_date']

def lote_list(request, template_name='leilao_fbv/lote_list.html'):
    lote = Lote.objects.all()
    data = {}
    data['object_list'] = lote
    return render(request, template_name, data)

def lote_create(request, template_name='leilao_fbv/lote_form.html'):
    form = LoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('leilao_fbv:lote_list')
    return render(request, template_name, {'form':form})

def lote_update(request, pk, template_name='leilao_fbv/lote_form.html'):
    lote= get_object_or_404(Lote, pk=pk)
    form = LoteForm(request.POST or None, instance=lote)
    if form.is_valid():
        form.save()
        return redirect('leilao_fbv:lote_list')
    return render(request, template_name, {'form':form})

def lote_delete(request, pk, template_name='leilao_fbv/lote_confirm_delete.html'):
    lote= get_object_or_404(Lote, pk=pk)    
    if request.method=='POST':
        lote.delete()
        return redirect('leilao_fbv:lote_list')
    return render(request, template_name, {'object':lote})
