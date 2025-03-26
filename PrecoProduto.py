'''1 - Montar um programa que solicite 3 preços de um produto. - FEITO
---2 - O sistema deverá calcular a média de preço.' -          - FEITO
---3 - Os valores digitados não poderão ser valores negativos. - FEITO'''

def validapreco(valorp):
    while True:
        Preco = float(input(valorp))
        if Preco >=0:
            break
    return Preco

# Solicitando os preços dos produtos para o usuário

preco1 = validapreco("Digite o 1º preço: ")
preco2 = validapreco("Digite o 2º preço: ")
preco3 = validapreco("Digite o 3º preço: ")

# Calculando a média de preços dos produtos

mediaPreco = (preco1 + preco2 + preco3) / 3

# Imprimindo o a média de preço do produto

print(f"A média de preço do produto é de: R${mediaPreco:,.2f}")