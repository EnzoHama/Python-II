CA=print("1:candidato A")
CB=print("2:candidato B")
CC=print("3:candidato C")
A=0
B=0
C=0
pergunta=input(" Vote na letra maiuscula do candito que você quer votar: ")
if pergunta=='A':
   print("Você voto no candidato A")
   T=A+1
   print ("candidato A está com", T, "voto" )
   print ("candidato B está com 0 voto" )
   print ("Candidato C está com 0 voto" )
elif pergunta=='B':
    print ("Você voto no candidato B")
    Ta=B+1
    print ("candidato A está com 0 voto" )
    print ("candidato B está com", Ta,"voto")
    print ("Candidato C está com 0 voto"  )
else:
    print("Você votou no candidato C")
    Tc=C+1
    print ("candidato A está com 0 voto"  )
    print ("candidato B está com 0 voto" )
    print ("Candidato C está com", Tc, "voto")
#print ("candidato A está com 0 voto",{T},"voto")
#print ("candidato B está com 0 voto",{Ta},"voto")
#print ("Candidato C está com", {Tc}, "voto")