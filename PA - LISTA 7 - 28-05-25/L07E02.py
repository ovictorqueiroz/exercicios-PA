from time import sleep

index = 0
numeros = []

while index < 5:
    num = int(input("Digite um número: "))
    numeros.append(num)
    index += 1

print(f'Os números lidos foram: {numeros}')
print('Ordenando números...')

mudanca = True
nMudancas = 0

while mudanca:
    mudanca = False
    for i in range(len(numeros) - 1):
        if numeros[i] > numeros[i + 1]:
            numeros[i], numeros [i +1] = numeros[i + 1], numeros [i]
            
            mudanca = True
            nMudancas += 1
            print(f'{nMudancas} mudanças feitas')
            sleep(2)


print(f'Os números estão ordenados:')
print(numeros)