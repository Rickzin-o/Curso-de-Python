lista = []
while True:
    valor = int(input('Digite um número: '))
    lista.append(valor)
    continua = str(input('Deseja continuar? [S/N] '))
    while continua not in 'SsNn':
        continua = str(input('Deseja continuar? [S/N] '))
    if continua in 'Nn':
        break
lp = []
li = []
for v in lista:
    if v % 2 == 0:
        lp.append(v)
    elif v % 2 == 1:
        li.append(v)
print(f'Os valores digitados foram {lista}')
print(f'Os valores pares foram {lp}')
print(f'Os valores ímpares foram {li}')
