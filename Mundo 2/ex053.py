string = str(input("Digite uma frase: "))
novastring = string.strip().lower().replace(" ", "")
inverso = novastring[::-1]
print(f'{novastring} ao contrário é {inverso}')
if novastring == inverso:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")
