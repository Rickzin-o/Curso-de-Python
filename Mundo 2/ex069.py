homens = maiores = mulher20 = 0
print('SISTEMA DE CADASTRO')
while True:
    print('---' * 20)
    print('   Cadastre alguém   ')
    print('---' * 20)
    idade = int(input('Idade: '))
    genero = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while genero not in "MF":
        genero = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if genero in 'Mm':
        homens += 1
    if genero in 'Ff' and idade < 20:
        mulher20 += 1
    if idade > 18:
        maiores += 1
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input('Quer continuar cadastrando? [S/N]: ')).strip().upper()[0]
    if continuar in "Nn":
        break
print('===' * 25)
print(f'Foram cadastradas {maiores} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {homens} homens.')
print(f'Foram cadastradas {mulher20} mulheres com menos de 20 anos.')
