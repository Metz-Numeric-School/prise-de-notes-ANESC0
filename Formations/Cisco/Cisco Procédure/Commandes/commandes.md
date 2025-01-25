
Voici une liste de commandes **Cisco IOS** qui te permettront d'afficher des informations essentielles sur les **ports**, les **interfaces**, les **VLANs**, et d'autres configurations importantes pour dépanner ou vérifier l'état de ton réseau.

## 1. **Vérifier l'état des interfaces**

- **Affiche l'état général de toutes les interfaces (physiques et VLAN) sur le switch/routeur** :
    
    ```plaintext
    show ip interface brief
    ```
    
    Cela te montre un résumé des interfaces avec leur état (up ou down) et leur adresse IP.
    
- **Vérifie les détails d'une interface spécifique (par exemple, gig0/1)** :
    
    ```plaintext
    show interface gig0/1
    ```
    
    Cette commande donne un aperçu détaillé de l'interface (statut, bande passante, erreurs, paquets reçus/expédiés, etc.).
    

## 2. **Vérifier les VLANs**

- **Affiche les VLANs existants et les ports associés** :
    
    ```plaintext
    show vlan brief
    ```
    
    Cela te montre la liste de tous les VLANs configurés et à quels ports chaque VLAN est associé.
    
- **Affiche les VLANs sur le switch** :
    
    ```plaintext
    show vlan
    ```
    
- **Affiche les VLANs actifs sur les interfaces trunk** :
    
    ```plaintext
    show interface trunk
    ```
    
    Cette commande te donne un aperçu des VLANs autorisés à passer par les liens trunk.
    

## 3. **Vérification de l'état du trunk**

- **Affiche les ports trunk et les VLANs autorisés** :
    
    ```plaintext
    show interfaces trunk
    ```
    
    Cela te permet de voir quels VLANs passent sur les interfaces en mode trunk.

## 4. **Vérification des routes et de la table de routage**

- **Affiche la table de routage** :
    
    ```plaintext
    show ip route
    ```
    
    Cela te donne un aperçu des routes configurées sur ton routeur.
    
- **Affiche les interfaces avec leurs adresses IP et les sous-réseaux associés** :
    
    ```plaintext
    show ip interface brief
    ```
    

## 5. **Vérification des configurations des VLANs**

- **Affiche les interfaces VLAN (principalement sur un switch)** :
    
    ```plaintext
    show interface vlan 10
    ```
    
    Remplace **10** par le numéro du VLAN pour afficher l'état d'un VLAN particulier.
    
- **Vérifie l'état des sous-interfaces sur le routeur (Router-on-a-Stick)** :
    
    ```plaintext
    show ip interface brief
    ```
    
    Cela te montre toutes les sous-interfaces et leur état.
    

### 6. **Vérification du VTP (VLAN Trunking Protocol)**

- **Affiche les informations du VTP** :
    
    ```plaintext
    show vtp status
    ```
    
    Cela te donne des informations sur l'état du VTP (mode, version, domaine, etc.).
    
- **Affiche les VLANs propagés via VTP** :
    
    ```plaintext
    show vtp vlan
    ```
    

## 7. **Vérification des ports de switch**

- **Vérifie l'état des ports sur un switch** :
    
    ```plaintext
    show interfaces status
    ```
    
    Cela te montre l'état des interfaces, leur type (access, trunk), et si elles sont activées ou non.
    
- **Vérifie l'état des ports spécifiques** :
    
    ```plaintext
    show interface fastEthernet 0/1
    ```
    

## 8. **Vérification des statistiques de l'interface**

- **Vérifie les erreurs et les statistiques d'une interface spécifique** :
    
    ```plaintext
    show interfaces gig0/1 counters
    ```
    
    Cela te montre les erreurs de transmission, les collisions, les paquets reçus/expédiés, etc.

## 9. **Vérification du spanning tree**

- **Affiche l'état de **Spanning Tree Protocol (STP)** sur le switch** :
    
    ```plaintext
    show spanning-tree
    ```
    
    Cela montre le rôle des ports dans l'algorithme STP, ainsi que l'état de chaque VLAN.

## 10. **Vérification des configurations de la passerelle par défaut**

- **Affiche la configuration de la passerelle par défaut sur un routeur** :
    
    ```plaintext
    show ip route
    ```
    
    Cela permet de voir si la passerelle par défaut est configurée correctement.

---

### Résumé des commandes principales :

- **`show ip interface brief`** : Résumé de toutes les interfaces (état et IP).
- **`show vlan brief`** : Liste des VLANs configurés.
- **`show interface trunk`** : Vérifie les interfaces en mode trunk.
- **`show vlan`** : Affiche les VLANs et les ports associés.
- **`show vtp status`** : Vérifie le statut du VTP.
- **`show interfaces status`** : Vérifie l'état des ports du switch.
- **`show ip route`** : Affiche la table de routage.
- **`show spanning-tree`** : Vérifie l'état du STP (Spanning Tree Protocol).

Ces commandes devraient couvrir la plupart des informations nécessaires pour diagnostiquer les problèmes de connectivité, vérifier la configuration des interfaces, des VLANs, et assurer un bon routage entre les VLANs.
