a= int(input("entrez le prix HT en euros "))
tva = (a * 20) / 100

print("Le prix du produit TTC est de "+str(tva+a)+" dont "+str(tva)+" de TVA")