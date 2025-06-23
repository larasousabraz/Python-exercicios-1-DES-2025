# Bianca está programando o controle de acesso a uma plataforma que só funciona entre 9h e 21h.
# O programa deve receber a hora atual (formato 24h) e informar se o acesso é permitido.

horario = int(input("Digite o horário atual (24h): "))
if horario < 9 > 21:
    print("A plataforma será executada em alguns instantes.")
else:
    print("A plataforma não pode ser executada agora.")