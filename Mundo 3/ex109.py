import module109.moeda as moeda

p = float(input('Digite um preço: R$'))
print(f'A metade desse preço é {moeda.metade(p, True)}')
print(f'O dobro desse preço é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(p, 13, True)}')
