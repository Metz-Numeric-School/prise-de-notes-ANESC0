fr = float(input("Veuillez entrer la note de français "))
math = float(input("Veuillez entrer la note de math "))
geo = float(input("Veuillez entrer la note de geo "))
info = float(input("Veuillez entrer la note de informatique "))

sommeNotes= fr+ math+geo+info

moyenneEleve = sommeNotes //4


print("La moyenne de l'élève est de "+str(moyenneEleve))