import random
print('\033[0:32m-=-\033[m' * 15)
print('\033[0:36mVamos jogar o clássico Pedra Papel e Tesoura!\033[m')
print('\033[0:32m-=-\033[m' * 15)
lista = ['pedra', 'papel', 'tesoura']
pchoic = random.choice(lista)
schoic = str(input('Faça sua escolha e veja se consegue vencer do computador: ')).strip().lower()
if pchoic == schoic:
    print('\033[0:33mEMPATE! Puxa vida parece que escolhemos a mesma coisa!\033[m')
elif pchoic == 'pedra' and schoic == 'tesoura' or pchoic == 'papel' and schoic == 'pedra' or pchoic == 'tesoura' and schoic == 'papel':
    print('\033[0:31mVOCÊ PERDEU! Isso, eu venci! Minha escolha foi {}.'.format(pchoic))
else:
    print('\033[0:32mVOCÊ GANHOU!!! É, parece que você derrotou o computador, minha escolha foi {}.'.format(pchoic))
