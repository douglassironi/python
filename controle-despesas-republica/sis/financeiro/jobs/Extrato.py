from django_extensions.management.jobs import BaseJob
from financeiro.models import Compras, Extrato, Despesas, Rateios
from django.contrib.auth.models import User
from datetime import datetime, date
from django.db.models import Sum
import operator
class Job(BaseJob):
    help = "Job extrato mensal."

    def execute(self):
        # executing empty sample job
        def addExtrato(des, vlr, usr):
            ex = Extrato(despesa=des,valor=vlr,usuario=usr)
            ex.save()

        us = User.objects.all()
        co = Compras.objects.filter(rateio=True,data__month=datetime.today().strftime("%m")).all()
        de = Despesas.objects.all()
        # LIMPA O EXTRATO JA LANCADO.
        Extrato.objects.filter(data__month=datetime.today().strftime("%m")).delete()
        #
        for usr in us:
            credito = 0
            for c in co.filter(usuario=usr.id):
                credito += c.valorUnitario+c.quantidade
            if round(credito) > 0:
                ds = Despesas.objects.get(descricao="COMPRAS")
                ds.valor = reduce(operator.add,[c.valorUnitario+c.quantidade for c in co ])
                ds.save()
                addExtrato(ds,-round(credito,2),usr)

            for x in de:
                 rt = Rateios.objects.filter(despesa=x.id,usuario=usr.id)
                 if [c for c in rt]:
                     for ra in [c for c in rt]:
                         addExtrato(x,round((x.valor * ra.perc)/100,2),usr)
                 else:
                     addExtrato(x,round( x.valor / us.count(),2),usr)
        #
        #
        #
