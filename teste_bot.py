import requests, sys
from tk_bot import *

url = f'https://api.telegram.org/bot{token}'
print('RECEBENDO MENSAGENS:' )
while True:
    reqURL = requests.get(url + '/getUpdates')
    if not reqURL.status_code == 200:
        sys.exit('Erro na requisição \nCódigo de retorno:' + str(reqURL.status_code))
    if reqURL.json()['result'] == []: continue
    jsretorno = reqURL.json()
    