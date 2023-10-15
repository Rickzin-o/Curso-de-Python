lista = list()
media = 0
while True:
    cadastro = dict()
    cadastro['Nome'] = str(input('Nome da pessoa: '))
    cadastro['Sexo'] = str(input(f'Sexo de {cadastro["Nome"]} [M/F]: ')).upper()
    while cadastro['Sexo'] not in "MmFf":
        cadastro['Sexo'] = str(input(f'ERRO! Sexo de {cadastro["Nome"]} [M/F]: ')).upper()
    cadastro['Idade'] = int(input(f'Idade de {cadastro["Nome"]}: '))
    media += cadastro['Idade']
    lista.append(cadastro)
    continua = str(input(f'{cadastro["Nome"]} CADASTRADO! Quer continuar? [S/N] '))
    while continua not in "SsNn":
        continua = str(input(f'ERRO! Quer continuar? [S/N] '))
    if continua in "Nn":
        break

media /= len(lista)
mulheres = []
pesacimed = []
for d in lista:
    for k, v in d.items():
        if k == 'Sexo' and v == 'F':
            mulheres.append(d['Nome'])
for d in lista:
    for k, v in d.items():
        if k == 'Idade' and v > media:
            pesacimed.append(d)

print('---' * 25)
print(f'== Foram cadastradas um total de {len(lista)} pessoas')
print(f'== A média de idade é de {media}')
print(f'== As mulheres registradas foram: {mulheres}')
print(f'\n== As pessoas acima da média de idade foram:')

for d in pesacimed:
    for k, v in d.items():
        print(f'{k} = {v};', end=' ')
    print()
