contador = 0
notas = []
media = []

while contador < 4:

    nota = float(input('Digite a nota do aluno: '))

    notas.append(nota)

    media = sum(notas) / 4

    contador += 1


print(notas)
print(media)
