a = float(input("prix HT: "))
b = int(input("quantité: "))
c = float(input("TVA (en %): "))
j = 0
j = ((a*(c/100)+a)*b)
print ("prix total: ",j)