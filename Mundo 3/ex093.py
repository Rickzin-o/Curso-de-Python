ficha = dict()
ficha['Jogador'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {ficha["Jogador"]} jogou? '))

tgols = []
for i in range(1, partidas+1):
    tgols.append(int(input(f'Quantas gols na {i}ª partida? ')))
ficha['Gols'] = tgols[:]
ficha['Total de gols'] = sum(tgols)

print('---' * 25)
print(ficha)
print('---' * 25)

for k, v in ficha.items():
    print(f'{k} foi registrado com {v}')

print('---' * 25)

print(f'O jogador {ficha["Jogador"]} jogou {partidas} partidas')
for i, gols in enumerate(ficha['Gols']):
    print(f' - Na partida {i+1} ele fez {gols} gols')
print(f'Foi um total de {ficha["Total de gols"]} gols')
