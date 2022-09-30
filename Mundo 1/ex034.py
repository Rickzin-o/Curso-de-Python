salario = float(input('Digite um salário: R$'))
a1 = (salario / 100) * 10
a2 = (salario / 100) * 15
if salario > 1250:
    # Se o salário for maior que 1250, o aumento é de 10%
    novo = a1 + salario
    print('Você recebeu um aumento de 10%, sendo um aumento de R${:.2f}, passando a receber R${:.2f}'.format(a1, novo))
else:
    # Se o salário for menor ou igual a 1250, o aumento é de 15%
    novo = a2 + salario
    print('Você recebeu um aumento de 15%, sendo um aumento de R${:.2f}, passando a receber R${:.2f}'.format(a2, novo))
