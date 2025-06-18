x = int(input('Digite um número X: '))
y = int(input('Digite um número Y: '))

if x < y:
    num_inicial = x
    num_final = y
else:
    num_inicial = y
    num_final = x

while num_inicial < num_final + 1:
    print(num_inicial)
    num_inicial += 1