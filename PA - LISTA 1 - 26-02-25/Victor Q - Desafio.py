num = int(input('Insira um valor: '))

divisor = int(input('Insira um divisor: '))

resposta1 = int(num // divisor)
resposta2 = num / divisor

resto = int((resposta2 - resposta1) * divisor)

print(f'Resposta: {resposta1}')
print(f'Resto: {resto}')

