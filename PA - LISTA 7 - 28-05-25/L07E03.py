alunos = []

contadorAlunos = 0

while contadorAlunos < 5:

    nomeAluno = input('Digite o nome do Aluno: ')
    notas = []
    somaNotas = 0

    for i in range(4):
        notaAluno = float(input(f'Digite a nota de {nomeAluno}: '))
        notas.append(notaAluno)
        somaNotas = somaNotas + notaAluno

    mediaAluno = somaNotas / len(notas)

    aluno = {
        "nome": nomeAluno,
        "media": mediaAluno,
        "notas": notas
    }

    alunos.append(aluno)


    contadorAlunos += 1
    print("_"*50)

print('[BOLETIM FINAL]')

for aluno in alunos:
    print(f"Nome: {aluno['nome']} \n"
          f"Notas: {aluno['notas']} \n"
          f"Média Final: {aluno['media']:.1f}")

    if aluno['media'] < 5:
        print('Status: [REPROVADO] \n')
    else:
        print('Status: [APROVADO]\n ')