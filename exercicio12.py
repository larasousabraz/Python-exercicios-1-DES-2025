## Exercício 12 – Validação de Senha
##Peça ao usuário uma senha e verifique se ela contém pelo menos 8 caracteres.  
##Exiba uma mensagem de "Senha válida" ou "Senha muito curta".

senha = input("Digite uma senha: ")

if senha == "":
    print("Senha muito curta")
elif len(senha) >= 8: 
    print("Senha válida")
else:
    print("Senha muito curta")
