num = int(input('Digite um número: '))

while num < 5:
       print('Entrada inválida. Digite um número maior que 5')
       num =int(input('Digite um número: '))
       
while num > 10:
       print('Entrada inválida. Digite um numero menor que 10.')
       num =int(input('Digite um número: '))
       
print(f'O numero digitado foi {num}')
