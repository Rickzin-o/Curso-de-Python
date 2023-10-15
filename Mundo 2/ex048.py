soma = 0
contador = 0
for i in range(0, 500, 3):
    if i % 2 == 1:
        contador += 1
        soma += i
print(f'Soma dos números impares divisível por 3.\nSão {contador} números '
      f'resultando em {soma}.')
