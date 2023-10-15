def leiaInt(entrada):
    while True:
        try:
            num = int(input(entrada))
            break
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse valor.')
            num = 0
            break
        except:
            print('ERRO! Digite um valor inteiro válido.')
    return num


def leiaFloat(entrada):
    while True:
        try:
            num = float(input(entrada))
            break
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse valor.')
            num = 0
            break
        except:
            print('ERRO! Digite um valor real válido.')
    return num


inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}.')
