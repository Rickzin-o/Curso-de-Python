import random
from time import sleep

palpites = []

print('--' * 20)
print(f'{"JOGA NA MEGA SENA":^40}')
print('--' * 20)
njogos = int(input('Quantos jogos você quer que eu palpite? '))
print(f'====== SORTEANDO {njogos} JOGOS ======')

for i in range(njogos):
    palpites.append([])
    for j in range(6):
        while True:
            numero = random.randint(1, 60)
            if numero not in palpites[i]:
                palpites[i].append(numero)
                break

for i, p in enumerate(palpites):
    print(f'Jogo {i+1}: {sorted(p)}')
    sleep(0.5)
