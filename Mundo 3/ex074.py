from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os números sorteados foram ', end='')
for i, n in enumerate(numeros):
    print(n, end=' ')
print(f'\nO maior valor foi {max(numeros)}.\nE o menor valor foi {min(numeros)}.')
