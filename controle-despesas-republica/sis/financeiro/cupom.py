from PIL import Image
# import zbarlight
import requests
from bs4 import BeautifulSoup


def decodeQR(arquivo):
    im = Image.open(arquivo)
    im.save(arquivo[:-3]+"png" )
    with open(arquivo[:-3]+"png", 'rb') as image_file:

        print image_file
        image = Image.open(image_file)
        image.load()
        # codes = zbarlight.scan_codes('qrcode', image)
        print codes
    return codes

def getHtml(url):
    rq = requests.get(url)
    return  BeautifulSoup(rq.text,"html.parser")
