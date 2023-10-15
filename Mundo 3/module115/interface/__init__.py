from time import sleep


def leiaint(entrada):
    while True:
        try:
            num = int(input(entrada))
            break
        except:
            print('ERRO! Digite um valor inteiro válido.')
    return num


def linhas(text, length=8):
    print('-' * length)
    print(text.center(length))
    print('-' * length)
    sleep(0.5)


def linhaunica(length=30):
    print('-' * length)


def menu(items):
    linhas('MENU PRINCIPAL', 50)
    for idx, item in enumerate(items):
        print(f'{idx + 1} - {item}')
    linhaunica(50)
