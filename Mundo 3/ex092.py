import datetime

anoatual = datetime.date.today().year
ficha = dict()

ficha['Nome'] = str(input('Nome: '))
ficha['Idade'] = anoatual - int(input('Ano de nascimento: '))
ficha['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if ficha['CTPS'] != 0:
    ficha['Contratação'] = int(input('Ano de contratação: '))
    ficha['Salário'] = int(input('Salário: R$'))
    ficha['Aposentadoria'] = (ficha['Contratação'] - (anoatual - ficha['Idade']))+35
print('=' * 40)
for k, v in ficha.items():
    print(f'{k} foi registrado como {v}')
    
