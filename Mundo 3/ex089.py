boletim = []
while True:
    dados = []
    dados.append(str(input('Nome do aluno: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    boletim.append(dados[:])
    continua = str(input('Quer continuar? [S/N] '))
    while continua not in 'SsNn':
        continua = str(input('Quer continuar? [S/N] '))
    if continua in 'Nn':
        break
print('===' * 25)
print(f'{"No.":<5}{"NOME":<13}MÉDIA')
print('-' * 25)

for i, aluno in enumerate(boletim):
    media = (aluno[1]+aluno[2])/2
    print(f'{i:<5}{aluno[0]:<13}{media:.1f}')
print('===' * 25)

while True:
    mostrar = int(input('Digite o No. do aluno que você deseja ver os dados (999 interrompe): '))
    if mostrar == 999:
        break
    print(f'As notas de {boletim[mostrar][0]} são {boletim[mostrar][1]} e {boletim[mostrar][2]}')
    print('---' * 15)
print('\nPROGRAMA FINALIZADO')
