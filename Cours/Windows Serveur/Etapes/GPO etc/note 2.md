
Je vais te guider étape par étape pour répondre à ta consigne en tenant compte de tes UOs et de la configuration demandée. Voici ce que tu dois faire :

---

### **Étape 1 : Organisation des utilisateurs et des groupes dans les UOs**

1. **Vérifie la structure des UOs dans Active Directory** :
    
    - Tes UOs devraient correspondre aux services de la société Heaven Habitat (par exemple : UO-ServCommercial, UO-ServInformatique, UO-Direction, etc.).
    - Place les comptes utilisateurs dans les UOs correspondantes.
        - Exemple :
            - Tous les employés du service commercial vont dans **UO-ServCommercial**.
            - Les directeurs iront dans **UO-Direction**.
2. **Crée des groupes de sécurité pour chaque service** :
    
    - Exemple :
        - **Grp_ServCommercial** pour le service commercial.
        - **Grp_ServInformatique** pour le service informatique.
    - Ajoute les utilisateurs dans leur groupe respectif.

---

### **Étape 2 : Création des dossiers partagés sur SERV1**

1. **Créer les dossiers sur le disque de SERV1** :
    
    - Exemple de structure :
        
        ```
        D:\Shares\Commercial
        D:\Shares\Informatique
        D:\Shares\Direction
        D:\Shares\Common
        ```
        
    - Chaque dossier sera dédié à un service (ou commun pour tous).
2. **Configurer le partage des dossiers** :
    
    - Clique droit sur chaque dossier > Propriétés > Partage > Partage avancé.
    - Coche **Partager ce dossier**.
    - Attribue des permissions de partage au groupe de sécurité correspondant.
        - Exemple : **Grp_ServCommercial** aura accès au dossier `\\SERV1\Commercial`.
3. **Configurer les permissions NTFS (onglet Sécurité)** :
    
    - Ajoute les groupes de sécurité et attribue les droits nécessaires :
        - **Lecture/Écriture** pour les utilisateurs de chaque service sur leur dossier respectif.
        - **Full Control** pour les administrateurs si nécessaire.

---

### **Étape 3 : Mappage des lecteurs réseau via GPO**

1. **Ouvre la console GPMC** :
    
    - Sur SERV3 (contrôleur de domaine), ouvre **Gestion des stratégies de groupe**.
2. **Crée une nouvelle GPO** :
    
    - Nomme-la, par exemple, **Mappage des lecteurs réseau**.
3. **Configurer les lecteurs réseau** :
    
    - Navigue vers : **Configuration utilisateur > Préférences > Paramètres Windows > Lecteurs réseau**.
    - Ajoute un mappage par service :
        - **Action** : Créer.
        - **Emplacement** : Chemin réseau du dossier partagé (par exemple, `\\SERV1\Commercial`).
        - **Lettre du lecteur** : Attribue **S:** pour chaque service.
        - **Ciblage au niveau des éléments** : Ajoute une règle pour que seul le groupe concerné (par exemple, **Grp_ServCommercial**) ait ce mappage.

---

### **Étape 4 : Configuration des profils errants pour le service commercial**

1. **Attribue un chemin de profil utilisateur** :
    
    - Ouvre les propriétés des utilisateurs du service commercial dans Active Directory.
    - Dans l'onglet **Profil**, remplis le champ **Chemin du profil** :
        - Exemple : `\\SERV1\Profiles\%username%`.
    - Crée le dossier `D:\Profiles` sur SERV1 et partage-le.
2. **Configurer les permissions sur le dossier des profils** :
    
    - Partage `D:\Profiles` et attribue **Modification** au groupe **Grp_ServCommercial**.

---

### **Étape 5 : Configuration du lecteur personnel (H:)**

1. **Configurer les dossiers personnels** :
    
    - Crée un dossier `D:\Users` sur SERV1.
    - Configure chaque utilisateur avec un chemin de dossier de base :
        - Dans l'onglet **Profil** de l'utilisateur dans Active Directory, sélectionne **Connecter** et attribue **H:** au chemin réseau :
            - Exemple : `\\SERV1\Users\%username%`.
2. **Configurer les permissions sur `D:\Users`** :
    
    - Partage `D:\Users` et configure NTFS pour que chaque utilisateur ait accès uniquement à son propre dossier.

---

### **Étape 6 : Configurer le dossier commun (P:)**

1. **Configurer le dossier partagé COMMON** :
    
    - Crée le dossier `D:\Shares\Common` sur SERV1.
    - Configure le partage réseau : `\\SERV1\Common`.
    - Partage et permissions NTFS :
        - Partage : Tous les utilisateurs ont accès.
        - NTFS : Configure les permissions pour que chaque utilisateur puisse lire/modifier uniquement ses propres fichiers.
2. **Configurer le mappage réseau (P:) via GPO** :
    
    - Dans la même GPO que pour **S:**, ajoute une nouvelle configuration de lecteur réseau :
        - **Emplacement** : `\\SERV1\Common`.
        - **Lettre** : **P:**.

---

### **Étape 7 : Configurer les plages horaires**

1. **Configurer les heures de connexion** :
    - Dans Active Directory, ouvre les propriétés de chaque utilisateur.
    - Dans l’onglet **Compte**, clique sur **Heures de connexion**.
    - Configure les heures (par exemple, 7h à 19h pour les employés normaux, et illimité pour les directeurs).

---

### **Étape 8 : Configuration de l'imprimante réseau**

1. **Partager l'imprimante** :
    
    - Connecte l'imprimante au réseau via SERV1.
    - Dans **Gestion des imprimantes**, partage l’imprimante.
2. **Configurer l’accès via GPO** :
    
    - Ajoute une configuration d’imprimante réseau dans la GPO.
    - Chemin : **Configuration utilisateur > Préférences > Paramètres Windows > Imprimantes**.

---

Si tu veux que je détaille une partie précise ou que je corrige un problème, dis-le-moi !
