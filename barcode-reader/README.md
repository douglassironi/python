#  Barcode Reader.

Modulo em python para leitura de imagens e identificao de codigos de barras.
Utilizado para envio e vinculo de documentos para GED.

Basicamente, le imagens em diretorio e renomea a mesma para o codigo de barras identificado.
Como roda com o deamon, o script acaba se tornando um serviço.

Exemplo:
```sh
dev@srv01:~/Projects/DecodeBarCode$ ./bar.py
usage: bar.py start|stop|restart
