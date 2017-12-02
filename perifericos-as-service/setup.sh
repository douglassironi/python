#!/bin/bash

pip install virtualenv
virtualenv microservphx2020
source ./microservphx2020/bin/activate

pip install bottle
pip install Pillow
pip install python-escpos
pip install pyserial
pip install pyusb
pip install qrcode
pip install PyYAML
pip install python-escpos-xml

chmod a+x appServices.py
./appServices.py

