polyedre = input()  
a = float(input())  

if polyedre == "T":  
    print((2 ** 0.5 / 12) * a ** 3)
elif polyedre == "C": 
    print(a ** 3)
elif polyedre == "O":  
    print((2 ** 0.5 / 3) * a ** 3)
elif polyedre == "D":  
    print(((15 + 7 * (5 ** 0.5)) / 4) * a ** 3)
elif polyedre == "I": 
    print((5 * (3 + (5 ** 0.5)) / 12) * a ** 3)
else:
    print("Polyèdre non connu")