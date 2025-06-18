#Elabore um algoritmo que leia um número, se ele for maior que dez, some 
#cinco ao seu valor, se for menor ou igual, some 20 e mostre se o resultado for 
#maior que vinte e cinco.

n1 = int(input('Digite um numero: '))

if n1 > 10:
    n1 = n1 + 5

else:
    n1 = n1 + 20
        
if n1 > 25:
    print(n1)
