Voici un résumé des passages clés du document :

### **Introduction**

Cette vidéo est la cinquième d’une série utilisant **Cisco Packet Tracer** pour construire un réseau de plus en plus complexe. Cette partie se concentre sur la **sécurité de base**.

### **Sécurisation des accès**

- **Mots de passe** :
    - Importance d’utiliser des mots de passe **complexes** (majuscules, minuscules, chiffres, caractères spéciaux).
    - Éviter les mots de passe courts ou issus d’un dictionnaire.
    - Activation d’une **longueur minimale** (`security password min-length 8`).
- **Niveaux de privilège** :
    - **User EXEC mode (niveau 1)** : accès limité.
    - **Privileged EXEC mode (niveau 15)** : accès complet à la configuration.
- **Chiffrement des mots de passe** :
    - `enable secret` au lieu de `enable password` (plus sécurisé).
    - `service password-encryption` (chiffrement faible niveau 7, facilement déchiffrable).
    - Création d’utilisateurs locaux (`username Joe privilege 15 secret network4321`).

### **Protection contre les attaques**

- **Timeout automatique** (`exec-timeout 1 30`) : déconnexion après **1 min 30 sec** d’inactivité.
- **Blocage après plusieurs tentatives échouées** :
    - `login block-for 120 attempts 5 within 45`
    - Bloque les connexions après **5 échecs en 45 sec** pendant **2 min** (protection contre les attaques bruteforce).
- **Bannière d’avertissement** :
    - `banner motd "Accès interdit aux personnes non autorisées"`
    - Utile pour des raisons **légales** en cas d'intrusion.

### **Sécurisation des accès distants**

- **Telnet** (non sécurisé, en clair) → **désactivé** (`transport input ssh`).
- **SSH** (sécurisé, chiffré) → **activé** :
    - Nécessite un **nom de domaine** (`ip domain-name monentreprise.com`).
    - Génération d’une **clé RSA** (`crypto key generate rsa modulus 2048`).
    - Configuration des **VTY lines** pour exiger SSH (`line vty 0 4 login local`).

### **Protection des ports switch**

- **Activation de Switchport Security** (`switchport port-security`).
- **Apprentissage automatique de l’adresse MAC** (`switchport port-security mac-address sticky`).
- **Détection des appareils non autorisés** :
    - `violation shutdown` → désactive le port si un **MAC inconnu** est détecté.
    - **Remise en service manuelle** (`shutdown` puis `no shutdown`).

### **Conclusion**

Cette vidéo pose les bases de la **sécurité des équipements Cisco**, couvrant :

- La **gestion des accès** et **chiffrement des mots de passe**.
- Les **protections contre attaques bruteforce**.
- La **sécurisation des accès distants** avec SSH.
- La **protection des ports switch** contre les périphériques inconnus.

La prochaine vidéo portera sur des techniques de **sécurité avancée**.6





Liste des commandes :


### sur le routeur :

```
show privilege

# afficher la ligne de console

show line console ?

# Selectionner la ligne de console

line console 0
password cisco  // mot de passe
login // login


```


