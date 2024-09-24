fr = float(input("Veuillez entrer la note de français "))
math = float(input("Veuillez entrer la note de math "))
geo = float(input("Veuillez entrer la note de geo "))
info = float(input("Veuillez entrer la note de informatique "))

sommeNotes= fr+ math+geo+info

moyenneEleve = sommeNotes //4

if moyenneEleve >=16 and moyenneEleve < 20:
    print("Mention très bien!")
else :
    if moyenneEleve >=12 and moyenneEleve <16:
        print("Mention Bien")
    else:
        if moyenneEleve >=8 and moyenneEleve <12:
            print("Mention assez bien")
        else:
            if moyenneEleve >= 4 and moyenneEleve <8:
                print("Mention insuffisant")
            else:
                if moyenneEleve >=0 and moyenneEleve <4:
                    print("Mention nul")

    