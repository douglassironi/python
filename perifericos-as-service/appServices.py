!./microservphx2020/bin/python
import os
import re
import subprocess
from io import BytesIO, open
import usb
from bottle import route, run, template
from bottle import request, response
from bottle import post, get, put, delete
from escpos.printer import Usb
from escpos_xml import parse
from base64 import *
import re, json
from ctypes import cdll
# 
#  Servico para comunicar com a impressora.
#  Parametro: documento
#  Dado: Um XML em base64
# 

@get('/impressora')
def descSrvImprime():
    data = {}
    data['descricao']= '/impressora'
    data['parametro']='documento'
    data['tipo_de_dados']='XML de Comandos base64'
    data['documentacao_XML']='https://pypi.python.org/pypi/python-escpos-xml/0.1.0'
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(data)


@post('/impressora')
def imprime():

    namepattern = re.compile(r'^[a-zA-Z\d]{1,64}$')

    try:
        if request.forms.get('documento'):
                retorno="Enviado para Impressora com sucesso"
                printer = Usb(0x04b8,0x0e02,0)
                printer.text(b64decode(request.forms.get('documento')))
                printer.cut()
                retorno = "Impresso com sucesso."
        else:
                response.status = 400
                retorno = "Deve ser informado o parametro documento, que o valor e uma base64."

    except Exception, e:
        response.status = 400
        retorno = str(e)

    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'retorno': retorno})

@get('/devices')
def devices():
    device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
    df = subprocess.check_output("lsusb", shell=True)
    devices = []
    for i in df.split('\n'):
        if i:
            info = device_re.match(i)
            if info:
                dinfo = info.groupdict()
                dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
                devices.append(dinfo)
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(devices)



@post('/pinpad/ConfiguraIntSiTefInterativo')
def ConfiguraIntSiTefInterativo():
    l = cdll.LoadLibrary('libclisitef.so')
    try:
        if request.forms.get('servidor'):
            pass
        if request.forms.get('loja'):
            pass
        if request.forms.get('caixa'):
            pass
        else:
            response.status = 400
            retorno = "Deve ser informado o parametro servidor, loja e caixa para configurar no PinPad."

        ret = l.ConfiguraIntSiTefInterativo(request.forms.get('servidor'),request.forms.get('loja'),request.forms.get('caixa'),0)
        l.VerificaPresencaPinPad()
        retorno = ret
    except Exception, e:
       response.status = 400
       retorno = str(e)

    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'retorno': retorno})




@post('/pinpad/EscreveMensagemPinPad')
def EscreveMensagemPinPad():
    l = cdll.LoadLibrary('libclisitef.so')
    #l.ConfiguraIntSiTefInterativo('10.11.101.69','00000031','cx000001',0)
    #l.VerificaPresencaPinPad()
    try:
        if request.forms.get('mensagem'):
            ret = l.EscreveMensagemPermanentePinPad(request.forms.get('mensagem'))
            retorno = "Mensagem escrita com sucesso no pinpad" + str(ret)
        else:
            response.status = 400
            retorno = "Deve ser informado o parametro mensagem, que vai escrever no PinPad."

    except Exception, e:
        response.status = 400
        retorno = str(e)

    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'retorno': retorno})



@get('/')
def index():

    response.headers['Content-Type'] = 'application/json'
    data = {}
    data['impressora']='/impressora'
    data['gaveta'] = '/gaveta'
    data['pinpad']='/pinpad'

    return json.dumps(data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
