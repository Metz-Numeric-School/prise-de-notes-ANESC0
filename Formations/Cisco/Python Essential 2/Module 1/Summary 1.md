
----
## Résumé de la section 1.1.9

### 1. Importer un module en entier
- Pour importer un module en entier, utilise l'instruction **`import module_name`**. Tu peux importer plusieurs modules à la fois en utilisant une liste séparée par des virgules. Par exemple :
  ```python
  import mod1
  import mod2, mod3, mod4
  ```
  Bien que cette dernière forme ne soit pas recommandée pour des raisons stylistiques, il est préférable et plus joli d'exprimer la même intention de manière plus explicite, telle que :
  ```python
  import mod2
  import mod3
  import mod4
  ```

### 2. Accéder aux entités d'un module importé
- Si un module est importé de la manière ci-dessus et que tu veux accéder à l'une de ses entités, tu dois préfixer le nom de l'entité en utilisant la notation par point. Par exemple :
  ```python
  import my_module

  result = my_module.my_function(my_module.my_data)
  ```
  L'extrait de code utilise deux entités provenant du module `my_module` : une fonction nommée `my_function()` et une variable nommée `my_data`. Les deux noms doivent être préfixés par `my_module`. Aucun des noms d'entités importées ne conflicte avec les noms identiques existant dans l'espace de noms de ton code.

### 3. Importer des entités individuelles d'un module
- Tu peux importer non seulement un module en entier, mais aussi des entités individuelles de celui-ci. Dans ce cas, les entités importées ne doivent pas être préfixées lors de leur utilisation. Par exemple :
  ```python
  from module import my_function, my_data

  result = my_function(my_data)
  ```
  Cette méthode - malgré son attrait - n'est pas recommandée en raison du risque de conflits avec les noms dérivés de l'importation de l'espace de noms du code.

### 4. Importer toutes les entités d'un module
- La forme la plus générale de l'instruction ci-dessus te permet d'importer toutes les entités offertes par un module :
  ```python
  from my_module import *

  result = my_function(my_data)
  ```
  **Remarque :** cette variante d'importation n'est pas recommandée pour les mêmes raisons que précédemment (la menace d'un conflit de noms est encore plus dangereuse ici).

### 5. Changer le nom de l'entité importée à la volée
- Tu peux changer le nom de l'entité importée "à la volée" en utilisant la phrase **`as`** de l'importation. Par exemple :
  ```python
  from module import my_function as fun, my_data as dat

  result = fun(dat)
  ```

---

J'espère que cette fiche de révision t'aidera à bien réviser ! Si tu as d'autres questions ou besoin de plus d'informations, fais-le moi savoir ! 😊