
### **Objectifs :**

- Vérifier la connectivité.
- Configurer et vérifier les ACL standard numérotées et nommées.
- Modifier une ACL standard.

---

### **Partie 1 : Vérification de la connectivité**

**Étapes :**

1. **Depuis PC-A**, pinguer **PC-C** et **PC-D** pour tester la connectivité.
2. **Depuis R1**, pinguer **PC-C** et **PC-D**.
3. **Depuis PC-C**, pinguer **PC-A** et **PC-B**.
4. **Depuis R3**, pinguer **PC-A** et **PC-B**.
5. Vérifier si tous les PC peuvent pinguer le serveur à l'adresse **209.165.200.254**.

**Note :** Il est important de tester la connectivité avant de configurer les ACL pour s'assurer que le réseau fonctionne correctement.

---

### **Partie 2 : Configuration et vérification des ACL standard numérotées et nommées**

#### **Étape 1 : Configuration d'une ACL standard numérotée**

1. Créer une ACL numérotée **1** sur **R3** qui permet l'accès de certains réseaux à un autre réseau.
    
    **Commandes :**
    
    ```bash
    R3(config)# access-list 1 remark Allow R1 LANs Access
    R3(config)# access-list 1 permit 192.168.10.0 0.0.0.255
    R3(config)# access-list 1 permit 192.168.20.0 0.0.0.255
    R3(config)# access-list 1 deny any
    ```
    
2. Appliquer l'ACL à l'interface **GigabitEthernet 0/0/0** en sortie :
    
    **Commandes :**
    
    ```bash
    R3(config)# interface g0/0/0
    R3(config-if)# ip access-group 1 out
    ```
    

#### **Étape 2 : Vérification de l'ACL numérotée**

1. Pour vérifier l'ACL et voir ses entrées :
    
    **Commandes :**
    
    ```bash
    R3# show access-list 1
    ```
    
2. Pour vérifier où l'ACL est appliquée et dans quelle direction :
    
    **Commandes :**
    
    ```bash
    R3# show ip interface g0/0/0
    ```
    

#### **Étape 3 : Test de l'ACL numérotée**

1. **Tester l'ACL** pour vérifier que le trafic du réseau **192.168.10.0/24** peut accéder au réseau **192.168.30.0/24** :
    - Depuis **PC-A**, pinguer **PC-C**.
2. Tester si le trafic du réseau **192.168.20.0/24** est autorisé vers le réseau **192.168.30.0/24** :
    - Depuis **PC-B**, pinguer **PC-C**.
3. Vérifier si **PC-D** peut ou non pinger **PC-C** (attendu : non autorisé).
4. Tester depuis **R1** si le ping vers **PC-C** est autorisé :
    
    ```bash
    R1# ping 192.168.30.3
    ```
    

---

#### **Étape 4 : Configuration d'une ACL nommée**

1. Créer une ACL standard nommée **BRANCH-OFFICE-POLICY** sur **R1**, permettant à **192.168.40.0/24** d'accéder à **192.168.10.0/24** et autorisant uniquement **PC-C** à y accéder :
    
    **Commandes :**
    
    ```bash
    R1(config)# ip access-list standard BRANCH-OFFICE-POLICY
    R1(config-std-nacl)# permit host 192.168.30.3
    R1(config-std-nacl)# permit 192.168.40.0 0.0.0.255
    R1(config-std-nacl)# end
    ```
    
2. Appliquer l'ACL à l'interface **GigabitEthernet 0/0/0** en sortie sur **R1** :
    
    **Commandes :**
    
    ```bash
    R1(config)# interface g0/0/0
    R1(config-if)# ip access-group BRANCH-OFFICE-POLICY out
    ```
    
3. Vérifier l'ACL nommée avec les commandes :
    
    **Commandes :**
    
    ```bash
    R1# show access-lists
    R1# show ip interface g0/0/0
    ```
    

#### **Étape 5 : Test de l'ACL nommée**

1. Depuis **PC-C**, tester la connectivité avec **PC-A** en pingant son adresse IP.
2. T
3. Tester si **PC-D** peut accéder au réseau **192.168.10.0/24** (attendu : non autorisé).

---

### **Partie 3 : Modification d'une ACL standard**

1. **Problème :** Le serveur **209.165.200.254** ne répond pas à **PC-A** à cause de l'ACL qui bloque le trafic sortant.
    
2. **Solution :** Ajouter une règle à l'ACL **BRANCH-OFFICE-POLICY** pour permettre le retour du trafic depuis le réseau **209.165.200.224/27** vers le réseau **192.168.10.0/24**.
    
    **Commandes :**
    
    ```bash
    R1(config)# ip access-list standard BRANCH-OFFICE-POLICY
    R1(config-std-nacl)# 30 permit 209.165.200.224 0.0.0.31
    R1(config-std-nacl)# 40 deny any
    R1(config-std-nacl)# end
    ```
    
3. **Vérification :** Vérifier que les modifications ont été appliquées avec :
    
    ```bash
    R1# show access-lists
    ```
    
4. **Test :** Depuis **PC-A**, tester si le serveur à **209.165.200.254** répond désormais :
    
    **Commandes :**
    
    ```bash
    PC-A# ping 209.165.200.254
    ```
    

---

### **Questions de réflexion :**

1. Pourquoi utiliser des ACL étendues si les ACL standard sont déjà efficaces ?
2. Bien que les ACL nommées demandent plus de saisie, pourquoi choisir des ACL nommées plutôt que des ACL numérotées ?

---

Ce résumé détaillé vous aide à suivre chaque étape de la configuration et de la vérification des ACL tout en répondant aux questions de l'exercice.