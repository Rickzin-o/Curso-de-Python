from time import sleep
print('==' * 25)
print('\033[0:34mBem-vindo ao Analisador de Triângulos versão 2.0!\033[m')
print('==' * 25)
sleep(1)
a = float(input('Digite o comprimento em cm de uma linha: '))
b = float(input('Digite o comprimento de uma segunda linha: '))
c = float(input('Digite uma terceira linha: '))
print('\033[0:33mVamos ver...\033[m')
sleep(1)
if a - c < b < a + c and b - c < a < b + c and a - b < c < b + a:
    print('\033[0:32mEssas linhas podem formar um triângulo!\033[m')
    if a == b == c:
        print('Aliás, esse é um triângulo \033[0:34mequilátero.\033[m')
    elif a == b or a == c or b == c:
        print('Aliás, esse é um triângulo \033[0:34misóceles.\033[m')
    else:
        print('Aliás, esse é um triângulo \033[0:34mescaleno.\033[m')
else:
    print('\033[0:31mEssas linhas não podem formar um triângulo.\033[m')
