#Desenvolva um algoritmo (fluxograma e pseudocódigo) que leia dois números e 
#mostre o menor. 

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 < n2:
    print(f'{n1} é o menor número.')
    
else:
    if n1 == n2:
        print('Os números são iguais.')

    else:
        print(f'{n2} é o menor')
    
