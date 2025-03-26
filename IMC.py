sair = 'Não'

while sair == False:
    peso =  float(input("Digite seu peso(KG): "))
    altura = float(input("Digite sua altura(m): "))

    IMC = peso / (altura*altura)

    print (f"Seu IMC é de {IMC:,.2f}")

    sair = input("Deseja sair? Sim/Não")