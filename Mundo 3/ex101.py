from datetime import datetime

ano = datetime.now().year

def voto(nascimento):
    idade = ano - nascimento
    print(f'Com {idade} anos', end=' ')
    if idade < 16:
        return 'NÃO VOTA'
    elif idade < 18 or idade >= 65:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'

birth = int(input('Em que ano você nasceu? '))
print(voto(birth))
