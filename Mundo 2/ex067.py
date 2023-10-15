while True:
    n = int(input('De qual valor você quer ver uma tabuada? '))
    print('---' * 25)
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
    print('---' * 25)
print('Número negativo DETECTADO = Programa de tabuada ENCERRADO! Volte sempre!')
