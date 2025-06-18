#7. Crie um algoritmo que leia três números e mostre seus valores em ordem 
#crescente.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

menor = n1

domeio = 0

maior = 0

if n2 < menor:
    menor = n2

    if n3 < menor:
        menor = n3
        domeio = n2
        maior = n1 
    else:
        menor = n2
        domeio = n3
        maior = n1

else:
    maior = n2

    if n3 > n1:
        maior = n3
        domeio = n2
        menor = n1
        
    else:
        maior = n2
        domeio = n3
        menor = n1

print(menor)
print(domeio)
print(maior)

