#Elabore um algoritmo que leia três números some cinco ao menor valor e mostre o resultado.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

menor = n1

if n2 < menor:
    menor = n2

if n3 < menor:
    menor = n3

resultado = menor + 5

print(f'O menor número digitado foi {menor}, que somado a 5, é {resultado} ')