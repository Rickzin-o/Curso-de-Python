cidade = str(input('Digite o nome de sua cidade: ')).strip().capitalize()
b = cidade.split()
print('Essa cidade começa com "Santo"? {}'.format('Santo' in b[0]))
# True se começar, False caso o contrário
