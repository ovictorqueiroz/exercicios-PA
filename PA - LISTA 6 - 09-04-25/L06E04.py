x = int(input('Digite um número para ver sua tabuada: '))

contador = 1

while contador < 11:
    resultado = x * contador
    print(f'{x} X {contador} = {resultado}' )
    contador += 1