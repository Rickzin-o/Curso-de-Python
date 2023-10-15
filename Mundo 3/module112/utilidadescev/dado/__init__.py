def leiadinheiro(inp):
    money = input(inp)
    while True:
        money = money.strip()
        if money.replace('.', '').replace(',', '').isnumeric():
            break
        else:
            print(f'ERRO! Valor "{money}" não é válido!')
            money = input(inp)
    return float(money.replace(',', '.'))

