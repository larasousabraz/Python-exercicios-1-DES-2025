# Isabela está desenvolvendo um aplicativo de corrida que calcula a velocidade média do usuário.
# O programa deve receber a distância percorrida e o tempo gasto, calcular a velocidade e indicar se foi 
# lenta (<5 km/h), moderada (5 a 10 km/h) ou rápida (>10 km/h).

distancia = float(input("Digite a distância percorrida: "))
tempo = float(input("Digite o tempo gasto:  "))
v_media = distancia / tempo 
if v_media < 5:
    print("Lento.")
elif v_media >= 5 <= 10:
    print("Moderado.")
else:
    print("Rápido.")
     