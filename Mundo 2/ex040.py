from time import sleep
print('--' * 10)
print('\033[0:34mCalculador de médias\033[m')
print('--' * 10)
not1 = float(input('Digite sua primeira nota aqui: '))
not2 = float(input('Digite sua segunda nota aqui: '))
med = (not1 + not2) / 2
print('\033[0:36mSua média é...\033[m')
sleep(2)
if med < 5:
    print('{:.2f}! \033[0:31mREPROVADO! Estude mais da próxima vez...\033[m'.format(med))
elif 7 > med >= 5:
    print('{:.2f}! \033[0:33mRECUPERAÇÃO! Você não foi reprovado, mas podia ser melhor.\033[m'.format(med))
else:
    print('{:.2f}! \033[0:32mPASSOU! Sua nota foi suficiente para passar, parabéns!\033[m'.format(med))
