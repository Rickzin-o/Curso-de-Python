from random import randint
from time import sleep
from operator import itemgetter

players = dict()
players['jogador1'] = randint(1, 6)
players['jogador2'] = randint(1, 6)
players['jogador3'] = randint(1, 6)
players['jogador4'] = randint(1, 6)
for k, v in players.items():
    print(f'O {k} tirou {v} no dado!')
    sleep(0.5)

print('\nRankings:')

colocacoes = []
colocacoes = sorted(players.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(colocacoes):
    print(f'Em {i+1}º lugar temos o {v[0]} com {v[1]}')
    sleep(0.25)
