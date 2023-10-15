tup = (int(input('Digite um número inteiro: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite um último número: ')))
print(f'Você digitou os valores {tup}')
print(f'O valor 9 apareceu {tup.count(9)} vezes')
if 3 in tup:
    print(f'O valor 3 apareceu na {tup.index(3)+1}ª posição.')
else:
    print(f'O valor 3 não foi digitado')

print('Os valores pares digitados foram', end=' ')
for n in tup:
    if n % 2 == 0:
        print(n, end=' ')
