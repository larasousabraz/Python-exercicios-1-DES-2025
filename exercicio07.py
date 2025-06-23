# Uma empresa quer avaliar seus colaboradores com base em três metas atingidas.
# O programa deve calcular a média das três avaliações e exibir:

# Aprovado (>=7)
# Em treinamento (>=5 e <7)
# Reprovado (<5)

meta1 = int(input("Digite o índice da meta 1: "))
meta2 = int(input("Digite o índice da meta 2: "))
meta3 = int(input("Digite o índice da meta 3: "))
indice = meta1 + meta2 + meta3 / 3

if indice >=7:
    print("Parabéns, você foi aprovado!")
elif indice >=5 <7:
    print("Você está em etapa de treinamento.")
else:
    ("Ah não!  Parece que você não foi aprovado.")