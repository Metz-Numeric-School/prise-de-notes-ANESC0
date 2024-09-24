prixUnitaire = int(input("Veuillez entrer le prix unitaire "))

qtCommande = int(input("Veuillez la quantité commandée"))


montantHt= prixUnitaire * qtCommande

remise = (montantHt * 15) / 100

montantHt = montantHt - remise

tva = (montantHt * 20) / 100

montantHt = montantHt + tva

print("Le prix de la commande TTC est égal à "+str(montantHt))