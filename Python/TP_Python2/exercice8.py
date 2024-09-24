a = int(input("Veuillez entrer une valeur pour a "))
b = int(input("Veuillez entrer une valeur pour b "))

if a==0 and b==0:
    print("L'ensemble des solutions est l'ensemble R")
else :
    if a==0 and b!=0:
        print("L'ensemble des solutions est l'ensemble vide")
    else:
        if a!=0:
            print("La solution est ("+str(-b/a)+")")

