import module107.moeda as moeda

p = float(input('Digite um preço: R$'))
print(f'A metade desse preço é {moeda.metade(p)}')
print(f'O dobro desse preço é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(p, 13)}')
