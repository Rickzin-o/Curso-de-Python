from datetime import date

ano = int(input('Digite um ano, digite 0 para o ano atual: '))
if ano == 0:
    # Pega o ano atual
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # Conferindo se o ano é bissexto
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
