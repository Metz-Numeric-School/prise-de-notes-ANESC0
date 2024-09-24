a = int(input("Veuillez le nombre de doigts de A "))
b = int(input("Veuillez le nombre de doigts de B "))

somme = a+b


if somme % 2 > 0:
    print("Le joueur B a remporté la partie ")
else :
    print("Le joueur A a remporté la partie ")