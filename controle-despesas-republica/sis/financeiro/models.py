from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from cupom import decodeQR, getHtml
from decimal import *
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Notas(models.Model):

    notafiscal = models.FileField(blank=True, null=True, upload_to='cupons')
    url_qrcode = models.URLField(blank=True, null=True, max_length=1000)
    usuario = models.ForeignKey(User,blank=True, null=True)

    def save(self,*args, **kwargs):
        super(Notas, self).save(*args, **kwargs)
        if self.url_qrcode != None:
            scratch(self.url_qrcode,self.usuario)
        elif decodeQR(self.notafiscal.name) != None:
            [scratch(x,self.usuario) for x in decodeQR(self.notafiscal.name)]

    class Meta:
        verbose_name = 'Notas'
        verbose_name_plural = 'Notas'

    def __unicode__(self):
        if self.notafiscal.name:
            return self.notafiscal.name
        else:
            return self.url_qrcode

class Compras(models.Model):
    usuario = models.ForeignKey(User,blank=True, null=True)
    item = models.IntegerField(blank=True, null=True)
    ean = models.CharField(blank=True, max_length=100)
    descricao = models.CharField(blank=True, max_length=100)
    quantidade = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    valorUnitario = models.DecimalField(max_digits=20, decimal_places=6)
    rateio = models.BooleanField(default=True)
    email = models.EmailField(blank=True, null=True)
    data = models.DateField(default=datetime.today)


    class Meta:
        verbose_name = 'Compras'
        verbose_name_plural = 'Compras'

    def __unicode__(self):
        return self.descricao


class Despesas(models.Model):

    descricao = models.CharField(blank=True, max_length=100)
    valor = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    fixa = models.BooleanField(default=False)
    dtLancamento = models.DateField(default=datetime.today)

    class Meta:
        verbose_name = 'Despesas'
        verbose_name_plural = 'Despesas'

    def __unicode__(self):
        return self.descricao

class Rateios(models.Model):
    usuario  = models.ForeignKey(User)
    despesa = models.ForeignKey(Despesas)
    perc = models.DecimalField(max_digits=6, decimal_places=2,default=0)

    class Meta:
        verbose_name = 'Rateio'
        verbose_name_plural = 'Rateios'

    def __unicode__(self):
        return self.usuario.username + " "+ self.despesa.descricao+" "+ str(self.perc)+"%"


class Extrato(models.Model):
    data = models.DateField(default=datetime.today)
    despesa = models.ForeignKey(Despesas)
    valor = models.DecimalField(max_digits=20, decimal_places=2)
    usuario = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Extrato'
        verbose_name_plural = 'Extratos'

    def __unicode__(self):
        return self.despesa.descricao+" "+str(self.valor)


def addCompra(it,username,data):
    cp = Compras.objects.create(usuario=username,item=it, ean=data[0], descricao=data[1],quantidade=Decimal(str(data[2]).replace(',','.')),valorUnitario=Decimal(str(data[4]).replace(',','.')))
    cp.save()

def scratch(url,username):
    if url:
        bc = getHtml(url)
        sp = getHtml(bc.iframe["src"])
        sp.find("td",{"class":"NFCCabecalho_SubTitulo"})
        for x in range(1,200):
            try:
                for it in sp.find_all("tr",{'id':'Item + '+str(x)}):
                    print x
                    addCompra(x,username,[x.get_text() for x in it.find_all('td')])

            except Exception as e:
                print e
