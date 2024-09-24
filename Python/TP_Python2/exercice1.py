# initialiser le quotient
divisePar = 0

# demander la note de la matiere en francais
fr = float(input("Veuillez entrer la note de français "))

# puis demander son coefficient
coef = float(input("Veuillez entrer le coefficient de la matière "))
fr= fr*coef
divisePar +=coef

# math

math = float(input("Veuillez entrer la note de math "))
coef = float(input("Veuillez entrer le coefficient de la matière "))
math= math*coef
divisePar +=coef
#geo

geo = float(input("Veuillez entrer la note de geo "))
coef = float(input("Veuillez entrer le coefficient de la matière "))
geo = geo*coef
divisePar +=coef

#info

info = float(input("Veuillez entrer la note de informatique "))
coef = float(input("Veuillez entrer le coefficient de la matière "))
info= info*coef
divisePar +=coef

# on divise la somme totale par le nombre total de notes

print("La moyenne de l'élève est de "+str((fr+math+geo+info)//divisePar))