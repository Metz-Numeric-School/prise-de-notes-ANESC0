

# Partie 1
### Résumé du Scénario

#### **Objectifs :**

- **Partie 1** : Planification d'une mise en œuvre d'une ACL (Access Control List).
- **Partie 2** : Configuration, application et vérification d'une ACL standard.

#### **Contexte :**

Les **ACL standards** sont utilisées sur les routeurs pour contrôler le trafic basé sur l'adresse source. L'objectif de cette activité est de :

1. Définir des critères de filtrage.
2. Configurer des ACL standard.
3. Appliquer ces ACL sur les interfaces des routeurs.
4. Vérifier et tester l'implémentation de l'ACL.

Les routeurs sont déjà configurés avec des adresses IP et le protocole de routage **EIGRP**.

---

### **Instructions :**

#### **Partie 1 : Planification de l'implémentation des ACL**

- **Étape 1 : Vérifier la connectivité actuelle** Avant d'appliquer des ACL, il est essentiel de vérifier que tous les appareils du réseau peuvent communiquer entre eux en pingant chaque dispositif.
    
- **Étape 2 : Évaluer deux politiques réseau et planifier l'implémentation des ACL :**
    
    - **Sur R2** :
        1. **Politique :** Le réseau **192.168.11.0/24** ne doit pas avoir accès au **WebServer** du réseau **192.168.20.0/24**.
        2. **Action :** Créer une ACL pour interdire l'accès de **192.168.11.0/24** à **192.168.20.254** (WebServer) et appliquer cette ACL sur l'interface sortante vers le WebServer. Créer une règle secondaire pour permettre tout autre trafic.
    - **Sur R3** :
        1. **Politique :** Le réseau **192.168.10.0/24** ne doit pas pouvoir communiquer avec le réseau **192.168.30.0/24**.
        2. **Action :** Créer une ACL pour interdire l'accès de **192.168.10.0/24** à **192.168.30.0/24** et appliquer cette ACL sur l'interface sortante vers le PC3. Créer une règle secondaire pour permettre tout autre trafic.

---

### **Résumé des actions à effectuer :**

1. **Vérification de la connectivité réseau.**
2. **Création des ACLs** pour restreindre les accès selon les politiques définies.
3. **Application des ACLs** sur les interfaces concernées des routeurs (R2 et R3).
4. **Vérification du bon fonctionnement** des ACLs après application.

Cela résume l'objectif et les actions nécessaires pour mettre en œuvre les ACLs sur ton réseau.


-----


# Partie 2 

### **Étape 1 : Configurer et appliquer une ACL numérotée sur R2**

1. **Créer une ACL numérotée 1** sur R2 qui **interdit l'accès** au réseau **192.168.20.0/24** depuis le réseau **192.168.11.0/24** :
    
    ```bash
    R2(config)# access-list 1 deny 192.168.11.0 0.0.0.255
    ```
    
2. **Permettre tout autre trafic** en ajoutant une règle de permission :
    
    ```bash
    R2(config)# access-list 1 permit any
    ```
    
3. **Vérifier la configuration de l'ACL** pour s'assurer que les règles sont correctement appliquées :
    
    ```bash
    R2# show access-lists
    ```
    
    Résultat attendu :
    
    ```plaintext
    Standard IP access list 1
    10 deny 192.168.11.0 0.0.0.255
    20 permit any
    ```
    
4. **Appliquer l'ACL** sur l'interface **GigabitEthernet 0/0** pour filtrer le trafic sortant vers le WebServer :
    
    ```bash
    R2(config)# interface GigabitEthernet0/0
    R2(config-if)# ip access-group 1 out
    ```
    



### **Étape 2 : Configurer et appliquer une ACL numérotée sur R3**

1. **Créer une ACL numérotée 1** sur R3 qui **interdit l'accès** au réseau **192.168.30.0/24** depuis le réseau **192.168.10.0/24** :
    
    ```bash
    R3(config)# access-list 1 deny 192.168.10.0 0.0.0.255
    ```
    
2. **Permettre tout autre trafic** en ajoutant une règle de permission :
    
    ```bash
    R3(config)# access-list 1 permit any
    ```
    
3. **Vérifier la configuration de l'ACL** pour s'assurer que les règles sont correctement appliquées :
    
    ```bash
    R3# show access-lists
    ```
    
    Résultat attendu :
    
    ```plaintext
    Standard IP access list 1
    10 deny 192.168.10.0 0.0.0.255
    20 permit any
    ```
    
4. **Appliquer l'ACL** sur l'interface **GigabitEthernet 0/0** pour filtrer le trafic sortant vers le réseau **192.168.30.0/24** :
    
    ```bash
    R3(config)# interface GigabitEthernet0/0
    R3(config-if)# ip access-group 1 out
    ```
    

### **Étape 3 : Vérification de la configuration et de la fonctionnalité des ACL**

1. **Vérifier l'application des ACL sur les interfaces** avec la commande :
    
    ```bash
    R2# show run
    ```
    
2. **Tester la fonctionnalité des ACL** avec les pings suivants pour vérifier que le filtrage fonctionne comme prévu :
    
    - Ping de **192.168.10.10 à 192.168.11.10** (devrait réussir)
    - Ping de **192.168.10.10 à 192.168.20.254** (devrait réussir)
    - Ping de **192.168.11.10 à 192.168.20.254** (devrait échouer)
    - Ping de **192.168.10.10 à 192.168.30.10** (devrait échouer)
    - Ping de **192.168.11.10 à 192.168.30.10** (devrait réussir)
    - Ping de **192.168.30.10 à 192.168.20.254** (devrait réussir)
3. **Vérifier les résultats de l'ACL** avec la commande :
    
    ```bash
    R2# show access-lists
    ```
    
    Résultat attendu (nombre de correspondances) :
    
    ```plaintext
    Standard IP access list 1
    10 deny 192.168.11.0 0.0.0.255 (4 match(es))
    20 permit any (8 match(es))
    ```
    
    Pour R3 :
    
    ```bash
    R3# show access-lists
    ```
    
    Résultat attendu :
    
    ```plaintext
    Standard IP access list 1
    10 deny 192.168.10.0 0.0.0.255 (4 match(es))
    20 permit any (8 match(es))
    ```
    

---

### **Conclusion :**

- Après avoir appliqué ces configurations et effectué les tests, tu devrais observer que les ACLs limitent correctement l'accès selon les politiques définies dans la Partie 1 du scénario.