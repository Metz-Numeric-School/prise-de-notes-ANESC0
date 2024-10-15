tempAmbiante= int(input("Veuillez entrer la température ambiante "))
tempBassRef= int(input("Veuillez entrer la température des bassins de refroidissement "))
difTem = tempAmbiante-tempBassRef

if difTem < 20 or difTem>40:
    print("   ^   ")
    print(r" / ! \   DANGER ! ")
    print(r"/ ___ \ ")
else:
    print("It's Okay!")
