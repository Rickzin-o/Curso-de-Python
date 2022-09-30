frase = input('Digite um frase: ').upper().strip()
print('A letra "A" aparece {} vezes nessa frase'.format(frase.count('A')))
print('A primeira vez que ela aparece é no caractere {}'.format(frase.find('A')+1))
print('A última vez que ela aparece é no caractere {}'.format(frase.rfind('A')+1))
