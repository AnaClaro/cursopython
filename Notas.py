# Solicitando as notas dos alunos ao usuário
while True:
    nota1 = float(input("Digite a nota do 1º Bimestre: "))
    if nota1 <=10 and nota1 >=0:
        break
while True:
    nota2 = float(input("Digite a nota do 2º Bimestre: "))
    if nota2 <=10 and nota2 >=0:
        break
while True:
    nota3 = float(input("Digite a nota do 3º Bimestre: "))
    if nota3 <=10 and nota3 >=0:
        break
while True:
    nota4 = float(input("Digite a nota do 4º Bimestre: "))
    if nota4 <=10 and nota4 >=0:
        break

# Calculando o total e a média

notaTotal = nota1 + nota2 + nota3 + nota4
mediaNota = notaTotal / 4

# Imprimindo resultados

print(f"A nota total é:", notaTotal)
print(f"A média das notas é: {mediaNota: ,.2f}")

# Calculando situação do aluno

if mediaNota >=5:
    print("ALUNO APROVADO.")
elif mediaNota <=3:
    print("ALUNO EM RECUPERAÇÃO")
else:
    print("ALUNO REPROVADO")

print("Fim do ano letivo.")