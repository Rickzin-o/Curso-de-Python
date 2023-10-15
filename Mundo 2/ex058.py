import random

print('Tente adivinhar qual número, entre 0 e 10, o computador escolheu!')
escolha = random.randint(0, 10)
adivinho = int(input('Digite um número: '))
n = 0
while adivinho != escolha:
    n += 1
    maiormenor = 'mais' if adivinho < escolha else 'menos'
    adivinho = int(input(f'Errado, é {maiormenor}! Digite outro número: '))
print(f'Parabéns! Eu escolhi o número {escolha}! Você errou {n} vezes.')
