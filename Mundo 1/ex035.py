from time import sleep

print('-=-' * 15)
print('Bem-vindo ao analisador de triângulos!')
print('-=-' * 15)
sleep(1)
a = float(input('Digite o comprimento em cm de uma linha: '))
b = float(input('Digite o comprimento de uma segunda linha: '))
c = float(input('Digite o comprimento da terceira linha: '))
print('Deixe-me ver...')
sleep(1)
if a - c < b < a + c and b - c < a < b + c and a - b < c < a + b:
    print('Essas linhas podem formar um triângulo!')
else:
    print('Essas linhas não podem formar um triângulo.')
