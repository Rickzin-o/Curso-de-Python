def metade(num=0, form=False):
    """
    Calcula a metade de um valor dado.
    :param num: Valor inteiro ou flutuante.
    :param form: Formata o valor em moeda se verdadeiro.
    :return: Valor calculado.
    """
    res = num / 2
    if form:
        res = moedar(res)
    return res


def dobro(num=0, form=False):
    """
    Calcula o dobro de um valor dado.
    :param num: Valor inteiro ou flutuante.
    :param form: Formata o valor em moeda se verdadeiro.
    :return: Valor calculado.
    """
    res = num * 2
    if form:
        res = moedar(res)
    return res


def aumentar(num=0, percent=10, form=False):
    """
    Aumenta um valor com base na porcentagem dada.
    :param num: Valor inteiro ou flutuante.
    :param percent: Porcentagem de aumento do valor.
    :param form: Formata o valor em moeda se verdadeiro.
    :return: Valor calculado.
    """
    res = num + (num * (percent / 100))
    if form:
        res = moedar(res)
    return res


def diminuir(num=0, percent=10, form=False):
    """
    Reduz um valor com base na porcentagem dada.
    :param num: Valor inteiro ou flutuante.
    :param percent: Porcentagem de redução do valor.
    :param form: Formata o valor em moeda se verdadeiro.
    :return: Valor calculado.
    """
    res = num - (num * (percent / 100))
    if form:
        res = moedar(res)
    return res


def moedar(text):
    """
    Formata um texto em moeda.
    :param text: Texto a ser formatado, precisa ser em números.
    :return: Valor formatado em moeda.
    """
    if type(text) == float:
        p = f'{text:.2f}'
        return f'R${p.replace(".", ",")}'


def resumo(num, percentp, percentm):
    """
    Analisa um número e resume alguns cálculos que podem ser feitos.
    :param num: Valor a ser analisado.
    :param percentp: Porcentagem para o cálculo de aumento.
    :param percentm: Porcentagem para o cálculo de redução.
    :return: Resumo das análises do valor.
    """
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
