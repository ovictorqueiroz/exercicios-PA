n1 = int(input('Digite um número: '))

while n1 >= 5:
    print('Digite um número menor que 5 para continuar')
    n1 = int(input('Digite um número: '))

if n1 % 2 == 0:
    while n1 <= 20:
        print(n1)
        n1 += 2
else:
    n1 += 1
    while n1 <= 20:
        print(n1)
        n1 += 2
