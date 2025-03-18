
![[Pasted image 20250305113237.png]]
### Résumé du scénario

**Objectifs :**

1. Configurer et appliquer une ACL standard nommée.
2. Vérifier l'application de l'ACL.

**Contexte :** L'administrateur réseau doit créer une ACL standard nommée pour empêcher l'accès à un serveur de fichiers, tout en permettant uniquement à certains appareils (PC1 et le Web Server) d'y accéder.

### **Partie 1 : Configurer et Appliquer une ACL Standard Nommée**

1. **Vérifier la connectivité** avant d'appliquer l'ACL (les trois postes de travail doivent pouvoir pinger le Web Server et le File Server).
    
2. **Configurer une ACL nommée** sur R1 :
    
    - Permettre l'accès uniquement à **192.168.20.4 (PC1)** et **192.168.100.100 (Web Server)**.
    - Bloquer tout autre accès.
    
    ```bash
    R1(config)# ip access-list standard File_Server_Restrictions
    R1(config-std-nacl)# permit host 192.168.20.4
    R1(config-std-nacl)# permit host 192.168.100.100
    R1(config-std-nacl)# deny any
    ```
    
3. **Vérifier la configuration de l'ACL** avec la commande `show access-lists` :
    
    ```bash
    R1# show access-lists
    Standard IP access list File_Server_Restrictions
    10 permit host 192.168.20.4
    20 permit host 192.168.100.100
    30 deny any
    ```
    
4. **Appliquer l'ACL** sur l'interface **Fast Ethernet 0/1** en sortant :
    
    ```bash
    R1(config-if)# ip access-group File_Server_Restrictions out
    ```
    
5. **Sauvegarder la configuration.**
    

### **Partie 2 : Vérifier l'Implémentation de l'ACL**

1. **Vérifier l'application de l'ACL** avec les commandes :
    - `show access-lists` (pour vérifier l'ACL).
    - `show run` ou `show ip interface fastethernet 0/1` (pour vérifier l'application de l'ACL sur l'interface).
2. **Vérifier le fonctionnement de l'ACL** :
    - Tous les postes de travail peuvent pinger le **Web Server**.
    - Seuls **PC1** et le **Web Server** peuvent pinger le **File Server**.
    - Utiliser `show access-lists` pour vérifier le nombre de paquets ayant correspondu à chaque règle.

---

En résumé, cette configuration bloque l'accès au serveur de fichiers pour tous les appareils sauf **PC1** et le **Web Server**.