l = []
while True:
    valor = int(input('Digite um número inteiro: '))
    l.append(valor)
    go = str(input('Deseja continuar? [S/N] '))
    while go not in 'NnSs':
        go = str(input('Deseja continuar? [S/N] '))
    if go in 'Nn':
        break
print(f'Foram digitados um total de {len(l)} números.')
l.sort(reverse=True)
print(f'Os valores em ordem decrescente são {l}.')
value5 = 'SIM' if 5 in l else 'NÃO'
print(f'O valor 5 foi digitado? {value5}')
