

---

### **1. Comprendre le problème**

- **But :** Calculer et afficher les coordonnées des sommets d’un hexagone régulier centré en `(0, 0)` avec un rayon donné. 
- Les sommets sont espacés de 60° (ou PI / 3 radians) en partant de 0° (point situé à droite du centre).
- **Formules pour les coordonnées des sommets :** 

  x= rayon . cos(angle)
  y= rayon . sin (angle)



---

### **2. Étapes à suivre**

1. **Lire et valider l'entrée utilisateur :**
    
    - Utilisez `float(input(...))` pour lire une longueur.
    - Vérifiez qu’elle est strictement positive (`if rayon <= 0`).
2. **Générer les angles des sommets :**
    
    - Les angles (en radians) sont :  0 ; Pi / 3 ; 2Pi /3, Pi ; Pi/3 ; 5Pi/3 
    - On peut utiliser une boucle pour générer ces valeurs.
3. **Calculer les coordonnées des sommets :**
    
    - Pour chaque angle, utilisez les fonctions `math.cos()` et `math.sin()` pour calculer xx et yy.
4. **Afficher les résultats :**
    
    - Affichez chaque couple de coordonnées sur une nouvelle ligne.

---

### **3. Exemple de code**

Voici un exemple commenté pour implémenter ce programme :

```python
import math

# Étape 1 : Lire et valider l'entrée utilisateur
rayon = float(input("Entrez une longueur strictement positive pour le rayon : "))
if rayon <= 0:
    print("Erreur : La longueur doit être strictement positive.")
    exit()

# Étape 2 : Générer les angles et calculer les coordonnées
print("Coordonnées des sommets de l'hexagone :")
for i in range(6):  # Il y a 6 sommets
    angle = i * math.pi / 3  # Angles en radians : 0, π/3, 2π/3, ...
    x = rayon * math.cos(angle)
    y = rayon * math.sin(angle)
    print(f"Sommet {i+1} : ({x:.2f}, {y:.2f})")  # Affichage avec 2 décimales
```

---

### **4. Résultats attendus**

Si l’utilisateur entre 1.01.0 comme rayon, le programme doit afficher quelque chose comme :

```
Coordonnées des sommets de l'hexagone :
Sommet 1 : (1.00, 0.00)
Sommet 2 : (0.50, 0.87)
Sommet 3 : (-0.50, 0.87)
Sommet 4 : (-1.00, 0.00)
Sommet 5 : (-0.50, -0.87)
Sommet 6 : (0.50, -0.87)
```

---

### **Conseils**

- **Validation des entrées :** Ajoutez une gestion des erreurs avec `try...except` pour éviter les saisies non numériques.
- **Précision :** Vous pouvez ajuster l’affichage des coordonnées en modifiant le format (ex. : `f"{x:.3f}"` pour 3 décimales).
- **Graphique :** Si vous souhaitez visualiser l’hexagone, vous pouvez utiliser le module `turtle` ou `matplotlib`.


