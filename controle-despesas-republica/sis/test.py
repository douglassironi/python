from PIL import Image
import zbarlight
import requests
from bs4 import BeautifulSoup
from decimal import *


def decodeQR(arquivo):
    with open(arquivo, 'rb') as image_file:
         image = Image.open(image_file)
         image.load()
    codes = zbarlight.scan_codes('qrcode', image)
    return codes

def getHtml(url):
    rq = requests.get(url)
    return  BeautifulSoup(rq.text,"html.parser")

def scratch(url):
    bc = getHtml(url)
    sp = getHtml(bc.iframe["src"])
    sp.find("td",{"class":"NFCCabecalho_SubTitulo"})
    data = []
    for x in range(1,200):
        for it in sp.find_all("tr",{'id':'Item + '+str(x)}):
            data= [x.get_text() for x in it.find_all('td')]
    print Decimal(str(data[5]).replace(',','.'))
[scratch(x) for x in decodeQR("TESTE.png")]
