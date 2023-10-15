lista = list()
while True:
    ficha = dict()
    ficha['Jogador'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {ficha["Jogador"]} jogou? '))
    tgols = []
    for i in range(1, partidas+1):
        tgols.append(int(input(f'Quantas gols na {i}ª partida? ')))
    ficha['Gols'] = tgols[:]
    ficha['Total'] = sum(tgols)
    lista.append(ficha.copy())
    
    continua =  str(input('Quer continuar? [S/N] '))
    if continua in "Nn":
        break
    print('-' * 30)
print('===' * 25)
print(f'{"Noº":<4}{"Nome":<14}{"Gols":<16}{"Total":<6}')
print('-' * 40)

for i, d in enumerate(lista):
    print(f"{i:<4}{d['Jogador']:<14}{str(d['Gols']):<16}{str(d['Total']):<6}")

while True:
    print('-' * 40)
    index = int(input('Mostrar dados de qual jogador? '))
    if index == 999:
        break
    if index < len(lista):
        jogador = lista[index]
        print(f'== LEVANTAMENTO DO JOGADOR {jogador["Jogador"]}:')
        for i, v in enumerate(jogador['Gols']):
            print(f'    No jogo {i+1} ele fez {v} gols.')
    if index >= len(lista):
        print(f'Não existe jogador com código {index}! Tente novamente')

print('< PROGRAMA FINALIZADO >')
