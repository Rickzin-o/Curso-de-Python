num = int(input('Digite um número inteiro: '))
print('''Digite um valor para escolher o tipo de conversão:
1 - Converte para Binário
2 - Converte para Octal
3 - Converte para Hexadecimal''')
conversor = int(input('Você irá converter pará: '))
if conversor == 1:
    print('{} convertido na base BINÁRIA equivale a {}'.format(num, str(bin(num)[2:])))
elif conversor == 2:
    print('{} convertido na base OCTAL equivale a {}'.format(num, str(oct(num)[2:])))
elif conversor == 3:
    print('{} convertido para a base HEXADECIMAL equivale a {}'.format(num, str(hex(num)[2:])))
else:
    print('OPÇÃO INVÁLIDA!')
