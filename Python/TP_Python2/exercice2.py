a = int(input("Veuillez entrer la première valeur "))
b = int(input("Veuillez entrer la deuxième valeur "))
c = int(input("Veuillez entrer la troisième valeur "))


trieOuNon= False
if a<=b and b<=c:
    trieOuNon=True

if trieOuNon==True:
    print("Les nombres sont triés dans l'ordre croissant")
else : print("Les nombre ne sont pas triés dans l'ordre croissant")