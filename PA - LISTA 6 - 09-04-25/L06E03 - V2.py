x = int(input('Digite um número X: '))
y = int(input('Digite um número Y: '))

if x < y:
    while x < y + 1:
        print(x)
        x += 1 
else:
    while x > y - 1:
        print(x)
        x -= 1
