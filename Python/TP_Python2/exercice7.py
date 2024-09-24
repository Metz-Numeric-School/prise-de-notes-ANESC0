montantTTC = int(input("Veuillez entrer le montant TTC du produit "))


if montantTTC > 500 and montantTTC <1000:
    montantTTC = montantTTC * (1 - 2/100)
else :
    if montantTTC >= 1000 and montantTTC <= 2000:
        montantTTC= montantTTC * (1 - 5/100)
    else:
        if montantTTC > 2000:
            montantTTC=montantTTC * (1-10/100)


print("Le montant TTC avec ou sans la remise est de "+str(montantTTC))