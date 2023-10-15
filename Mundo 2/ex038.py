n1 = int(input('\033[4:35mHora de comparar alguns números! Digite o primeiro valor: '))
n2 = int(input('\033[0:35mDigite o segunda valor: '))
if n1 > n2:
    print('O primeiro valor ({}) é maior!'.format(n1))
elif n1 < n2:
    print('O segundo valor ({}) é maior!'.format(n2))
else:
    print('Os dois valores são iguais.')
