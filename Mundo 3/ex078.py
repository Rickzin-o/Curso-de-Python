lista = []
for i in range(5):
    lista.append(int(input(f'Digite um número inteiro: ')))
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)}, nas posições ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(i, end=' - ')
print(f'\nO menor valor digitado foi {min(lista)}, nas posições ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(i, end=' - ')
