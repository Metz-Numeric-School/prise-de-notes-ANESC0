# AWS Organizations

--------------------------------------------------------------------------

## A/

![[Pasted image 20241021154009.png]]

### *AWS Organizations* :

- **Service gratuit de gestion de comptes AWS**
- Permet de **consolider plusieurs comptes AWS** dans une **organisation centralisée**.

---

### **Principaux avantages** :

1. **Gestion centralisée** des stratégies d'accès sur plusieurs comptes.
2. **Contrôle de l'accès** aux services AWS.
3. **Automatisation** de la création et gestion des comptes AWS.
4. **Facturation consolidée** sur plusieurs comptes AWS.

--------------------------------------------------------------------------


## B/ Terminologie AWS Organizations

![[Pasted image 20241021154139.png]]


#### *Organisation de base (Racine)* :

- **Structure principale** contenant tous les comptes AWS.
- Peut contenir plusieurs **unités organisationnelles (OU)**.

#### *Unités Organisationnelles (OU)* :

- **Conteneur pour les comptes** au sein de la racine.
- Peut contenir d'autres **OU**, formant ainsi une hiérarchie.
- Ressemble à une **arborescence inversée** : la racine est en haut, avec les OU comme branches et les comptes comme feuilles.

#### *Politiques* :

- **Transmission des politiques** : Lorsqu'une politique est jointe à un nœud (racine ou OU), elle s'applique à toutes les branches et feuilles en dessous.
- **Politiques jointes aux OU** ou directement aux **comptes** pour un contrôle granulaire.

#### *Comptes* :

- Représentent des **comptes AWS standard** contenant vos ressources AWS.
- Un compte peut appartenir à **une seule unité organisationnelle** à la fois.

--------------------------------------------------------------------------



## C/
![[Pasted image 20241021154252.png]]

### **Fonctionnalités d'AWS Organizations**

1. **Politiques de Contrôle des Services (SCP)** :
    
    - Création de **politiques régissant** l'utilisation des services AWS sur plusieurs comptes.
2. **Groupes de Comptes** :
    
    - Création de **groupes de comptes** avec des politiques attachées pour assurer leur application uniforme sur tous les comptes.
3. **Gestion Automatisée des Comptes** :
    
    - Utilisation d'**API** pour automatiser la **création et la gestion** de nouveaux comptes AWS.
4. **Facturation Consolidée** :
    
    - Mise en place d'un **moyen de paiement unique** pour tous les comptes AWS de l'organisation.
    - Affichage d'une vue globale des **frais** encourus par tous les comptes.
    - Accès à des **réductions tarifaires** liées à l'utilisation groupée.


--------------------------------------------------------------------------


## D/ Différences entre AWS Organizations et AWS IAM

![[Pasted image 20241021154334.png]]

1. **AWS IAM (Identity and Access Management)** :
    
    - **Politiques d'accès** :
        - Donne ou refuse l'accès aux services AWS (ex. : Amazon S3) et à des ressources spécifiques (ex. : un compartiment S3).
        - Peut être appliquée à quelques utilisateurs, groupes ou rôles IAM.
        - **Ne peut pas** restreindre l'accès de la racine ou de l'administrateur du compte AWS.
2. **AWS Organizations** :
    
    - **Politiques de Contrôle des Services (SCP)** :
        - Donne ou refuse l'accès à des services AWS pour des comptes individuels ou des groupes au sein d'une unité d'organisation.
        - Les actions d'une SCP affectent **tous les utilisateurs, groupes et rôles IAM** d'un compte, y compris la racine et l'administrateur.



--------------------------------------------------------------------------


## E/

![[Pasted image 20241021154500.png]]
**Prérequis :**

- Accès à au moins deux comptes AWS existants.
- Connexion à chaque compte en tant qu'administrateur.

#### *Étapes de configuration :*

1. **Créer une organisation :**
    
    - Utilisez votre compte AWS actuel comme compte principal.
    - Invitez un autre compte AWS à rejoindre votre organisation.
    - Créez un nouveau compte comme compte membre.
2. **Créer des unités organisationnelles (OU) :**
    
    - Créez deux unités organisationnelles dans votre nouvelle organisation.
    - Placez les comptes membres dans ces OU.
3. **Créer des politiques de contrôle des services (SCP) :**
    
    - Définissez des restrictions pour les actions pouvant être déléguées aux utilisateurs et aux rôles dans les comptes membres.
    - Note : Les SCP sont un type de politique de contrôle d'organisation.
4. **Tester les politiques :**
    
    - Connectez-vous en tant qu'utilisateur dans chaque rôle (ex. : OU1, OU2).
    - Vérifiez comment les SCP impactent l'accès aux comptes.
    - Utilisez le simulateur de politique IAM pour tester et dépanner les politiques IAM basées sur les ressources jointes aux utilisateurs, groupes ou rôles dans votre compte AWS.



--------------------------------------------------------------------------


## F /

![[Pasted image 20241021154623.png]]


#### *AWS Organizations peut être géré via plusieurs interfaces :*

1. **Console de gestion AWS :**
    
    - Interface basée sur le navigateur.
    - Permet d’effectuer toutes les tâches de gestion de votre organisation et de vos ressources AWS.
2. **Interface de ligne de commande AWS (AWS CLI) :**
    
    - Outils en ligne de commande pour exécuter des commandes AWS.
    - Plus rapide et souvent plus pratique que la console pour effectuer des tâches.
3. **Kits SDK AWS :**
    
    - Comprend des bibliothèques et des exemples de code pour divers langages et plateformes (Java, Python, Ruby, .NET, iOS, Android).
    - Facilite la gestion de tâches comme la signature des demandes, la gestion des erreurs et les nouvelles tentatives de demande.
4. **API HTTPS d'AWS Organizations :**
    
    - Permet l'accès programmatique à AWS Organizations.
    - Vous pouvez envoyer des demandes HTTPS directement au service.
    - Nécessite l’inclusion d’un code pour signer numériquement les demandes avec vos informations d'identification.

