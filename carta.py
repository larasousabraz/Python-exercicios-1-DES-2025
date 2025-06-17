destinatario = input("Digite o e-mail do destinatário: ")
mensagem = input("Digite sua mensagem: ")
remetente = input("Digite seu usuário de e-mail: ")
data = input("Digite a data de envio: ")

print("\n💌 Sua carta 💌")
print(f"\nOlá {destinatario}, \nmensagem: \n\n{mensagem}\n\nAtenciosamente,\n{remetente}")
print(f"\nE-mail enviado de {remetente} para {destinatario}\n Data de envio: {data}, há poucos segundos.")
