
------
## Résumé de la section 1.4.8

### 1. Python Package Index (PyPI)
- Un **répertoire** conçu pour collecter et partager du code Python gratuit existe sous le nom de **Python Package Index (PyPI)**.
- Il est également connu sous le nom plus niche de **The Cheese Shop**.
- Le site web du Shop est disponible à l'adresse [https://pypi.org/](https://pypi.org/).

### 2. Utilisation de The Cheese Shop avec `pip`
- Un outil spécialisé appelé **pip** a été créé pour utiliser The Cheese Shop.
- **pip** signifie "pip installs packages" (pip installe des packages).
- **pip** peut ne pas être déployé dans le cadre de l'installation standard de Python ; il est donc possible que vous deviez l'installer manuellement.
- **pip** est un outil de console.

### 3. Vérification de la version de `pip`
- Pour vérifier la version de `pip`, l'une des commandes suivantes doit être exécutée :
  ```sh
  pip --version
  ```
  ou
  ```sh
  pip3 --version
  ```
- Vérifiez laquelle de ces commandes fonctionne dans l'environnement de votre système d'exploitation.

### 4. Principales activités de `pip`
- `pip help operation` – affiche une brève description de pip.
- `pip list` – affiche la liste des packages actuellement installés.
- `pip show package_name` – affiche des informations sur package_name, y compris les dépendances du package.
- `pip search anystring` – recherche dans les répertoires PyPI pour trouver des packages dont les noms contiennent anystring.
- `pip install name` – installe name à l'échelle du système (des problèmes peuvent survenir si vous n'avez pas les droits administratifs).
- `pip install --user name` – installe name uniquement pour vous ; aucun autre utilisateur de la plateforme ne pourra l'utiliser.
- `pip install -U name` – met à jour un package précédemment installé.
- `pip uninstall name` – désinstalle un package précédemment installé.
