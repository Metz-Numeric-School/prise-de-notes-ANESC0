
# Notions de base de la mise en réseau

## A/

![[Pasted image 20241028131359.png]]

Un **réseau informatique** est constitué de deux **machines clientes** ou plus connectées entre elles pour **partager des ressources**. Un réseau peut être divisé logiquement en **sous-réseaux**. La mise en réseau nécessite un **périphérique réseau** (tel qu'un **routeur** ou un **commutateur**) pour connecter les clients et permettre la **communication** entre eux.



--------------------------------------------------------------------------


## B/

![[Pasted image 20241028131444.png]]

Chaque **ordinateur client** d'un réseau possède une **adresse IP unique** qui l'identifie. Une adresse IP est un **libellé numérique** au format **décimal** que les machines convertissent en **format binaire**. Par exemple, l'adresse IP **192.0.2.0** est constituée de quatre nombres séparés par un point (.), chacun représentant **8 bits** au format **octal** et pouvant aller de **0 à 255**. L'ensemble de ces quatre nombres forme une adresse IP de **32 bits** en binaire.



--------------------------------------------------------------------------

## C/

![[Pasted image 20241028131548.png]]

Une **adresse IP** de **32 bits** est appelée **adresse IPv4**. Des **adresses IPv6** de **128 bits** existent également, permettant de connecter davantage d'**appareils**. Une adresse IPv6 est composée de **huit groupes** de quatre lettres et chiffres, séparés par des **deux-points (:)**. Par exemple, l'adresse IPv6 **2600:1f18:22ba:8c00:ba86:a05e:a5ba:00FF**. Chaque groupe de l'adresse IPv6 représente **16 bits** au format **hexadécimal**, soit une valeur entre **0 et FFFF**. L'ensemble des huit groupes forme une adresse IPv6 de **128 bits** en binaire.



--------------------------------------------------------------------------


## D/

![[Pasted image 20241028131638.png]]


Le **CIDR (Classless Inter-Domain Routing)** est une méthode pour décrire les **réseaux**. Une adresse CIDR est exprimée par une **adresse IP**, suivie d’une **barre oblique (/**) et d’un **nombre** indiquant le nombre de bits fixes pour le **préfixe de routage**. Les bits restants sont flexibles et permettent de varier les adresses.

Par exemple, dans l'adresse CIDR **192.0.2.0/24**, les **24 premiers bits** sont fixes, laissant **8 bits flexibles**, ce qui permet **256 adresses IP** de 192.0.2.0 à 192.0.2.255. Avec **192.0.2.0/16**, les **16 premiers bits** sont fixes, laissant **16 bits flexibles**, pour **65 536 adresses IP**, de 192.0.0.0 à 192.0.255.255.

Il existe deux exceptions :

- Une adresse CIDR avec **32 bits fixes** (par exemple, **192.0.2.0/32**) représente une **adresse IP unique**, souvent utilisée pour les règles de **pare-feu**.
- **0.0.0.0/0** représente tout l’**Internet**, avec tous les bits flexibles.



--------------------------------------------------------------------------


## E/

![[Pasted image 20241028131755.png]]


Le **modèle OSI (Open Systems Interconnection)** est un **modèle conceptuel** qui explique comment les **données** circulent sur un **réseau**. Il se compose de **sept couches** et décrit les **protocoles** et **adresses** utilisés à chaque couche pour envoyer des données. Par exemple, les **hubs** et **commutateurs** fonctionnent à la **couche 2** (couche de **liaison de données**), tandis que les **routeurs** fonctionnent à la **couche 3** (couche **réseau**). Le modèle OSI aide également à comprendre la **communication** dans un **cloud privé virtuel (VPC)**.

