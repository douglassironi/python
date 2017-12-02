# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class database(models.Model):
    nome = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Database'
        verbose_name_plural = 'Databases'

    def __unicode__(self):
        return self.nome

class clientes(models.Model):
    nome = models.CharField(max_length=100)
    enderecos = models.CharField(max_length=100)
    database = models.ForeignKey(database)
