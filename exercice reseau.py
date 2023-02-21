probleme = input("choisis un probleme a.reseau b.pilote : ")
pbreseau = "0"
pbpilote = "0"

if probleme == "a":
    pbreseau = input("quel probleme reseau: ")
    if pbreseau == "carte reseau":
        print("probleme de carte reseau")
    elif pbreseau == "DHCP" :
        print("probleme DHCP")
    else:
        print("probleme resau inconnu")    

elif probleme == "b":
    pbpilote = input("quelle probleme pilote?: ")
    if pbpilote =="nonreconnu":
        print("reinstalle")
    elif pbpilote == "noninstalle":
        print("chercher le pilote sur internet")
    else:
        print("porbleme pilote non supporter")    
else:
    print("probleme non reconnu")

