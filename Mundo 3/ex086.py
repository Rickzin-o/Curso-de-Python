matriz = [[], [], []]
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Digite um valor inteiro para [{i}, {j}]: ')))
print('--' * 40)
for linha in matriz:
    for valor in linha:
        print(f'[{valor:^5}]', end='')
    print('')
