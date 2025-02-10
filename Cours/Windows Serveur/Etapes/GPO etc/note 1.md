Oui, absolument ! Avant de mapper le lecteur réseau pour vos utilisateurs, vous devez d'abord **créer le dossier sur le serveur 1** et le configurer pour qu'il soit accessible via le réseau. Voici un guide détaillé pour bien faire les choses :

---

### **Étape 1 : Créer le dossier sur SERV1**

1. **Connectez-vous à SERV1** :
    
    - Ouvrez une session sur le serveur principal (SERV1).
2. **Créer le dossier** :
    
    - Accédez au disque où vous souhaitez stocker les fichiers (par exemple, `D:`).
    - Créez un nouveau dossier, par exemple :
        - `D:\Services\Commercial` pour le Service Commercial.
        - `D:\Common` pour le dossier commun.
3. **Nommer le dossier** :
    
    - Donnez un nom explicite au dossier pour éviter toute confusion (par exemple, utilisez les noms des services).

---

### **Étape 2 : Partager le dossier**

1. **Ouvrir les propriétés du dossier** :
    
    - Faites un clic droit sur le dossier (par exemple, `Commercial`) et cliquez sur **Propriétés**.
2. **Configurer le partage** :
    
    - Allez dans l'onglet **Partage** et cliquez sur **Partage avancé**.
    - Cochez **Partager ce dossier**.
    - Donnez un nom de partage, par exemple `Commercial` ou `Services_Commercial`.
3. **Configurer les permissions de partage** :
    
    - Cliquez sur **Autorisations** :
        - Supprimez `Tout le monde`.
        - Ajoutez le groupe de sécurité correspondant (par exemple, `Grp_Service_Commercial`).
        - Donnez uniquement les droits **Modifier**.

---

### **Étape 3 : Configurer les permissions NTFS**

1. **Ouvrir l'onglet Sécurité** :
    
    - Dans les propriétés du dossier, allez dans l'onglet **Sécurité**.
2. **Configurer les permissions NTFS** :
    
    - Cliquez sur **Modifier**, puis sur **Ajouter**.
    - Ajoutez le groupe correspondant au service (par exemple, `Grp_Service_Commercial`).
    - Attribuez les permissions suivantes :
        - **Lecture & exécution** et **Écriture** pour les utilisateurs du service.
        - Assurez-vous que seuls les directeurs ou administrateurs ont un contrôle total si nécessaire.
3. **Appliquer les permissions** :
    
    - Cliquez sur **Appliquer** et **OK**.

---

### **Étape 4 : Tester l’accès**

1. **Vérifier le partage** :
    
    - Depuis une autre machine, ouvrez l’Explorateur de fichiers et tapez `\\SERV1` dans la barre d’adresse.
    - Assurez-vous que le dossier partagé est visible et accessible avec les bonnes permissions.
2. **Simuler une connexion** :
    
    - Essayez de créer, modifier, ou supprimer un fichier pour vérifier que les droits NTFS et de partage sont bien appliqués.

---

### **Étape 5 : Mapper le lecteur réseau**

Une fois le dossier créé et partagé, vous pouvez passer à l’étape suivante pour **mapper le lecteur réseau** (via méthode manuelle ou GPO comme expliqué plus haut).

Si vous avez des doutes sur une étape ou si quelque chose ne fonctionne pas comme prévu, n'hésitez pas !