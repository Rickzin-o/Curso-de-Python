from random import randint

ganhou = True
wins = 0

print('===' * 25)
print('Hora de jogar par ou ímpar!')
print('===' * 25)

while True:
    comp_esc = randint(0, 10)
    my_esc = int(input('Escolha um número: '))
    parimpar = str(input('Você escolhe Par ou Ímpar? [P/I] ')).strip().upper()[0]
    while parimpar not in "PI":
        parimpar = str(input('Você escolhe Par ou Ímpar? [P/I] ')).strip().upper()[0]
    somatoria = comp_esc + my_esc
    resultado = "Par" if somatoria % 2 == 0 else "Impar"
    print('---' * 20)
    print(f'Você escolheu {my_esc} e o computador {comp_esc}. A soma é {somatoria}, quer dizer que deu {resultado}!')
    ganhou = resultado[0] in parimpar
    if ganhou:
        print('Você ganhou! Vamos jogar denovo...')
        print('===' * 25)
        wins += 1
    if not ganhou:
        print('Você perdeu! Mais sorte na próxima.')
        print('===' * 25)
        break
print(f'O jogo acabou, você ganhou {wins} vezes.')
