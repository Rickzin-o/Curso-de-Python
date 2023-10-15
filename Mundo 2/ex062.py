valor = int(input('Digite um número inteiro: '))
razao = int(input('Agora digite a razão: '))
n = 0
termos = 10
running = True
pa = f'A progressão aritmética é {valor}, '
while running:
    valor += razao
    pa += f'{valor}, '
    n += 1
    if n == termos:
        print(pa + 'fim.')
        termos = int(input('Quantos mais termos você gostaria de ver? '))
        n = 0
    if termos == 0:
        running = False
print('Ok! Acabamos.')
