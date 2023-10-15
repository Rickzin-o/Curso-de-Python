soma = 0
n = 0
valor = 0
while valor != 999:
    valor = int(input('Digite um número inteiro [999 para acabar]: '))
    if valor != 999:
        soma += valor
        n += 1
print(f'Você digitou {n} números, e todos juntos somam {soma}.')
