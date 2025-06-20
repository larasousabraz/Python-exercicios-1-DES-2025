# Renata quer solicitar um financiamento, mas precisa verificar se cumpre os critérios:

# Salário mensal acima de R$ 3.000,00
# A parcela não pode ser maior que 35% do salário

salario = float(input("Digite o salário mensal: "))
parcela = int(input("Digite o percentual que o financiamento ocupa no salário: "))

if  salario > 3000 or parcela > 35:
    print("Infelizmente, o financiamento não pode ser realizado.")
else:
    print("O financiamento pode ser realizado.")
