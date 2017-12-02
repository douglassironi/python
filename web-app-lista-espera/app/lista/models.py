# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime



class Especialidades(models.Model):
    # TODO: Define fields here

    descricao = models.CharField(blank=True, max_length=100)
    responsavel  = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Especialidades'
        verbose_name_plural = 'Especialidades'

    def __unicode__(self):
        return self.descricao


class teste(models.Model):
    descricao= models.CharField(max_length=10)
    def __unicode__(self):
        return self.descricao
# Create your models here.
class DadosFamilia(models.Model):
    # TODO: Define fields here
    nome = models.CharField( max_length=100)
    nascimento = models.DateField()
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    estado = models.CharField(max_length=2, default="RS")
    necessidade  = models.ForeignKey(Especialidades)
    data_solicitacao = models.DateTimeField(blank=True, default=datetime.datetime.now)
    ativo = models.BooleanField(default=True)
    data_inativado = models.DateField(default=datetime.datetime.today)
    criado_por = models.ForeignKey(User,default=1)


    class Meta:
        verbose_name = 'dados_familia'
        verbose_name_plural = 'Dados das Familias'

    def __unicode__(self):
        return self.nome
