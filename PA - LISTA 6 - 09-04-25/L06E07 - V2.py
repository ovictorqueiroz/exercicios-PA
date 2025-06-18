n1 = int(input('Digite um número maior que 10: '))
n2 = int(input('Digite um número menor que 5: '))

while n1 <= 10:
        print('Entrada inválida. Tente novamente')
        n1 = int(input('Digite um número maior que 10: '))
        
while n2 >= 5:
        print('Entrada inválida. Tente novamente')
        n2 = int(input('Digite um número menor que 5: '))

print(f'Os números digitados foram {n1} e {n2}')
print('fim')
