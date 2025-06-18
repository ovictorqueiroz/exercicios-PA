user_num = int(input('Digite um número: '))

while user_num >= 10:
    print('Digite um número menor que 10')
    user_num = int(input('Digite um número: '))
    
print(f'O número digitado foi {user_num}')
