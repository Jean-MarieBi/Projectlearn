
a=0
b=1
fibonacci=[]


for i in range(2,20):
    c= a+b
    fibonacci.append(c)
    a=b
    b=c
print(fibonacci)    
#x = int(input("Choisis un chiffre: "))
