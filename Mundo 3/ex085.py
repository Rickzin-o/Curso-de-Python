numeros = [[], []]
for i in range(1, 8):
    numero = int(input(f'Digite o {i}º valor: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    if numero % 2 == 1:
        numeros[1].append(numero)
print(f'Os valores pares digitados foram {sorted(numeros[0])}')
print(f'Os valores ímpares digitados foram {sorted(numeros[1])}')
