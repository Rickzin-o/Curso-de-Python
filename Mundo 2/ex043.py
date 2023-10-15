print('\033[0:34mVamos calcular índice de massa corporal.\033[m')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Seu IMC é de {:.1f} e você está na categoria ABAIXO DO PESO'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é de {:.1f} e você está na categoria PESO IDEAL'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é de {:.1f} e você está na categoria SOBREPESO'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é de {:.1f} e você está na categoria OBESIDADE'.format(imc))
else:
    print('Seu IMC é de {:.1f} e você está na categoria OBESIDADE MÓRBIDA, cuidado!'.format(imc))
