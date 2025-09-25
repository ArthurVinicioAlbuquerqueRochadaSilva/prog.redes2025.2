'''
Escreva um programa em Python que receba um endereço IPv4 no formato decimal 
(exemplo: 192.168.1.10) e exiba o endereço em formato binário (cada octeto separado por ponto).
'''
ip = '192.10.5.2'
print(f'Ip normal.....: {ip}')
lstIp = [bin(int(x))[2:] for x in ip.split('.')]
print(f'Ip em bits....: {lstIp}')
