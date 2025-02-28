#Horas_paga=int(input("Qual é o seu valor pago por hora?"))
#Horas_trabalhadas= int(input("Quantas horas trabalhadas?"))
#salario_brulto= Horas_paga*Horas_trabalhadas
#Toltal_desconto= int(input("Qual é o total de desconto aplicado no salario bruto?"))
#desconto= salario_brulto * (Toltal_desconto / 100)
#salario_liquido= desconto - salario_brulto
#print (salario_liquido)
nht= int(input("insira o numero de horas que voce trabalha.")) 
vph = float(input("Agora, insira o valor pago por hora.")) 
discount = float(input("Insira o valor do desconto em porcentagem: "))  
salario = (vph) * (nht) 
print(salario) 
desconto = salario * (discount/100)  
print("Olá Sr(a) seu Salario bruto e liquido final é de ", salario - desconto) 
 