

Pour ajouter une machine virtuelle dans notre plan PNETLAB , il faut disposer d'une machine cliente comme Windows 10, mais cette procédure est valable pour un Windows Server également.

# 1ère étape

## Modifier le network editor

![[Pasted image 20250115135211.png]]

dans le virtual network il faut avoir un VMnet (VMnet0) en mode **NAT** et un autre VMnet (VMnet1) en mode **host only** que la VM contiendra dans ses cartes réseaux.

Le VMnet0 est donc la carte réseau NAT de ma VM PNETLAB. Et cette VM PNETLAB contient d'autres VMnet qui seront intégrés sur les VM que l'on ajoutera dans notre réseau sur PNETLAB


### Sur la VM PNETLAB :

![[Pasted image 20250115135556.png]]

### Sur la VM Windows 10 : 

on ajoute la carte réseau VMnet1

![[Pasted image 20250115140009.png]]

-----

# 2eme étape

Pour intégrer le serveur PRTG il faut que notre machine virtuelle Windows 10 soit inclue dans la VLAN que l'on a dédié aux serveurs sur notre plan PNETLAB

![[Pasted image 20250115143514.png]]

Dans mon plan j'ajouterai mon serveur PRTG sur la Vlan 60 , il apparaît déjà sur le plan mais nous verrons comment l'ajouter plus tard .

![[Pasted image 20250115140541.png]]


## Changer l'adresse ip de la VM Windows10

Après avoir consulté le plan je devrais ajouter une IP à ma VM incluse dans la plage de ma VLAN 
60 donc entre 172.16.1.128 -> 172.16.1.143
Je choisi donc l'adresse 172.16.1.130/28


Je me rend dans les paramètres réseau du PC . et je change donc manuelle l'adresse IP pour la mettre en statique directement

![[Pasted image 20250115141046.png]]



## Ajouter le VMnet1 sur PNETLAB

- Il faut maintenant ajouter le VMnet1 sur le réseau PNETLAB pour cela on se rend sur pnet lab et on ajoute un network

![[Pasted image 20250115141345.png]]

ce VMnet1 intégrera la VM Windows 10 et servira prochainement de serveur PRTG on l'ajoute donc sur un switch où nous avons des ports dédiés à la VLAN 60 SERVERS.

comme ceci.

Nous pouvons voir le serveur en jaune, qui permet d'intégrer notre VM Windows 10

![[Pasted image 20250115143454.png]]


Dès que mon serveur PRTG est ajouté je connecterais ce network sur mon interface que j'ai dédié à la VLAN 60 dans mon cas de e4/0 à e4/3.

Pour finaliser la communication entre un pc de notre réseau PNETLAB et notre VM sur VMnet1 il faudra configurer le parfeu de notre Windows 10 pour qu'il autorise les entrées.



# Configurer le pare-feu Windows 10

## Ajouter une règle de trafic entrant

On se rend dans le menu du pare-feu

![[Pasted image 20250115141816.png]]


On clique les "règles de trafic entrant".

![[Pasted image 20250115141904.png]]


On clique sur "nouvelle règle à droite" 

![[Pasted image 20250115141948.png]]


Ensuite on sélectionne "personnalisée" et on clique sur "protocole et ports"

![[Pasted image 20250115142034.png]]

Dans type de protocole on choisi ICMPv4

![[Pasted image 20250115142217.png]]


Ensuite on laisse comme tel

![[Pasted image 20250115142307.png]]


Pareil pour cette étape

![[Pasted image 20250115142711.png]]

Dans cette étape nous donnons simplement un nom à notre règle


![[Pasted image 20250115143131.png]]



# Ping d'un pc de PNETLAB à ma VM Windows 10

## De ma VM Windows 10

![[Pasted image 20250115143639.png]]


## D'un pc sur PNETLAB

![[Pasted image 20250115143734.png]]

