import socket
'''
meu_socket1 = socket.AF_INET 
meu_socket2 = socket.SOCK_DGRAM

print(meu_socket1)
print(meu_socket2)
'''
name = socket.gethostname()
ip = socket.gethostbyname('www.globo.com     nbv n')
print(ip)

print(name)
dados = socket.gethostbyaddr(ip)
print(dados)