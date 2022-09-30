p = float(input('Digite um preço de um produto: '))
d = p / 100 * 5
np = p - d
print('Um desconto de 5% seria R${:.2f} a menos, portanto o valor com desconto é de R${:.2f}'.format(d, np))
