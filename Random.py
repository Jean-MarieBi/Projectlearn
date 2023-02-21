import random
nb_secret= random.randrange(1,1000)
nb_joueur=-1

while nb_secret != nb_joueur:
    nb_joueur = int(input("choisis un nombre?: "))
    if nb_secret > nb_joueur:
        print("plus grand")
    elif nb_secret < nb_joueur:
        print("plus petit")       
print("bravo tu as trouver")