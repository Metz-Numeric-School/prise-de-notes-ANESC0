
# Sur machine virtuelle StormShield


on importe le fichier **.ova** sur VMware sur cette VM.
Sur cette VM on lui attribue 3 carte réseaux en tout : 
- une en **NAT**
- deux en **host-only**
on désactivera le **DHCP** sur les deux en host-only

![[Pasted image 20250311105331.png]]

![[Pasted image 20250311105227.png]]


- on met le clavier en français et on défini un mot de passe. 


Après sur la deuxième interface nous mettrons un DHCP avec comme adresse IP  **172.16.10.254** avec une masque **255.255.255.0**

![[Pasted image 20250311144412.png]]


Une fois arrivée sur cette page on intègre une autre VM Windows 10 pour se connecter à notre  interface StormShield
![[Pasted image 20250311105344.png]]



# Sur VM Windows 10

dans les propriétés de la carte réseaux Windows 10 nous mettrons ces données

![[Pasted image 20250311105643.png]]

et nous entrerons l'url sur le navigateur

```
https://172.16.10.254
```



## Activé les mises à jour

pour pouvoir récupérer un numéro de licence sur **Stormshield** nous devons importer un fichier de mise à jour dans "**SYSTEME -> Maintenance** "


## Activer le fichier de Licence

On se rend dans "**SYSTEME -> Licence**" et on séléctionne le fichier de licence correspondant au numéro du firewall

![[Pasted image 20250311115436.png]]

![[Pasted image 20250311115454.png]]



-----


### Dans Politique de Sécurité

## Filtrage activer "Pass all"

![[Pasted image 20250402095058.png]]


#### NAT

![[Pasted image 20250311115023.png]]![[Pasted image 20250311115115.png]]


## LOG ST SHIELD 

user :  admin
mdp : P@ssw0rd

IP : 172.16.10.254