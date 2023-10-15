from datetime import date
genero = input("""Diga seu gênero:
M para masculino
F para feminino
Digite aqui: """)
if genero == 'M':
    ano = int(input('Digite o ano que você nasceu: '))
    anoatual = date.today().year
    a = anoatual - ano
    if a < 18:
        faltam = 18 - a
        print('Você tem {} anos e ainda não deve se alistar no serviço militar'.format(a))
        print('Você terá que se alistar daqui a {} ano(s), no ano de {}'.format(faltam, anoatual + faltam))
    elif a == 18:
        print('Você tem {} anos, está na hora de se alistar no serviço militar!'.format(a))
    else:
        passou = a - 18
        print('Você tem {} anos e já passou da idade para poder se alistar no serviço militar'.format(a))
        print('O prazo pra se alistar passou faz {} ano(s), você tinha que se alistar em {}'.format(passou, anoatual - passou))
elif genero == 'F':
    print('Você não precisa fazer alistamento militar!')
else:
    print('Opção inválida. Certifique se você digitou uma das opções corretamente')
