a = float(input("prix HT: "))
b = int(input("quantité: "))
c = float(input("TVA (en %): "))

r = (input("Couleur (Bleu,Blanc,Noir): "))
if r == "Bleu" or r == "bleu":
 a = a+1
elif  r =="Blanc" or r =="blanc":
    a = a+2
elif r =="Noir" or r == "noir":
    a = a+3
else :
    print("choisis ta couleur")
    

j = ((a*(c/100)+a)*b)
print ("prix total: ",j)