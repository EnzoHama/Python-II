# primeira tentativa CA=print("1:candidato A")
#CB=print("2:candidato B")
#CC=print("3:candidato C")
#A=0
#B=0
#C=0
#pergunta=input(" Vote na letra maiuscula do candito que você quer votar: ")
#if pergunta=='A':
 #  print("Você voto no candidato A")
 #  T=A+1
  # print ("candidato A está com", T, "voto" )
 #  print ("candidato B está com 0 voto" )
 #  print ("Candidato C está com 0 voto" )
#elif pergunta=='B':
   # print ("Você voto no candidato B")
    #Ta=B+1
    #print ("candidato A está com 0 voto" )
    #print ("candidato B está com", Ta,"voto")
    #print ("Candidato C está com 0 voto"  )
#else:
    #print("Você votou no candidato C")
    #Tc=C+1
    #print ("candidato A está com 0 voto"  )
    #print ("candidato B está com 0 voto" )
    #print ("Candidato C está com", Tc, "voto")
#print ("candidato A está com 0 voto",{T},"voto")
#print ("candidato B está com 0 voto",{Ta},"voto")
#print ("Candidato C está com", {Tc}, "voto")
def urna_eletronica():
    senha_correta = "1234"
    candidatos = {"1": "Candidato A", "2": "Candidato B", "3": "Candidato C"}
    votos = {"Candidato A": 0, "Candidato B": 0, "Candidato C": 0}

    print("Bem-vindo à urna eletrônica!")

    senha = input("Digite a senha para acessar a urna: ")
    if senha != senha_correta:
        print("Senha incorreta! Acesso negado.")
        return

    while True:
        print("\nCandidatos:")
        for numero, nome in candidatos.items():
            print(f"{numero}: {nome}")

        voto = input("Digite o número do seu candidato (ou 'sair' para encerrar): ")
        if voto == "sair":
            break
        elif voto in candidatos:
            votos[candidatos[voto]] += 1
            print(f"Voto registrado para {candidatos[voto]}.")
        else:
            print("Opção inválida! Tente novamente.")

    print("\nResultado da votação:")
    for candidato, contagem in votos.items():
        print(f"{candidato}: {contagem} votos")

urna_eletronica()
