# Amazon S3 Glacier


[[AWS S3 Glacier]]


## A/

![[Pasted image 20241030023901.png]]

Avec l'**archivage des données** sur **Amazon S3 Glacier**, vous pouvez stocker vos données à un coût très bas, même inférieur à celui d'Amazon S3. Cependant, la récupération des données nécessite du temps, pouvant prendre plusieurs heures. Voici les **trois concepts clés** à connaître :

### Concepts Clés d'Amazon S3 Glacier

1. **Archive** :
   - Une **archive** est tout objet (photo, vidéo, fichier, document) stocké dans Amazon S3 Glacier. 
   - C'est l'unité de stockage de base, chaque archive ayant son propre **ID** et optionnellement une **description**.

2. **Coffre** :
   - Un **coffre** sert de conteneur pour les archives. 
   - Lors de sa création, vous devez spécifier son **nom** et la **région** où il sera localisé.

3. **Stratégie d'accès au coffre** :
   - Elle détermine qui peut accéder aux données dans le coffre et les opérations possibles. 
   - Une **stratégie d'accès** et une **politique de verrouillage** peuvent être créées pour gérer les autorisations et empêcher les modifications.

### Options de Récupération de Données

Amazon S3 Glacier propose trois options de récupération, chacune avec des délais d'accès et des coûts distincts :

- **Récupérations Accélérées** : disponibles en **1 à 5 minutes**, mais à un tarif plus élevé.
- **Récupérations Standard** : prennent généralement **3 à 5 heures**, avec un tarif inférieur à celui des récupérations accélérées.
- **Récupérations en Bloc** : prennent entre **5 et 12 heures**, et sont la solution la moins coûteuse.




------------------------------------------------------


## B/
![[Pasted image 20241030024024.png]]

Voici un résumé des **cas d'utilisation d'Amazon S3 Glacier** pour l'archivage de données :

### Cas d'Utilisation d'Amazon S3 Glacier

1. **Archivage des Actifs Multimédias** :
   - Les ressources multimédias comme les vidéos et reportages nécessitent un stockage durable et peuvent atteindre plusieurs pétaoctets. 
   - Amazon S3 Glacier permet d'archiver ces contenus à moindre coût, avec la possibilité de les déplacer vers Amazon S3 pour leur diffusion en cas de besoin.

2. **Archivage de Données Médicales** :
   - Les systèmes hospitaliers doivent conserver des pétaoctets de dossiers patients pour des périodes prolongées, en raison des exigences réglementaires.
   - Amazon S3 Glacier offre une solution fiable et sécurisée pour l'archivage des dossiers des patients à très faible coût.

3. **Archivage Réglementaire et de Conformité** :
   - De nombreuses entreprises, notamment dans les secteurs de la santé et des services financiers, doivent respecter des réglementations strictes sur la conservation des données.
   - Le verrouillage de coffre d'Amazon S3 Glacier permet d'assurer la conformité avec des réglementations telles que la règle 17a-4(f) de la SEC.

4. **Archivage des Données Scientifiques** :
   - Les organismes de recherche gèrent d'importants volumes de données générées et analysées au cours de leurs travaux.
   - Amazon S3 Glacier simplifie la gestion des données en éliminant les complexités liées à la planification de la capacité et à la gestion des installations sur site.

5. **Conservation des Actifs Numériques** :
   - Les bibliothèques et administrations se heurtent à des défis d'intégrité des données pour la préservation numérique.
   - Amazon S3 Glacier effectue des vérifications régulières de l'intégrité des données et inclut des mécanismes d'auto-régénération.

6. **Remplacement des Bandes Magnétiques** :
   - Bien que les bibliothèques de bandes offrent un coût de stockage réduit, elles nécessitent un investissement initial élevé et une maintenance spécialisée.
   - Amazon S3 Glacier n'engendre pas de coût initial et évite les frais de maintenance, rendant le stockage plus économique et plus simple à gérer.

----


## C/

![[Pasted image 20241030024113.png]]


### Accès à Amazon S3 Glacier

Pour gérer vos données dans **Amazon S3 Glacier**, voici les options disponibles :

1. **Console de Gestion AWS** :
   - Permet de créer et de supprimer des coffres, ainsi que de gérer les politiques d'archivage.

2. **API REST d'Amazon S3 Glacier** :
   - Nécessaire pour la plupart des opérations, comme le téléchargement et la récupération d'archives.

3. **Kits SDK AWS** :
   - Utilisez des SDK pour Java ou .NET pour intégrer facilement S3 Glacier dans vos applications.

4. **AWS CLI** :
   - Interface en ligne de commande pour exécuter des commandes et automatiser des tâches.



----


## D/

![[Pasted image 20241030024223.png]]

#### Types de Politiques

1. **Par Objet** : Règles spécifiques pour chaque objet.
2. **Par Compartiment** : Règles appliquées à tous les objets d’un compartiment.

#### Exemple de Politique

- Lorsqu’un utilisateur télécharge une vidéo, l’aperçu est d’abord stocké dans **Amazon S3 Standard**.
- Après 30 jours sans accès, il est déplacé vers **Amazon S3 – Accès peu fréquent**.
- Après un an, il est transféré vers **Amazon S3 Glacier** et supprimé après 1 an.

### Avantages

- **Coûts Réduits** : Déplacez les données peu utilisées vers des options moins coûteuses.
- **Gestion Automatique** : Les politiques gèrent le déplacement sans intervention manuelle.


----


## E/


![[Pasted image 20241030024329.png]]


![[Pasted image 20241030024400.png]]

### Différences de Chiffrement entre Amazon S3 et Amazon S3 Glacier

- **Amazon S3 Glacier** :  
  - Toutes les données sont **chiffrées par défaut**.

- **Amazon S3** :  
  - Le chiffrement côté serveur doit être activé par l'application. Options disponibles :
  
  1. **SSE-S3** (géré par Amazon) :  
     - Chiffrement avec clé unique par objet, utilisant AES-256.
  
  2. **SSE-C** (clé fournie par le client) :  
     - Vous gérez vos propres clés de chiffrement.

  3. **SSE avec AWS KMS** :  
     - Utilise des clés principales du client pour le chiffrement et la gestion des clés.

### Conclusion

Le choix entre S3 et S3 Glacier dépend des besoins en matière de stockage et de sécurité.


----

## F/

![[Pasted image 20241030024533.png]]



--------



![[Pasted image 20241030024553.png]]


