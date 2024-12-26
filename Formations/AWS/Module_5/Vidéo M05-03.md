
# Mise en réseau de VPC


## A/

![[Pasted image 20241028134447.png]]

Une **passerelle Internet** est un composant du **VPC** qui est scalable, redondant et hautement disponible, permettant la communication entre les instances de votre VPC et Internet. Elle a deux objectifs principaux : fournir une cible dans les tables de routage de votre VPC pour le trafic acheminé sur Internet et effectuer une **traduction d'adresses réseau** pour les instances ayant des adresses **IPv4 publiques** attribuées. 

Pour rendre un sous-réseau public, il est nécessaire d'attacher une passerelle Internet à votre VPC et d'ajouter un acheminement à la table de routage pour envoyer le trafic non local via cette passerelle vers Internet (0.0.0.0/0).


--------------------------------------------------------------------------



## B/

![[Pasted image 20241028134545.png]]


Une **passerelle de traduction d'adresses réseau (NAT)** permet aux instances d'un sous-réseau privé de se connecter à Internet ou à d'autres services AWS, tout en empêchant Internet d'initier une connexion avec ces instances. 

Pour créer une passerelle NAT, vous devez spécifier le sous-réseau public qu'elle occupera et associer une **adresse IP Elastic** à la passerelle lors de sa création. Après avoir créé la passerelle NAT, il est nécessaire de mettre à jour la table de routage associée à vos sous-réseaux privés pour diriger le trafic Internet vers cette passerelle, permettant ainsi aux instances de ces sous-réseaux privés de communiquer avec Internet. Alternativement, vous pouvez utiliser une **instance NAT** dans un sous-réseau public de votre VPC.

Cependant, une passerelle NAT est un service géré qui offre une meilleure disponibilité, une bande passante plus élevée et moins de tâches d'administration. Pour les cas d'utilisation courants, AWS recommande d'utiliser une passerelle NAT plutôt qu'une instance NAT.


--------------------------------------------------------------------------



## C/

![[Pasted image 20241028134712.png]]

Le **partage de VPC** permet aux clients de partager des sous-réseaux avec d'autres comptes AWS au sein de la même organisation dans **AWS Organizations**. 

Cela permet à plusieurs comptes AWS de créer leurs ressources d'application, telles que des instances **Amazon EC2**, des bases de données **Amazon RDS**, des clusters **Amazon Redshift** et des fonctions **AWS Lambda**, dans des VPC partagés et gérés de manière centralisée. 

Dans ce modèle, le compte propriétaire du VPC partage un ou plusieurs sous-réseaux avec d'autres comptes participants. Après le partage, les participants peuvent visualiser, créer, modifier et supprimer leurs ressources d'application dans les sous-réseaux partagés, tout en n'ayant pas accès aux ressources appartenant à d'autres participants ou au propriétaire du VPC.

Les avantages du partage de VPC incluent :

- **Séparation des tâches** : gestion centralisée de la structure du VPC, du routage et de l'attribution des adresses IP.
- **Responsabilité** : les propriétaires d'applications restent responsables de leurs ressources, comptes et groupes de sécurité.
- **Groupes de sécurité** : les participants peuvent référencer les ID de groupe de sécurité des autres.
- **Efficacité** : utilisation optimisée des ressources dans les sous-réseaux, y compris les VPN et **AWS Direct Connect**.
- **Aucune limite stricte** : évitement des limites strictes (par exemple, 50 interfaces virtuelles par connexion AWS Direct Connect grâce à une architecture réseau simplifiée).
- **Optimisation des coûts** : réduction des coûts par la réutilisation des passerelles NAT, des points de terminaison d'interface VPC et le trafic intra-zone de disponibilité.

En résumé, le partage de VPC dissocie les comptes et les réseaux, réduisant le nombre de VPC gérés de manière centralisée tout en les rendant plus grands, ce qui est particulièrement bénéfique pour les applications hautement interconnectées.



--------------------------------------------------------------------------



## D /

![[Pasted image 20241028135311.png]]

Une **connexion d'appairage de VPC** est une connexion réseau entre deux **VPC** qui permet d'acheminer le **trafic** de manière privée. Les **instances** des deux VPC peuvent communiquer comme si elles faisaient partie du même réseau. Vous pouvez créer une connexion d'appairage entre vos propres VPC, avec un VPC dans un autre compte **AWS**, ou avec un VPC dans une autre **région AWS**. Lors de la configuration de la connexion, vous devez créer des **règles** dans votre **table de routage** pour permettre la communication entre les VPC via la **ressource d'appairage**. Par exemple, dans la table de routage du VPC A, vous définissez la destination comme l'adresse IP du VPC B et la cible comme l'**ID** de la ressource d'appairage, et vice versa dans la table de routage du VPC B.

Cependant, l'appairage de VPC présente certaines **restrictions** :

- Les **plages d'adresses IP** ne peuvent pas se chevaucher.
- L'appairage **transitif** n'est pas pris en charge. Par exemple, si vous avez trois VPC (A, B et C), et que le VPC A est connecté au VPC B et au VPC C, le VPC B n'est pas automatiquement connecté au VPC C. Vous devez établir cette connectivité explicitement.
- Vous ne pouvez avoir qu'une **seule ressource d'appairage** entre deux VPC identiques.




--------------------------------------------------------------------------




## E/

![[Pasted image 20241028135437.png]]


