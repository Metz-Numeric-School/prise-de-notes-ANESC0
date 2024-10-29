
# Amazon Route 53

[[AWS Amazon Route 53]]



## A/

![[Pasted image 20241029013006.png]]
Voici la **procédure de base** suivie par **Amazon Route 53** lorsqu'un **utilisateur envoie une requête DNS** :

1. **L’utilisateur envoie une requête DNS** pour accéder à un domaine.
2. Le **résolveur DNS** (qui est généralement géré par le fournisseur d’accès internet de l’utilisateur) contacte **Amazon Route 53** pour obtenir l’**adresse IP** associée au domaine.
3. **Route 53** traite la requête et retourne l’**adresse IP** au résolveur DNS.
4. Le **résolveur DNS** fournit cette **adresse IP** à l’utilisateur, lui permettant d’accéder au service ou au site associé.

Ainsi, Route 53 aide à **diriger le trafic efficacement** vers les **points de terminaison** (par exemple, serveurs web, instances EC2) configurés pour le domaine de l’utilisateur.



## B/

![[Pasted image 20241029013055.png]]



## C/

![[Pasted image 20241029013148.png]]

Le **déploiement multirégions** avec **Amazon Route 53** est particulièrement utile pour **optimiser la performance et la disponibilité** des applications globales. En utilisant Route 53, l’utilisateur est automatiquement dirigé vers l’**équilibreur de charge Elastic Load Balancing (ELB)** le plus proche, améliorant ainsi l’expérience de navigation.

Les avantages principaux du **déploiement multirégions** incluent :

- **Routage basé sur la latence** : Route 53 dirige l’utilisateur vers la **région la plus proche** avec la **latence la plus faible**, garantissant des temps de réponse plus rapides.
- **Routage de répartition de charge** : la charge est équilibrée entre plusieurs **zones de disponibilité**, offrant une **tolérance aux pannes** et une **meilleure gestion des ressources**.

Ces options permettent de **minimiser les interruptions** et de **répondre aux besoins des utilisateurs de manière efficace**, peu importe leur emplacement géographique.




## D /

![[Pasted image 20241029013316.png]]


## E/

![[Pasted image 20241029013415.png]]

Le schéma de **basculement DNS** dans une architecture à plusieurs niveaux utilisant **Amazon Route 53** garantit la **haute disponibilité** d'une application web en dirigeant le trafic en fonction de l'état de santé des composants.

Voici comment configurer ce basculement :

1. **Créer deux enregistrements DNS pour le CNAME `www`** avec une **politique de routage par basculement** :
   - **Politique de routage principale** : elle pointe vers l'**équilibreur de charge** d’Amazon pour la pile d'applications web.
   - **Politique de routage secondaire** : elle dirige vers un **site web statique sur Amazon S3** servant de site de secours.

2. **Activer les vérifications de l'état de Route 53** pour l'enregistrement principal :
   - Si l'enregistrement principal est opérationnel, **Route 53** dirige le trafic vers l'**application web** par défaut.
   - En cas de **panne de l'instance de serveur web** ou de la **base de données**, Route 53 **bascule automatiquement** vers le **site de secours statique**.

Ce mécanisme permet de **minimiser les interruptions** et de garantir que les utilisateurs sont toujours redirigés vers un site fonctionnel.




--------------------------------------------------------------------------



![[Pasted image 20241029013518.png]]

