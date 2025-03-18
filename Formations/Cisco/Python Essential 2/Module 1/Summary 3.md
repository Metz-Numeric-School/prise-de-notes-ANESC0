
-----
## Résumé de la section 1.3.4

### 1. Modules et Packages
- Un **module** est conçu pour regrouper des entités liées telles que des fonctions, variables ou constantes.
- Un **package** est un conteneur qui regroupe plusieurs modules liés sous un nom commun.
  - Il peut être distribué tel quel (comme un ensemble de fichiers déployés dans un sous-répertoire) ou empaqueté dans un fichier zip.

### 2. Fichiers compilés Python
- Lors de la toute première importation d'un module, Python traduit son code source en un format semi-compilé stocké dans des fichiers `.pyc`.
- Ces fichiers `.pyc` sont déployés dans le répertoire `__pycache__` situé dans le répertoire de base du module.

### 3. Entités privées
- Pour indiquer qu'une entité particulière doit être traitée comme privée (c'est-à-dire ne pas être explicitement utilisée en dehors du module), ajoutez un préfixe `_` ou `__` à son nom.
- Notez que c'est seulement une recommandation, pas une obligation.

### 4. Shebang
- Les termes shabang, shebang, hasbang, poundbang et hashpling décrivent le digramme écrit comme `#!`.
- Il est utilisé pour indiquer aux systèmes d'exploitation de type Unix comment lancer le fichier source Python.
- Cette convention n'a aucun effet sous MS Windows.

### 5. Répertoires de packages non standard
- Pour que Python prenne en compte le répertoire d'un package non standard, son nom doit être inséré/ajouté à la liste des répertoires d'importation stockée dans la variable `path` contenue dans le module `sys`.

### 6. Fichier `__init__.py`
- Un fichier Python nommé `__init__.py` est exécuté implicitement lorsqu'un package le contenant est importé.
- Il est utilisé pour initialiser un package et/ou ses sous-packages (le cas échéant).
- Le fichier peut être vide, mais il ne doit pas être absent.
