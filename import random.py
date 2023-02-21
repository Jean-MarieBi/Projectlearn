import random
indexrand = random.randrange(0,3)
pblist = ["reseau","logiciel","electrique"]
pbindex = pblist[indexrand]
print(indexrand)

if pbindex == "reseau":
    print("valeur 0")
elif pbindex == "logiciel" :
    print("valeur 1")
elif pbindex == "electrique":
    print("valeur 3")
else :
    print("erreur")