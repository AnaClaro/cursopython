# Criando função

def PedirNota(frase):
    while True:
        nota = float(input(frase))
        if nota >=0 and nota <=10:
            break
    return nota

# Solicitando as notas dos alunos ao usuário

nota1bim = PedirNota("Digite a nota do 1º Bimestre: ")
nota2bim = PedirNota("Digite a nota do 2º Bimestre: ")
nota3bim = PedirNota("Digite a nota do 3º Bimestre: ")
nota4bim = PedirNota("Digite a nota do 4º Bimestre: ")

# Calculando a média

mediaNota = (nota1bim + nota2bim + nota3bim + nota4bim) / 4

# Imprimindo resultados

print(f"A média das notas é: {mediaNota:,.2f}")

# Calculando situação do aluno

if mediaNota >=5:
    print("ALUNO APROVADO.")
elif mediaNota >=3:
    print("ALUNO EM RECUPERAÇÃO.")
else:
    print("ALUNO REPROVADO.")

print("Fim do ano letivo.")