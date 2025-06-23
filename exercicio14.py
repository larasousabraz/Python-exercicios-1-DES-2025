## Exercício 14 – Sistema de Descontos
## Loja oferece os seguintes descontos:  
## Compras acima de R$ 500,00 têm 10%  
## Acima de R$ 300,00 têm 5%  
## Menor ou igual a R$ 300,00 não têm desconto

valor = float(input("Digite o valor da compra: "))

if valor > 500:
    desconto = valor * 0.10
elif valor > 300:
    desconto = valor * 0.05
else:
    desconto = 0

valor_final = valor - desconto

print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