Par défaut, les **instances** que vous lancez dans un **VPC** ne peuvent pas communiquer avec un **réseau distant**. Pour connecter votre VPC à ce réseau distant (c'est-à-dire créer un **réseau privé virtuel** ou une connexion **VPN**), suivez ces étapes :

1. Créez un **périphérique de passerelle virtuelle** (appelé passerelle de réseau privé virtuel **(VPN)**) et attachez-le à votre VPC.
2. Définissez la **configuration** du périphérique VPN ou de la passerelle client. La passerelle client n'est pas un périphérique, mais une **ressource AWS** qui fournit des informations à AWS sur votre périphérique VPN.
3. Créez une **table de routage personnalisée** pour diriger le trafic lié au **centre de données** d'entreprise vers la passerelle VPN. Vous devez également mettre à jour les **règles** du groupe de sécurité.
4. Établissez une connexion **AWS Site-to-Site VPN** pour relier les deux systèmes.
5. Configurez le **routage** pour faire passer le trafic via la connexion.



--------------------------------------------------------------------------




## F/

![[Pasted image 20241028135603.png]]

L'un des défis de la **communication en réseau** est la **performance** du réseau. Les performances peuvent être dégradées si votre centre de **données** est éloigné de votre région **AWS**. Pour de telles situations, **AWS** propose **AWS Direct Connect (DX)**. AWS Direct Connect vous permet d'établir une **connexion réseau privée** dédiée entre votre réseau et celui des emplacements DX. Cette connexion privée peut :

- Réduire les **coûts** de votre réseau,
- Augmenter le **débit** de la bande passante,
- Fournir une **expérience réseau** plus constante que les connexions basées sur Internet.

DX utilise des **réseaux locaux virtuels (VLAN)** conformes à la norme ouverte **802.1q**




--------------------------------------------------------------------------





## G/

![[Pasted image 20241028135656.png]]

Un **point de terminaison** d'un **VPC** est un **périphérique virtuel** qui vous permet de connecter en privé votre VPC aux **services AWS** pris en charge et aux services de point de terminaison d'un VPC basés sur la technologie **AWS PrivateLink**. La connexion à ces services ne nécessite pas de **passerelle Internet**, de **périphérique NAT**, de **connexion VPN** ni de **connexion AWS Direct Connect**. Les **instances** de votre VPC n'ont pas besoin d'adresses IP publiques pour communiquer avec les ressources du service, et le trafic entre votre VPC et les autres services ne quitte pas le réseau **Amazon**.

Il existe deux types de points de terminaison d'un VPC :

1. **Point de terminaison d'interface** : Cela vous permet de vous connecter à des services basés sur AWS PrivateLink, notamment certains services AWS, des services hébergés par d'autres clients AWS et des membres du **réseau de partenaires AWS (APN)**. Le propriétaire du service est le **fournisseur**, et vous, en tant que mandataire créant le point de terminaison d'interface, êtes l'utilisateur du service. Vous êtes facturé pour la création et l'utilisation d'un point de terminaison d'interface avec un service, avec des tarifs d'utilisation horaires et de traitement des données. Consultez la documentation AWS pour une liste des points de terminaison d'interface pris en charge.
    
2. **Points de terminaison de passerelle** : L'utilisation de points de terminaison de passerelle n'entraîne aucun frais supplémentaire. Cependant, des frais standard pour le transfert de données et l'utilisation des ressources s'appliquent.




--------------------------------------------------------------------------




## H/

![[Pasted image 20241028135754.png]]


Vous pouvez **configurer vos VPC** de plusieurs manières et profiter de nombreuses **options de connectivité** et de **passerelles**. Ces options incluent **AWS Direct Connect** (via des passerelles DX), des **passerelles NAT**, des **passerelles Internet**, et l'**appairage de VPC**, entre autres. Il n'est pas rare que des clients AWS utilisent des **centaines de VPC** répartis sur plusieurs comptes et régions AWS pour répondre aux besoins de divers secteurs d'activité, équipes, et projets.

Cependant, la configuration de la **connectivité** entre ces VPC peut devenir complexe. Toutes les options de connectivité sont strictement **point à point**, ce qui signifie que le nombre de connexions de VPC à VPC peut augmenter rapidement. À mesure que vous augmentez le nombre de **charges de travail** sur AWS, vous devez être capable de **mettre à l'échelle vos réseaux** sur plusieurs comptes et VPC pour suivre le rythme de la croissance.

Bien que vous puissiez utiliser l'**appairage de VPC** pour connecter des paires de VPC, gérer la connectivité point à point sur de nombreux VPC sans pouvoir gérer les politiques de connectivité de manière centralisée peut s'avérer **coûteux** et difficile sur le plan opérationnel. Pour la connectivité sur site, vous devez attacher votre **VPN** à chaque VPC individuel, ce qui peut être long à mettre en place et difficile à gérer lorsque les VPC se comptent par centaines.

Pour résoudre ce problème, vous pouvez utiliser **AWS Transit Gateway** afin de simplifier votre modèle de mise en réseau. Avec AWS Transit Gateway, vous devez créer et gérer une seule connexion depuis la passerelle centrale vers chaque VPC, centre de données sur site, ou bureau à distance. Une **passerelle de transit** agit comme un centre contrôlant la manière dont le trafic est acheminé entre tous les réseaux connectés, fonctionnant comme des **rayons**. 

Ce modèle en étoile simplifie considérablement la gestion et réduit les coûts d'exploitation, car chaque réseau doit simplement se connecter à la passerelle de transit et non à tous les autres réseaux. Chaque nouveau VPC est connecté à la passerelle de transit et est automatiquement disponible pour tous les autres réseaux connectés à cette passerelle, facilitant ainsi la mise à l'échelle de votre réseau au fur et à mesure de sa croissance.




--------------------------------------------------------------------------



![[Pasted image 20241028135942.png]]


