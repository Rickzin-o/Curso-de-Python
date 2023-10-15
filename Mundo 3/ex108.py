import module108.moeda as moeda

p = float(input('Digite um preço: R$'))
print(f'A metade desse preço é {moeda.moedar(moeda.metade(p))}')
print(f'O dobro desse preço é {moeda.moedar(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moedar(moeda.aumentar(p, 10))}')
print(f'Diminuindo 13%, temos {moeda.moedar(moeda.diminuir(p, 13))}')
