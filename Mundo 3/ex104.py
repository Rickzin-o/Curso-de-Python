def leiaInt(inp):
    print(inp, end='')
    a = input()
    while not a.isnumeric():
        print('ERRO! Digite um número inteiro válido!')
        print(inp, end='')
        a = input()
    return a

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
