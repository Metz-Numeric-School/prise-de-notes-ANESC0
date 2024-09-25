print(r"_______________________________________________")
print(r"             DEBUT DU PROGRAMME                ")
print(r"_______________________________________________")
a = float(input("Entrez un premier nombre flottants "))
b = float(input("Entrez un deuxième nombre flottants "))

somme = a + b
difference = a -b
produit = a*b

print(f" résultat de la somme : {somme}")
print(f" résultat de la soustraction : {difference}")
print(f" résultat de la multiplication : {produit}")

# quotient

if b==0:
    print("Erreur: division par zéro")
else:
    quotient = a/b
    print(f" résultat de la division : {quotient}")


print(r"_______________________________________________")
print(r"             FIN DU PROGRAMME                ")
print(r"_______________________________________________")
