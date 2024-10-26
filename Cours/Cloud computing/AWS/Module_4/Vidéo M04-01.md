# Modèle de responsabilité partagée AWS

## A/

![[Pasted image 20241025031832.png]]

Le modèle de responsabilité partagée d'AWS répartit les rôles de sécurité entre AWS et le client, allégeant la charge opérationnelle tout en offrant flexibilité et contrôle. Voici comment les responsabilités sont réparties :

- **Responsabilité d'AWS (Sécurité du cloud)** : AWS gère et sécurise l'infrastructure sous-jacente, depuis la sécurité physique des centres de données jusqu'aux couches de virtualisation, matériels, logiciels et réseaux exécutant les services d'AWS Cloud.
    
- **Responsabilité du client (Sécurité dans le cloud)** : Le client doit sécuriser ses propres données et configurations, en s'assurant du chiffrement des données au repos et en transit, de la gestion des autorisations et des identifiants de sécurité, ainsi que de la mise à jour et de la configuration sécurisée de ses instances et systèmes d'exploitation.
    

Ce modèle permet une division claire des tâches, garantissant que l'infrastructure est sécurisée par AWS, tandis que le client a le contrôle sur la sécurité de ses propres données et configurations.

--------------------------------------------------------------------------


## B/

![[Pasted image 20241025032036.png]]

Dans un modèle de responsabilité partagée, AWS est responsable de l'exploitation, de la gestion et du contrôle des composants critiques, notamment le système d'exploitation hôte bare metal, la virtualisation des hyperviseurs et la sécurité physique des installations. AWS protège l'infrastructure mondiale qui prend en charge tous les services AWS Cloud, y compris les régions, les zones de disponibilité et les emplacements périphériques.



--------------------------------------------------------------------------




## C/
![[Pasted image 20241025032242.png]]

Dans le cadre du modèle de responsabilité partagée d'AWS, AWS sécurise et maintient l'infrastructure cloud, tandis que les clients sont responsables de la sécurité de tout ce qu'ils déploient sur le cloud. Cela inclut :

- La sécurisation des systèmes d'exploitation d'instance
- La sécurisation des applications déployées
- Les configurations de groupes de sécurité, pare-feu et réseau
- La gestion sécurisée des comptes

Les clients ont un contrôle total sur leur contenu (stockage, utilisation, localisation, chiffrement) et la gestion des droits d'accès.




--------------------------------------------------------------------------


## D/

![[Pasted image 20241025032541.png]]

Dans le modèle de services cloud, l'infrastructure en tant que service (IaaS) et la plateforme en tant que service (PaaS) se distinguent par le niveau de gestion et de responsabilité.

- **IaaS** (Infrastructure as a Service) offre aux clients un contrôle total sur l'infrastructure, comme avec **Amazon EC2**. Cela inclut la configuration des systèmes d'exploitation, les correctifs de sécurité, les applications et les configurations réseau. Les clients sont responsables de la gestion complète de leurs ressources.
    
- **PaaS** (Platform as a Service) simplifie la gestion en fournissant une plateforme où AWS gère l'infrastructure sous-jacente. Des services comme **AWS Lambda** ou **Amazon RDS** permettent aux clients de se concentrer uniquement sur leurs applications et données, tandis qu'AWS gère la sécurité, les mises à jour et la maintenance de l'infrastructure.
    

Dans les deux cas, la sécurité et la classification des données restent des responsabilités majeures du client.



--------------------------------------------------------------------------


## E/

![[Pasted image 20241025032731.png]]
Le **logiciel en tant que service** (SaaS) désigne des applications hébergées centralement, accessibles via un navigateur, une application mobile ou une API. Les clients n'ont pas besoin de gérer l'infrastructure sous-jacente. Les services AWS comme **AWS Trusted Advisor**, **AWS Shield** et **Amazon Chime** sont des exemples de SaaS.

- **AWS Trusted Advisor** : Cet outil analyse l'environnement AWS d'un client et propose des recommandations pour optimiser les ressources selon les bonnes pratiques AWS.
    
- **AWS Shield** : Un service de protection contre les attaques DDoS, avec une surveillance continue et des mécanismes d'atténuation automatique des risques.
    
- **Amazon Chime** : Un service de communication permettant des réunions, des discussions et des appels professionnels, facturé à l'utilisation.
    

Les solutions SaaS simplifient la gestion pour les clients, qui n'ont pas à se préoccuper de l'infrastructure ou de la maintenance du service.



## F/

![[Pasted image 20241025032904.png]]

