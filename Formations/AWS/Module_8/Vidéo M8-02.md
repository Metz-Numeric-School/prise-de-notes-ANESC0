
# Amazon DynamoDB



## A/

![[Pasted image 20241030214219.png]]

DynamoDB passe au modèle de base de données **non relationnelle**, contrastant avec les bases de données **relationnelles** (RDB). Voici les différences clés :

- **Bases relationnelles (RDB)** : Utilisent des données **structurées** organisées en tables, enregistrements, et colonnes, avec des relations définies entre tables. Elles s'appuient sur le **langage SQL** pour l'interaction et peuvent être limitées pour l'**évolutivité horizontale** ou les données semi-structurées, nécessitant souvent des jointures.

- **Bases non relationnelles** : Ne suivent pas le modèle relationnel classique et sont populaires pour répondre aux **limites des RDB**. Elles sont idéales pour des données **non structurées** et **semi-structurées**, offrant une **mise à l'échelle ascendante** pour gérer des demandes de données variées.



## B/ [[AWS DynamoDB]]


![[Pasted image 20241030214333.png]]



![[Pasted image 20241030214534.png]]


## C/



![[Pasted image 20241030214548.png]]

DynamoDB gère la croissance des tables en les **partitionnant et en indexant les données** selon la clé principale. Il existe deux méthodes pour récupérer des éléments :

1. **Query** : Cette opération utilise la **clé principale** pour un accès rapide aux éléments grâce au partitionnement.
2. **Scan** : Elle recherche des éléments en fonction d’autres attributs, mais est **moins efficace** car elle doit analyser l'ensemble des éléments de la table pour identifier ceux correspondant aux critères.

Le **partitionnement** optimise l'interrogation et la numérisation des tables de grande taille pour une meilleure accessibilité.


![[Pasted image 20241030214635.png]]

Pour optimiser les requêtes dans DynamoDB, il est essentiel de bien définir la **clé principale** de la table :

1. **Clé unique** : Basée sur un seul attribut (par exemple, un GUID ou un ID produit), elle identifie chaque élément de façon unique. Une bonne distribution des valeurs, comme les identifiants aléatoires, améliore l'efficacité des requêtes.
  
2. **Clé composite** : Composée d'une **clé de partition** et d'une **clé secondaire**. Par exemple, dans une table de livres, la clé pourrait être l'auteur (partition) et le titre (tri). Cette approche est utile pour les requêtes fréquentes basées sur des relations, comme lister les livres d'un même auteur.

----



![[Pasted image 20241030214829.png]]

