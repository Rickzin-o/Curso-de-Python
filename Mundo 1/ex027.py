nome = str(input('Digite seu nome inteiro: ')).strip()
a = nome.split() # Separa os nomes em uma lista
print('Seu primeiro nome é {} e seu último é {}'.format(a[0], a[-1]))
