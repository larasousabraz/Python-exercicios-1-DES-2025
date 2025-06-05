# Rafael trabalha com armazenamento de grãos e precisa garantir que a umidade do ar no local não ultrapasse 70%.
# Escreva um programa que receba o valor da umidade atual e exiba um alerta se estiver acima do limite.

umidade = int(input("Digite o valor da umidade do local:"))
if umidade > 70:
    print("A umidade ultrapassou o limite permitido. ")
else:
    print("A umidade está normal.")
