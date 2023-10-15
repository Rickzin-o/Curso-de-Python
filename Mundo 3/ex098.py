from time import sleep


def contador(inicio, fim, passo):
    print('-' * 40)
    print(f'Contagem de {inicio} a {fim} contando de {passo} em {passo}')

    if passo == 0:
        passo = 1
    passo = max(passo, -passo)
    c = inicio
    if inicio < fim:
        while c <= fim:
            print(c, end=' ')
            c += passo
            sleep(0.2)
    else:
        while c >= fim:
            print(c, end=' ')
            c -= passo
            sleep(0.2)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 40)

print('Chegou sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fi = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fi, pas)
