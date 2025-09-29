
strIP = input('Digite o ip: ')
lstIp = [int(x) for x in strIP.split('.')]
bytesIp = bytes(lstIp)
IP = int.from_bytes(bytes([int(x) for x in strIP.split('.')]), 'big')
print(f'Aqui está o número do IPV4 em binário: {IP:032b}')

CIDR = 24
mask = 0xFFFFFFFF >> (32 - CIDR) << (32 - CIDR)
print(f'Aqui está o número da mask em binário: {mask}')

binRede = IP & mask
print(f'Aqui está o número da rede em binário: {binRede:}')

strRede = '.'.join([str(x) for x in binRede.to_bytes(4)])
print(f'Esse é o endereço IPV4 da rede: {strRede}')

binHost = binRede + 1
intHost = int(binHost)
ofcHost = '.'.join([str(x) for x in intHost.to_bytes(4)])
print(f'Aqui está o primeiro host: {ofcHost}')

''