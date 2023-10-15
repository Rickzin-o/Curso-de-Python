resposta = 'S'
menor = maior = media = n = 0
while resposta == 'S':
    valor = int(input('Digite um número inteiro: '))
    media += valor
    if n != 0:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    else:
        menor = valor
        maior = valor
    n += 1
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()
print(f'A média de todos os {n} números é de {media/n}')
print(f'O menor valor foi {menor} e o maior foi {maior}.')
