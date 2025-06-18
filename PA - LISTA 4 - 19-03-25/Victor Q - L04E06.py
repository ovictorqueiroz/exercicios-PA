#Desenvolva um algoritmo que leia dois números e mostre os números em 
#ordem crescente.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    o1 = n2
    o2 = n1
else:
    o1 = n1
    o2 = n2
    
print(o1)
print(o2)
