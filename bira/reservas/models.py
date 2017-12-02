# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class pessoas(models.Model):
    nome = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __unicode__(self):
        return self.nome

class salao(models.Model):
    descricao = models.CharField(max_length=20)
    class Meta:
        verbose_name = 'Salao'
        verbose_name_plural = 'Saloes'

    def __unicode__(self):
        return self.descricao

class reservas(models.Model):
    salao = models.ForeignKey(salao)
    reservista = models.ForeignKey(pessoas)
    data_reserva = models.DateField()
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __unicode__(self):
        return self.salao.descricao + " " + self.reservista.nome
