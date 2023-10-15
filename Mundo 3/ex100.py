from random import randint
from time import sleep


def sorteia(lst):
    print('Sorteando 5 valores...', end=' ')
    for i in range(5):
        n = randint(1, 10)
        print(n, end = ' ')
        lst.append(n)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lst):
    soma = 0
    for i, v in enumerate(lst):
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lst} temos {soma}.')


numeros = []
sorteia(numeros)
somaPar(numeros)
