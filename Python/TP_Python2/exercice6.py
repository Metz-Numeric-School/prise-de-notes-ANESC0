montantHt = int(input("Veuillez entrer le montant HT du produit "))
print("Pour une TVA de 5,5 %, saisissez 1 Pour une TVA de 19,6 %, saisissez 2 Pour une TVA de 33 %, saisissez 3")
codeTva = int(input("Veuillez entrer le code de la TVA "))
montantTTC=0
tva = 0


if codeTva==1:
    montantTTC=montantHt+ ((montantHt*5.5)/ 100)
    tva=5.5
else:
    if codeTva==2:
        montantTTC= montantHt+ ((montantHt*19.6)/100)
        tva=19.6
    else:
        montantTTC=montantHt+((montantHt*33)/100)
        tva=33


print("Le prix HT est de "+str(montantHt)+" €, la TVA est de "+str(tva)+" % et le prix TTC est de "+str(montantTTC)+" €.")