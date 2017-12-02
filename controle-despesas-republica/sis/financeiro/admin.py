from django.contrib import admin
from django import forms
from daterange_filter.filter import DateRangeFilter
from models import Compras, Despesas, Rateios, Extrato, Notas
# Register your models here.
admin.site.site_header = 'Farrofas House Despesas'



class ExtratoAdmin(admin.ModelAdmin):
    list_filter = (('data',DateRangeFilter), 'despesa', 'usuario')
    list_display =('data','despesa','valor','usuario')

class NotasAdmin(admin.ModelAdmin):
    list_display =('notafiscal','url_qrcode')
    exclude = ('usuario',)

    def save_model(self,request,obj,form,change):
		obj.usuario = request.user
		obj.save()


def remover_rateio(modeladmin, request, queryset):
    queryset.update(rateio=False)
    # make_published.short_description = "Retirar os Itens do Rateio"

def adicionar_rateio(modeladmin, request, queryset):
    queryset.update(rateio=True)
    # make_published.short_description = "Retirar os Itens do Rateio"


class ComprasAdmin(admin.ModelAdmin):
    list_filter = ('data', 'usuario')
    list_display =('data','ean','descricao','quantidade','valorUnitario','rateio')
    actions = [remover_rateio, adicionar_rateio]

class DespesasAdmin(admin.ModelAdmin):
    list_display =('descricao','valor','fixa')

class RateioAdmin(admin.ModelAdmin):
    list_display =('usuario','despesa','perc')

admin.site.register(Rateios,RateioAdmin)
admin.site.register(Despesas,DespesasAdmin)
admin.site.register(Compras,ComprasAdmin)
admin.site.register(Notas,NotasAdmin)
admin.site.register(Extrato,ExtratoAdmin)
