#!/usr/bin/python
from sys import argv
import os
import shutil
import datetime
import subprocess
import time
import logging
import logging.handlers
import zbar
from PIL import Image
from daemon import runner

path="/home/dev/Projects/DecodeBarCode/"

def barcode(arq):

	# create a reader
	scanner = zbar.ImageScanner()

	# configure the reader
	scanner.parse_config('enable')

	# obtain image data
	pil = Image.open(arq).convert('L')
	width, height = pil.size
	raw = pil.tobytes()

	# wrap image data
	image = zbar.Image(width, height, 'Y800', raw)

	# scan the image for barcodes
	scanner.scan(image)

	# extract results
	for symbol in image:
	    # do something useful with results
		dt= datetime.datetime.now()
		logger.info("Arquivo processado "+arq+" Codigo: "+symbol.data)
		shutil.move(arq,path+"/Processados/"+symbol.data+"_"+dt.strftime("%Y%m%d_%H%M%S%f")+".png")

	# clean up
	del(image)
	#Move as Imagens nao reconhecidas.
	dt= datetime.datetime.now()
	if os.path.exists(arq):
		logger.info("Arquivo NaoReconhecidos movendo com o nome de "+dt.strftime("%Y%m%d_%H%M%S%f"))
		shutil.move(arq,path+"/NaoReconhecidos/"+dt.strftime("%Y%m%d_%H%M%S%f")+".png")
	



class App():
	def __init__(self):
		self.stdin_path = '/dev/null'
		self.stdout_path = '/dev/tty'
		self.stderr_path = '/dev/tty'
		self.pidfile_path =  '/tmp/bar.pid'
		self.pidfile_timeout = 5

	

	def run(self):
		while True:
			included_extenstions = ['jpg', 'bmp', 'png','JPG', 'gif']
			file_names = [fn for fn in os.listdir(path) if not fn.startswith('.') and any(fn.endswith(ext) for ext in included_extenstions)]
			for f in file_names:
				try:
					barcode(path+f)
				except Exception, e:
						logger.info(e)
			time.sleep(10)

app = App()
logger = logging.getLogger("DaemonLog")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.handlers.RotatingFileHandler(
              "/var/log/bar_py/bar.log", maxBytes=2097152, backupCount=5)

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("Iniciando o processo.")

daemon_runner = runner.DaemonRunner(app)
daemon_runner.daemon_context.files_preserve=[handler.stream]
daemon_runner.do_action()

