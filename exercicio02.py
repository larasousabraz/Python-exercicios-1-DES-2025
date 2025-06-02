#  Juliana está coordenando entregas de projetos e precisa calcular o tempo total necessário 
# para finalizar três tarefas: X, Y e Z.
#  Se alguma tarefa estiver com o tempo de entrega negativo, deve-se exibir uma mensagem de 
# erro e não somar o total.

dia_01 = int(input("Digite o tempo necessário para terminar a tarefa X: "))
dia_02 = int(input("Digite o tempo necessário para terminar a tarefa Y: "))
dia_03 = int(input("Digite o tempo necessário para terminar a tarefa Z: "))
soma = dia_03 + dia_02 + dia_03

if dia_01 < dia_02 < 0 or dia_03 < 0:
    print("Erro: tempo determinado para a conclusão das tarefas acabou. ")
else:
    print(f"Tempo total do projeto: {soma} dias")








