'''
   Lendo Metadados de Imagens JPG (EXIF)
'''
import os, sys

# ------------------------------------------------------------------------------------------
# Variáveis e Constantes
DIR_APP    = os.path.dirname(__file__)
DIR_IMG    = f'{DIR_APP}\\imagens'
strNomeArq = f'{DIR_IMG}\\presepio_natalino.jpg'

# ------------------------------------------------------------------------------------------
try:
   fileInput = open(strNomeArq, 'rb')
except FileNotFoundError:
   sys.exit('\nERRO: Arquivo Não Existe...\n')
except Exception as erro:
   sys.exit(f'\nERRO: {erro}...\n')
else:
   # Verificando se o arquivo informado é JPG 
   if fileInput.read(2) != b'\xFF\xD8':
      fileInput.close()
      sys.exit('\nERRO: Arquivo informado não é JPG...\n')
    # Verifica se o arquivo possui metadados
   if fileInput.read(2) != b'\xFF\xE1':
      fileInput.close()
      sys.exit('\nAVISO: Este arquivo não possui metadados...\n')
 # Obtendo o header do EXIF
   exifSize      = fileInput.read(2)
   exifHeader    = fileInput.read(6) # EXIF Header (marcador EXIF)