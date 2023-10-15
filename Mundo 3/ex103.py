def ficha(nome='DESCONHECIDO', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'

name = str(input('Nome do jogador: '))
goals = input('Número de gols: ')
if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0

if name.strip() == '':
    print(ficha(gols=goals))
else:
    print(ficha(name, goals))
