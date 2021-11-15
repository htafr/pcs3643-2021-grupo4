from django import template
from leilao_fbv.models import Leiloeiro as Leiloeiro_fbv

register = template.Library() 

@register.filter(username='username') 
def is_leiloeiro(user, username):
    return Leiloeiro_fbv.objects.filter(username = username).exists()