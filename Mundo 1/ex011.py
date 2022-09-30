h = float(input('Qual a altura da sua parede em metros? '))
l = float(input('E a largura? '))
a = h * l
ld = a / 2
print('A área da sua parede é de {}m²'.format(a))
print('seriam necessários {} litros de tinta para pintá-la (considere 1 litro = 2m²)'.format(ld))
