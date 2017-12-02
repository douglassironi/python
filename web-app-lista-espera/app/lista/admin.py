# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import DadosFamilia, Especialidades, teste



# Register your models here.
admin.site.site_header = 'Lista de espera'

class DadosFamiliaAdmin(admin.ModelAdmin):
    exclude=['data_inativado','criado_por','data_solicitacao']
    list_display = ('id', 'nome','necessidade','criado_por','data_solicitacao','ativo')


admin.site.register(DadosFamilia,DadosFamiliaAdmin)
admin.site.register(Especialidades)
admin.site.register(teste)
