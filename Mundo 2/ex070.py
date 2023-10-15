maisbarato = ''
pmaisbarato = total = gasto = produtomil = 0

print('{:=^50}'.format(' LEITOR DE PRODUTOS '))

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Preço do produto: R$'))
    if total == 0 or preco < pmaisbarato:
        maisbarato = nome
        pmaisbarato = preco
    total += 1
    gasto += preco
    if preco > 1000:
        produtomil += 1
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar in "Nn":
        break
    print('---' * 20)
print(f'Você registrou {total} produtos, gastando um total de R${gasto:.2f}.')
print(f'O produto mais barato foi o(a) {maisbarato} com um valor de R${pmaisbarato:.2f}.')
print(f'{produtomil} produtos tiveram um valor maior que 1000 reais.')
