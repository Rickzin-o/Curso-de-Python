def metade(num):
    return num / 2


def dobro(num):
    return num * 2


def aumentar(num, percent):
    return num + (num * (percent / 100))


def diminuir(num, percent):
    return num - (num * (percent / 100))


def moedar(text):
    if type(text) == float:
        p = f'{text:.2f}'
        return f'R${p.replace(".", ",")}'
