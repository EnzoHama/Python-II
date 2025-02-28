idade= int(input("Qual é a sua idade ? "))
tem_carteira= input("Tem carteira de motorista? Digite s para sim e n para não ")
if idade>= 18 and tem_carteira == 's':
    print("Pode dirigir")
else:
    print("Não pode dirigir")