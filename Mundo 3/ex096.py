print('  Controle de Terrenos')
print('========================')


def area(lar, com):
    a = lar * com
    print(f'A área do terreno {lar:.1f}x{com:.1f} é de {a}m²')


l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
