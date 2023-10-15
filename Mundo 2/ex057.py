secsu = str(input('Digite seu gênero [M/F]: ')).upper().strip()[0]
while secsu not in 'FM':
    secsu = str(input('Valor inválido! Digite novamente [M/F]: ')).upper().strip()
if secsu == 'M':
    print('Você é do sexo masculino.')
elif secsu == 'F':
    print('Você é do sexo feminino.')
