valor = int(input('Digite um número inteiro: '))
razao = int(input('Agora digite a razão: '))
n = 1
pa = f'A progressão aritmética é {valor}, '
while n != 10:
    valor += razao
    pa += f'{valor}, '
    n += 1
print(pa + 'fim.')
