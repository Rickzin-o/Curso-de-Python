listagem = ('Caderno', 15, 'Lápis', 1.25, 'Grampeador', 20, 'Estojo', 18, 'Canetas', 6.5, 'Mochila', 240,'Notebook', 1200)
print('==' * 20)
print(f"{'LISTA DE PREÇOS':^40}")
print('==' * 20)
for ind, val in enumerate(listagem):
    if ind % 2 == 0:
        print(f'{val:.<27}', end='....')
    else:
        preco = f'{val:.2f}'
        print(f'R${preco:>7}')
print('--' * 20)
