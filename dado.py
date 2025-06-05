import random 
input("Pressione Enter para lançar o dado.")
resultado = random.randint (1,10)
print (f"O dado rolou: {resultado}" );
if resultado > 6:
    print("QUE ISSO MN, seloko tu tem sorte hein")
elif resultado < 2:
    print("caraca KKKKKKK tu é ruim hein tenta de novo aí");