# Diego está acompanhando seu consumo de internet mensal, que tem um limite de 100 GB.
# O programa deve receber o total consumido e avisar se ele ultrapassou o limite.

internet = int(input("Digite o consumo de internet atual: "))
if internet > 100:
    print("O limite de consumo de internet mensal foi ultrapassado.")
else:
    print(f"O limite de consumo tem um armazenamento de {internet}.")