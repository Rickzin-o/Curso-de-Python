from time import sleep
print('=' * 65)
print('\033[0:33mVocê vai comprar uma casa! Está na hora de fazer alguns cálculos.\033[m')  # apresentação legal
print('=' * 65)
sleep(1)
casa = float(input('Digite o valor da casa que você deseja comprar: R$'))
salario = float(input('Digite o valor de seu salário: R$'))
anos = float(input('Em quantos anos você vai pagar a casa? '))
prestmensal = casa / (anos * 12)
partsal = (salario / 100) * 30
print('\033[0:36mPROCESSANDO...\033[m')
sleep(2)
if prestmensal <= partsal:
    print('\033[0:34mVocê pagará por mês um valor de R${:.2f} por {} anos, aproveite a casa!\033[m'.format(prestmensal, anos))
else:
    print('\033[0:31mOPS! Parece que a prestação mensal excedeu 30% do seu salário, então você não pode comprar a casa\033[m')
