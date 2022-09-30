# Nota do futuro: Eu podia ter feito de forma mais prática
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Verificações do menor número
menor = a
if b >= a or b >= c:
    pass
else:
    menor = b
if c >= a or c >= b:
    pass
else:
    menor = c

# Verificações do maior número    
maior = b
if a <= b or a <= c:
    pass
else:
    maior = a
if c <= b or c <= b:
    pass
else:
    maior = c

print('O menor número entre eles é o {}'.format(menor))
print('O maior número entre eles é o {}'.format(maior))
