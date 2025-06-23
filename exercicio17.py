## Exercício 17 – Conversão de Temperaturas
## Peça ao usuário uma temperatura em Celsius e converta para Fahrenheit.  
## Fórmula: F = C × 1.8 + 32

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius * 1.8 + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")
