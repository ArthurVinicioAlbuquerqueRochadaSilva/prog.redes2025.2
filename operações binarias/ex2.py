import sys
intvalor = int(input('Digite um número inteiro:'))
if intvalor < 0:
    sys.exit('Digite valor positivo')
intQtbits = intvalor.bit_length()
print(intQtbits)
binValor = bin(intvalor)[2:]
print(binValor)
if len(binValor) % 8 != 0:
    