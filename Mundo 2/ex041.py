from time import sleep
from datetime import date
print('\033[0:36mVocê vai participar de um programa de natação e precisa saber sua categoria\033[m')
sleep(1)
nasce = int(input('Digite seu ano de nascimento aqui aqui: '))
anoatual = date.today().year
idade = anoatual - nasce
print('Você tem {} anos'.format(idade))
if idade <= 9:
    print('Você será da categoria mirim')
elif idade <= 14:
    print('Você será da categoria infantil')
elif idade <= 19:
    print('Você será da categoria Junior')
elif idade <= 20:
    print('Você será da categoria sênior')
else:
    print('Você será da categoria master')
