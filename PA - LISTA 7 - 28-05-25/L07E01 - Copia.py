contador = 0
notas = []
media = 0

while contador < 4:

    nota = float(input('Digite a nota do aluno: '))
    
    notas.append(nota)
    
    media = media + notas[contador]
    
    contador += 1

media = media / len(notas)
print(notas)
print(media)
print("fim")

