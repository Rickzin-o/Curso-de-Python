def metade(num, form=False):
    res = num / 2
    if form:
        res = moedar(res)
    return res


def dobro(num, form=False):
    res = num * 2
    if form:
        res = moedar(res)
    return res


def aumentar(num, percent, form=False):
    res = num + (num * (percent / 100))
    if form:
        res = moedar(res)
    return res


def diminuir(num, percent, form=False):
    res = num - (num * (percent / 100))
    if form:
        res = moedar(res)
    return res


def moedar(text):
    if type(text) == float:
        p = f'{text:.2f}'
        return f'R${p.replace(".", ",")}'


def resumo(num, percentp, percentm):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado":<20}{moedar(num):<10}')
    print(f'{"Dobro do preço":<20}{dobro(num, True):<10}')
    print(f'{"Metade do preço":<20}{metade(num, True):<10}')
    aumento = f'{percentp}% de aumento'
    reducao = f'{percentm}% de redução'
    print(f'{aumento:<20}{aumentar(num, percentp, True):<10}')
    print(f'{reducao:<20}{diminuir(num, percentm, True):<10}')
    print('-' * 30)
