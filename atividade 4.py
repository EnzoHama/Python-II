salario= float(input("Qual é o seu salário?"))
if salario <=1500:
    print("Você tem 0 de desconto")
    desconto=0
    #print("desconto aplicado no salario", salario)
    
elif salario >1501 and salario <=2500:
    print("Voce tem 5 porcento de desconto")
    desconto4= salario*0.05
    #total=salario - desconto1
    #print("desconto aplicado no salario", total)
elif salario >2501 and salario <=4000:
    print("Você tem 10 porcento de desconto")
    desconto2=salario*0.1
    #total1=salario - desconto
    #print("desconto aplicado no salario", total1)
else:
    print("Você tem 15 porcento de desconto")
    desconto3=salario*0.15
    #total2=salario - desconto
    #print("desconto aplicado no salario", total2)

salario1 = salario - desconto
print(f'Sálario a receber é de R$"{salario1}0,')
print(f'descont aplicado de R$ R$"{salario1}0,')