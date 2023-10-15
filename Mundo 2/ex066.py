soma = count = 0
while True:
    num = int(input('Digite um número inteiro [999 para parar]: '))
    if num == 999:
        break
    soma += num
    count += 1
print(f'Você digitou {count} números, somando {soma}.')
