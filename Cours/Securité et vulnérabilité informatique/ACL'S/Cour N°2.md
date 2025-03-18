
# ACLs - Access Control List

## Standard

- Numérotée : 1-99 et 1300-1999
- Filtrage : IPv4 source

Les ACLs standard se situent proche de la **destination**

## Etendue

- numérotée : 100-199 et 2000 - 2699
- Nommée

Les ACLs étendue se situent près de la **source**
### Filtrage:

- IPv4 Source et Destination
- IPv6 Source et Destination
- Ports
- Protocoles
- @MAC (option)

### Mots clés :
- Any
- Host
- Etablished (ACL Etendu)


----


les **ACLs** se gèrent avec les wild card 

## Wild Card

Pour trouver la valeur **Wild Card** il faut prendre le subnet mask d'un réseaux et faire la différence avec la valeur maximal d'un subnet mask (CIDR 32) qui est **255.255.255.255**

### ex : 

Pour un subnet Mask de **255.255.255.192**

on fait **255.255.255.255** - **255.255.255.192** ce qui nous donne **0.0.0.64**



## ACL sont composées d'ACE ( Access Control Elements)

#### 2 Méthodes de saisie : 

```
access-list
```


ou une autre méthode plus moderne


```
ip access-list
```


#### Vérification : 

Pour afficher les Acces List

```
show access-list
```


notamment pour montrer sur l'interface en question


```
show ip interface
```




------



## Commandes

Exemple

![[Pasted image 20250305105522.png]]

### Afficher les interfaces Ou les Access

```
show run | include interface|access
```

![[Pasted image 20250305105536.png]]

---

### Supprimer une Access list sur une interface 

```
interface s0/0/0
no ip access-group 11 out
```

### Supprimer les acces-list

```
no access-list 11
```





----

### Configurer et appliquer une ACL

![[Pasted image 20250305112053.png]]


**exemple** :

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
    

---

###  Permettre l'accès par hôte

On créer une ACL d'un hôte grâce à son ip sur le router 

```bash
R1(config)# ip access-list standard File_Server_Restrictions   
R1(config-std-nacl)# permit host 192.168.20.4   // PC1
R1(config-std-nacl)# permit host 192.168.100.100    // server WEB
R1(config-std-nacl)# deny any 
```

 **Appliquer l'ACL** sur l'interface  en sortant :

  ```bash
   R1(config-if)# ip access-group File_Server_Restrictions out
   ```


----


### Mettre un commentaire sur une ACL

```
access-list 1 remark Allow R1 LANs Access
```
