

![[Pasted image 20250115095956.png]]


----

# Mettre les interfaces NAT

## NAT Inside

l'interface qui part du routeur vers le réseau interne , Layer-3 (R->l3)
je select l'interface

```
enable    
conf t    
interface e0/0  
ip nat inside
```


## NAT Outside

sur l'autre qui va vers internet

```
enable
conf t
interface e0/1  
ip nat outside   
```
 



# Créer les access list  


Je créer une liste pour chaque vlan qui communique vers internet (donc pas les Imprimantes serveurs local)

j'effectue cette commande pour chaque vlan
pour le nom de la liste je met un nom qui pourra identifier un vlan come 10 ou SALES et l'adresse du réseau de met l'adresse de la vlan

```
acces-list (nom de la liste) permit (adresse du reseau)      

// Exemple

acces-list 10 permit 172.16.0.0 0.0.0.255


```
   

## Passer en PAT

On fait cela pour chaque access list

```
ip nat inside source list (nom de la list creer précemment) int (nom de l'interface qui va vers internet) overload 

// Exemple

ip nat inside source list 10 int e0/1 overload 

```
   

  