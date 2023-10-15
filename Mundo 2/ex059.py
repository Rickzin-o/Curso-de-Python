print('Bem-vindo à mini calculadora!')
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
print('===' * 25)
executar = 0
while executar != 5:
    print("""Digite:
[1] para somar os valores
[2] para multiplicar os valores
[3] para conferir qual o maior
[4] para digitar novos valores
[5] para fechar o programa""")
    executar = int(input('O que você gostaria de fazer? '))
    if executar == 1:
        print(f'A soma dos valores é {valor1 + valor2}')
    elif executar == 2:
        print(f'O produto dos valores é {valor1 * valor2}')
    elif executar == 3:
        if valor1 > valor2:
            print(f'O maior valor é {valor1}')
        elif valor2 > valor1:
            print(f'O maior valor é {valor2}')
        elif valor1 == valor2:
            print('Os dois valores são iguais')
    elif executar == 4:
        valor1 = int(input('Digite um valor: '))
        valor2 = int(input('Digite outro valor: '))
    elif executar == 5:
        pass
    else:
        print('Opção inválida!')

    if executar != 5:
        print('---' * 10)
print('===' * 25)
print('Obrigado por usar nosso serviço!')
