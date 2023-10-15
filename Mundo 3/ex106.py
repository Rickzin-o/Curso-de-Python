from time import sleep

def helpsystem(method):
    s = f"Acessando manual de '{method}'"
    sleep(0.2)
    print('-' * (26 + len(method)))
    print(f'  {s}  ')
    print('-' * (26 + len(method)))
    sleep(0.8)
    return help(method)

print('=' * 24)
print(f'{"Sistema PyHelp":^24}')
print('=' * 24)

while True:
    method = input('Nome da Função ou Biblioteca > ')
    if method.strip().lower() == 'fim':
        break
    helpsystem(method)
    sleep(1)
print('=' * 8)
print('  FIM!')
print('=' * 8)
