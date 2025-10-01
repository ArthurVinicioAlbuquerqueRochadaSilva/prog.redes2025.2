# Operações bit a bit (bitwise) com strings em Python
strTexto_1 = 'P'
strTexto_2 = 'd'

# Operação bit a bit
andResultado = ord(strTexto_1) & ord(strTexto_2)
orResultado  = ord(strTexto_1) | ord(strTexto_2)
xorResultado = ord(strTexto_1) ^ ord(strTexto_2)

print(f'strTexto_1 & strTexto_2: ACSII = {andResultado:>3} -> {chr(andResultado)} -> {(andResultado):08b}')
print(f'strTexto_1 | strTexto_2: ACSII = {orResultado:>3} -> {chr(orResultado)} -> {(orResultado):08b}')
print(f'strTexto_1 ^ strTexto_2: ACSII = {xorResultado:>3} -> {chr(xorResultado)} -> {(xorResultado):08b}')