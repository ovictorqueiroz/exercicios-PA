#Elabore um algoritmo que leia dois números, some cinco ao de menor valor, 
#compare os dois valores e mostre o maior.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 < n2:
    c = n1 + 5
    print(f'Variável C: {c}')

    if c > n2:
        print(f'{c} é maior que {n2}')
    
else:
    if n1 == n2:
        print('Os números são iguais.')

    else:
        d = n2 + 5
        print(f'Variável D: {d}')

        if d > n1:
            print(f'{d} é maior que {n1}')

           



    
