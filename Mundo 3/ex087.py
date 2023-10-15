matriz = [[], [], []]
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Digite um valor inteiro para [{i}, {j}]: ')))
print('--' * 40)
somapar = somatres = 0
for linha in matriz:
    for i, valor in enumerate(linha):
        print(f'[ {valor} ]', end='')
        if i == 2:
            somatres += valor
        if valor % 2 == 0:
            somapar += valor
    print('')
print(f'A soma dos valores pares digitados é {somapar}')
print(f'A soma dos valores da terceira coluna é {somatres}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
