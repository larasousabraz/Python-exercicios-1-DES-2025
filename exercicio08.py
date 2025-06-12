# Talita está simulando o custo de frete para sua loja virtual. O valor depende da distância:

# Até 50 km: R$ 5,00
# De 51 a 150 km: R$ 15,00
# Acima de 150 km: R$ 25,00

frete = int(input("Insira aqui a distância do frete: "))
if frete >= 50:
    print("O valor do frete é de R$ 5,OO.")
elif frete >51 <150:
    print("O valor do frete é de R$ 15,00.")
else:
    print("O valor do frete é de R$ 25,00.")