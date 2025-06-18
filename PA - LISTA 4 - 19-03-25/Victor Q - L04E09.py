#Desenvolva um algoritmo que leia quatro números, some os dois primeiros e subtraia os dois últimos, some os resultados e mostre a seguinte mensagem,
#resultado maior que dez, caso a afirmação esteja correta ou resultado menor ou igual a dez.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))

resultado1 = n1 + n2
print(f'Resultado 1: n1 + n2 =  {resultado1}')

resultado2 = n3 - n4
print(f'Resultado 2:n3 - n4 =  {resultado2}')

resultado3 = resultado1 + resultado2

if resultado3 > 10:
    print(f'O resultado das operações é maior que 10. {resultado3}')
else:
    print(f'O resultado das operações é menor ou igual a 10. {resultado3}')
