# Periferico as Service
Integraçāo com Hardware disponibilizando serviço.

A ideia e ter um microservico que faz a comunicacao com o hardware, gereando um RESTFull para ser consumido por qualquer sistema.

Nesse servico por exemplo, podemos mandar um arquivo direto para a impressora, acionar um PINPAD, entre outras coisas.

Vamos a instalacao:
```
sudo pip install virtualenv
virtualenv <nomeAmbiente>
source ./<nomeAmbiente>/bin/activate

sudo pip install bottle
sudo pip install Pillow
sudo pip install python-escpos
sudo pip install pyserial
sudo pip install pyusb
sudo pip install qrcode
sudo pip install PyYAML
sudo pip install python-escpos-xml

```
Ou basta roda o setup.sh para criar o ambiente.
