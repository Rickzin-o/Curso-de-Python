l = []
while True:
    value = int(input('Digite um valor inteiro: '))
    if value in l:
        print('Valor duplicado! Não será adicionado.')
    else:
        l.append(value)
        print('Valor adicionado no sistema.')
    continua = str(input('Quer continuar digitando? [S/N] '))
    while continua not in 'NnSs':
        continua = str(input('Quer continuar digitando? [S/N] '))
    if continua in 'Nn':
        break
l.sort()
print('--' * 25)
print(f'Os valores digitados em ordem crescente são {l}')
