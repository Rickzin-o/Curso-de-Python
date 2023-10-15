dados = []
pessoa = []
maiorp = menorp = 0
print('CADASTRO DE PESSOAS POR PESO')
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(dados) == 0:
        maiorp = menorp = pessoa[1]
    else:
        if pessoa[1] >= maiorp:
            maiorp = pessoa[1]
        if pessoa[1] <= menorp:
            menorp = pessoa[1]
    dados.append(pessoa[:])
    pessoa.clear()
    continua = str(input('Quer continuar cadastrando? [S/N] '))
    if continua not in 'SsNn':
        continua = str(input('Quer continuar cadastrando? [S/N] '))
    if continua in 'Nn':
        break

maiorlista = []
menorlista = []
for p in dados:
    if p[1] == maiorp:
        maiorlista.append(p[0])
    if p[1] == menorp:
        menorlista.append(p[0])
print('===' * 25)
print(f'Foram cadastradas {len(dados)} pessoas.')
print(f'O maior peso foi {maiorp}KG. Peso de {maiorlista}')
print(f'O menor peso foi {menorp}KG. Peso de {menorlista}')

