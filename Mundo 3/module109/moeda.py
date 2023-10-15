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
