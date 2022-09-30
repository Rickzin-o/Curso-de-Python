import random
from time import sleep

pensei = random.choice([0, 1, 2, 3, 4, 5])
print('-/-' * 24)
print('O computador pensará num número de 0 a 5, se você acertar, você ganha!')
print('-/-' * 24)
sleep(1)
escolhi = int(input('Tente acertar qual o número escolhido: '))
print('Hm...')
sleep(2)
if pensei == escolhi:
    # Se o número escolhido for igual ao pensado pelo computador, isso acontece
    print('Parabéns! Você acertou! O número escolhido foi {}'.format(pensei))
else:
    # Se o número escolhido pelo usuário for diferente do número do computador, isso acontece
    print('Ops! Você errou... O número escolhido foi {} e você escolheu {}'.format(pensei, escolhi))
print('Fim de jogo!')
