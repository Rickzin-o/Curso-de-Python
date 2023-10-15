num = int(input("Digite um número: "))
divisivel = []
for i in range(1, num+1):
    if num % i == 0:
        divisivel.append(i)
if 1 in divisivel and num in divisivel and len(divisivel) == 2:
    print("Este número é primo!")
else:
    print(f"Este número é divisivel por {len(divisivel)} números e não é primo.")
