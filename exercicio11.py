## Exercício 11 – Cálculo de IMC
##Crie um programa que receba o peso (kg) e a altura (m) de uma pessoa e calcule o IMC.  
##Classifique o resultado de acordo com a faixa:  
## Abaixo do peso (< 18.5)  
## Peso normal (18.5 a 24.9)  
## Sobrepeso (25 a 29.9)  
## Obesidade (>= 30)

peso = int(input("Digite seu peso em kg: "))
altura = int(input("Digite sua altura em m: "))
imc = peso / altura * altura
if imc <18.5:
    print("O IMC está abaixo do peso.")
elif imc > 18.6 < 24.9:
    print("O IMC está normal.")
elif imc > 25 < 29.9:
    print("O IMC está sobrepeso.")
else:
    print("O IMC está com índice de obesidade.")
