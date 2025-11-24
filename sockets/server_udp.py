import socket

# ----------------------------------------------------------------------
HOST_IP_SERVER  = ''              # Definindo o IP do servidor
HOST_PORT       = 50000           # Definindo a porta

BUFFER_SIZE     = 512             # Tamanho do buffer
CODE_PAGE       = 'utf-8'         # Definindo a página de 
                                  # codificação de caracteres
# ----------------------------------------------------------------------


# Criando o socket (socket.AF_INET -> IPV4 / socket.SOCK_DGRAM -> UDP)
sockServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sockServer.settimeout(0.5)

# Ligando o socket à porta
sockServer.bind( (HOST_IP_SERVER, HOST_PORT) ) 

print('\nRecebendo Mensagens...\n\n')
print('Pressione CRTL+C para sair...')

try:
    while True:
        try:
        # Recebendo os dados do cliente
            byteMensagem, tuplaCliente = sockServer.recvfrom(BUFFER_SIZE)
        except socket.timeout:
            continue
        else:
            strNomeHost = socket.gethostbyaddr(tuplaCliente[0])[0]
            limpo = strNomeHost.split('.')[0]
            # Imprimindo a mensagem recebida convertendo de bytes para string
            print(f'{tuplaCliente}: {limpo} {byteMensagem.decode(CODE_PAGE)}')
except KeyboardInterrupt:
         print('Aviso: saindo do servidor: foi pressionado CRTL + C')
finally:
    sockServer.close()
print('Servidor Finalizado')    