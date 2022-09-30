nome = str(input('Digite seu nome inteiro: ')).strip()
print(nome.upper()) # Nome em maiúsculo
print(nome.lower()) # Nome em minúsculo
print('Seu nome inteiro sem espaço tem {} letras'.format(len(nome.replace(' ', ''))))
a = nome.split() # Separa os nomes
print('Seu primeiro nome é {} e ele tem {} letras'.format(a[0], len(a[0])))
