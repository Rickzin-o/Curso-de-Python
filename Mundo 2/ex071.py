print('===' * 25)
print('{:^75}'.format('CAIXA ELETRÔNICO'))
print('===' * 25)

sacar = int(input('Quanto você quer sacar? R$'))
n50 = n20 = n10 = n5 = 0

while True:
    while sacar % 5 != 0:
        print('O valor precisa ser um múltiplo de 5! Tente novamente...')
        sacar = int(input('Quanto você quer sacar? R$'))
    if sacar >= 50:
        sacar -= 50
        n50 += 1
    else:
        if sacar >= 20:
            sacar -= 20
            n20 += 1
        else:
            if sacar >= 10:
                sacar -= 10
                n10 += 1
            else:
                if sacar >= 5:
                    sacar -= 5
                    n5 += 1
                else:
                    break
print('Foi sacado:')
if n50 > 0:
    print(f'{n50} cédulas de R$50')
if n20 > 0:
    print(f'{n20} cédulas de R$20')
if n10 > 0:
    print(f'{n10} cédulas de R$10')
if n5 > 0:
    print(f'{n5} cédulas de R$5')

print('---' * 25)
print('Volte sempre! Tenha um bom dia!')
