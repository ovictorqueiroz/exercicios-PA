print('Inicio')

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

soma = n1 + n2

if soma < 20:
    n1 = n1 * 10
    n2 = n2 * 10
    
    print(n1)
    print(n2)

print('Fim.')
