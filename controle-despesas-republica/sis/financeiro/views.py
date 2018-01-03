from django.shortcuts import render
from django.contrib.auth.models import User
from financeiro.models import Extrato
from datetime import datetime
from django.db.models import Sum, Q
# Create your views here.
def resumo(request):
    extrato = Extrato.objects.filter(usuario_id=request.user.id).values('data').annotate(valor_total=Sum('valor')).order_by('-data')
    return render(request, 'resumo.html', {'usuario':request.user,'extrato':extrato})
