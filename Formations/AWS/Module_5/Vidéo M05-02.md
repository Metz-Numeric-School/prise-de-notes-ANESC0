

# Amazon VPC


## A/

![[Pasted image 20241028132009.png]]

[[AWS VPC]]

**Amazon VPC** permet de créer un **cloud privé virtuel** isolé dans **AWS** pour lancer des **ressources**. Vous pouvez contrôler la **mise en réseau** : choisir les **adresses IP**, créer des **sous-réseaux**, et configurer **tables de routage** et **passerelles**. Par exemple, un **sous-réseau public** peut être dédié aux **serveurs web** avec accès à **Internet**, tandis qu’un **sous-réseau privé** peut contenir des **bases de données** sans accès public. Des **couches de sécurité** comme les **groupes de sécurité** et **ACL** renforcent la protection des **instances EC2**.


--------------------------------------------------------------------------



## B/

![[Pasted image 20241028132657.png]]


**Amazon VPC** permet de créer des **clouds privés virtuels** (VPC), qui sont des **réseaux virtuels isolés** dans **AWS** et spécifiques à chaque **compte**. Un VPC appartient à une seule **région AWS** mais peut couvrir plusieurs **zones de disponibilité**. Une fois créé, un VPC peut être divisé en **sous-réseaux**, chacun étant une **plage d'adresses IP** dans une zone de disponibilité unique. Les sous-réseaux peuvent être **publics** (avec accès Internet) ou **privés** (sans accès direct à Internet).



--------------------------------------------------------------------------




## C/

![[Pasted image 20241028132758.png]]


Les **adresses IP** permettent aux ressources de votre **VPC** de communiquer entre elles et avec Internet. Lors de la création d’un VPC, vous assignez un **bloc d'adresse CIDR IPv4** fixe, donc le choix est crucial. Ce bloc peut aller de **/16** (65 536 adresses) à **/28** (16 adresses). Vous pouvez également associer un **bloc CIDR IPv6** pour attribuer des adresses IPv6 aux ressources. Les sous-réseaux dans un VPC peuvent utiliser des **sous-ensembles** de ce bloc CIDR sans chevauchement, évitant ainsi les **adresses IP dupliquées** dans le même VPC.



--------------------------------------------------------------------------



## D/

![[Pasted image 20241028132939.png]]

- **Sous-réseau** : Nécessite son propre bloc d'adresses CIDR.
- **Réservations d'adresses IP** : Pour chaque bloc CIDR spécifié, AWS réserve **5 adresses IP** qui ne peuvent pas être utilisées.

#### Adresses réservées par AWS :

1. **Adresse réseau**
2. **Routeur local de VPC** (pour les communications internes)
3. **Résolution DNS**
4. **Utilisation future**
5. **Adresse de diffusion réseau**

- **Exemple** : Pour un sous-réseau avec le bloc CIDR IPv4 **10.0.0.0/24** (256 adresses IP au total) :
    - **Adresses IP disponibles** : 256 - 5 = **251 adresses IP**.



--------------------------------------------------------------------------



## E/

![[Pasted image 20241028133201.png]]


- **Attribution d'adresse IP publique** :
    
    - Pour qu'une **adresse IP publique** soit attribuée à une instance lors de sa création, il faut modifier les paramètres d'attribution automatique de l'**adresse IP publique** du **sous-réseau**.
- **Adresse IP élastique** :
    
    - **Définition** : C'est une **adresse IPv4 publique** statique, optimisée pour le **cloud computing dynamique**.
    - **Utilisation** : Peut être associée à n'importe quelle **instance** ou **interface réseau** dans un **VPC**.
    - **Avantage** : Permet de réassigner rapidement l'adresse à une autre instance en cas d'échec, facilitant ainsi la continuité du service.
    - **Déplacement des attributs** : Associer l'adresse à l'**interface réseau** permet de transférer tous ses attributs d'une instance à une autre en une seule étape.
- **Coûts** :
    
    - Des **frais supplémentaires** peuvent être appliqués pour l'utilisation d'**adresses IP élastiques**. Il est important de **libérer** ces adresses lorsqu'elles ne sont plus nécessaires.




--------------------------------------------------------------------------




## F/

![[Pasted image 20241028133734.png]]


--------------------------------------------------------------------------


## G/

![[Pasted image 20241028134108.png]]

Une **table de routage** contient un ensemble de règles, appelées **acheminements**, qui dirigent le trafic réseau depuis votre sous-réseau. 

Chaque acheminement spécifie une **destination** (le bloc d'adresse CIDR vers lequel le trafic doit aller) et une **cible** (l'endroit par lequel le trafic de destination est envoyé). Par défaut, chaque table de routage contient un acheminement local pour la communication au sein du **VPC**.

Vous pouvez personnaliser ces tables de routage en ajoutant des acheminements, bien que l'entrée d'acheminement local utilisée pour les communications internes ne puisse pas être supprimée. Chaque sous-réseau d'un **VPC** doit être associé à une table de routage. La **table de routage principale** est celle qui est automatiquement attribuée à votre **VPC** et contrôle le routage de tous les sous-réseaux qui ne sont pas explicitement associés à une autre table de routage.

Un sous-réseau ne peut être associé qu'à une seule table de routage à la fois, mais plusieurs sous-réseaux peuvent être associés à la même table de routage.






--------------------------------------------------------------------------


![[Pasted image 20241028134211.png]]





