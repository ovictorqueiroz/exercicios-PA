n1 = int(input('Digite um número: '))
while n1 <= 10:
    print('Digite um número maior que 10 para continuar')
    n1 = int(input('Digite um número: '))

n2 = int(input('Digite outro número: '))
while n2 >= 5:
    print('Digite um número menor que 5 para continuar')
    n2 = int(input('Digite outro número: '))

print(f'Os números digitados foram {n1} e {n2}')
print('fim')
