
# Introduction à AWS

--------------------------------------------------------------------------

## A/

![[Pasted image 20241019133026.png]]

Un **service web** est un logiciel accessible via Internet ou un réseau privé (intranet). Il utilise des formats standardisés, tels que **XML** (Extensible Markup Language) ou **JSON** (JavaScript Object Notation), pour les échanges entre les demandes et réponses d’une **API**.

Les services web sont **indépendants** du système d'exploitation ou du langage de programmation. Ils se décrivent automatiquement à l'aide d'un **fichier de définition d'interface** et sont **détectables** sur le réseau.

--------------------------------------------------------------------------


## B/

![[Pasted image 20241019133856.png]]
### Amazon Web Services (AWS)

**Amazon Web Services (AWS)** est une plateforme cloud sécurisée qui propose une vaste gamme de produits basés sur le cloud à l'échelle mondiale. Étant donné que ces produits sont accessibles via Internet, vous bénéficiez d’un accès à la demande à diverses ressources informatiques, notamment :

- **Stockage de calcul**
- **Services de mise en réseau**
- **Bases de données**
- **Autres ressources informatiques nécessaires à vos projets**

#### Mise en service rapide

Vous pouvez mettre en service et lancer immédiatement des ressources AWS, qui seront disponibles en quelques minutes.

#### Flexibilité et évolutivité

AWS offre une grande **flexibilité**. Votre environnement AWS peut être :

- Reconfiguré et mis à jour à la demande
- Mis à l’échelle automatiquement (à la hausse ou à la baisse) pour s'adapter aux schémas d'utilisation
- Fermé temporairement ou définitivement

Les frais associés aux services AWS deviennent ainsi des **dépenses opérationnelles**, remplaçant les dépenses en capital.

#### Intégration des services

Les services AWS sont conçus pour interagir les uns avec les autres, prenant en charge presque tous les types d’applications et de charges de travail. Pensez à ces services comme à des **blocs de construction** que vous pouvez assembler rapidement pour créer des solutions évolutives et sophistiquées, puis ajuster en fonction de l’évolution de vos besoins.

--------------------------------------------------------------------------




## C/

![[Pasted image 20241019144234.png]]

Les **services AWS** sont organisés en différentes catégories, chacune contenant un ou plusieurs services. Vous pouvez choisir les services souhaités dans ces catégories pour concevoir et créer vos solutions adaptées à vos besoins.


### Exemple d'application de base de données avec AWS

![[Pasted image 20241020155749.png]]


Supposons que vous souhaitiez créer une **application de base de données**. Voici comment vous pouvez utiliser différents services AWS :

1. **Collecte des données**  
    Vos clients peuvent envoyer des données à vos **instances Amazon Elastic Compute Cloud (Amazon EC2)**, qui font partie de la catégorie **Calcul**. Ces serveurs EC2 regroupent les données par incréments d’une minute et ajoutent un objet par client à **Amazon Simple Storage Service (Amazon S3)**, le service de stockage d'AWS que vous avez choisi d'utiliser.
    
2. **Alimentation de l'application**  
    Vous pouvez ensuite utiliser une **base de données non relationnelle** comme **Amazon DynamoDB** pour alimenter votre application. Par exemple, vous pouvez créer un index afin de localiser tous les objets collectés sur une certaine période pour un client donné.
    
3. **Configuration du réseau**  
    Vous pouvez décider d’exécuter ces services dans **Amazon Virtual Private Cloud (Amazon VPC)**, qui appartient à la catégorie **Réseau**.
    

#### Conclusion

Cet exemple simple illustre comment vous pouvez sélectionner des services web dans différentes catégories et les combiner pour créer une solution, ici une application de base de données. Bien entendu, les solutions que vous créez peuvent être beaucoup plus complexes et adaptées à vos besoins spécifiques.

--------------------------------------------------------------------------




## D/

![[Pasted image 20241019144306.png]]

Le **service** que vous choisissez d'utiliser dépend de vos **objectifs métier** et de vos **besoins technologiques**. Dans l'exemple précédent, nous avons utilisé **Amazon EC2** comme service de calcul, mais il existe de nombreuses autres options disponibles sur AWS. Voici quelques-unes des offres de calcul AWS que vous pouvez envisager en fonction de différents cas d'utilisation :

- **Amazon EC2** : Vous souhaitez avoir un **contrôle total** sur vos ressources informatiques AWS.
- **AWS Lambda** : Vous souhaitez exécuter votre code sans avoir à **gérer ni allouer** des serveurs.
- **AWS Elastic Beanstalk** : Vous souhaitez un service qui **déploie, gère et met à l'échelle** vos applications web pour vous.
- **Amazon Lightsail** : Vous avez besoin d’une **plateforme cloud légère** pour une application web simple.
- **AWS Batch** : Vous devez exécuter des **centaines de milliers** de charges de travail par lots.
- **AWS Outposts** : Vous souhaitez exécuter l'infrastructure AWS dans votre **centre de données sur site**.
- **Amazon Elastic Container Service (Amazon ECS)**, **Amazon Elastic Kubernetes Service (Amazon EKS)** ou **AWS Fargate** : Vous souhaitez mettre en œuvre une **architecture de conteneurs** ou de **microservices**.
- **VMware Cloud on AWS** : Vous disposez d'une plateforme de **virtualisation de serveur** sur site que vous souhaitez migrer vers AWS.

#### Conclusion :

Vous pouvez sélectionner un grand nombre de services dans d’autres catégories, et le nombre d’offres ne cesse de croître. Cela vous permet de choisir la solution la plus adaptée à vos besoins spécifiques.

--------------------------------------------------------------------------



## E/

![[Pasted image 20241019144414.png]]
L'éventail de **services AWS** peut être intimidant lorsque vous commencez à utiliser le cloud. Ce cours se concentre sur certains des services les plus courants dans les catégories suivantes :

- **Calcul**
- **Stockage**
- **Base de données**
- **Mise en réseau et diffusion de contenu**
- **Sécurité, identité et conformité**
- **Gestion et gouvernance**
- **Gestion des coûts AWS**

### Légende des Services AWS

Voici quelques-uns des services AWS que vous allez explorer :

- Amazon Elastic Block Store **(Amazon EBS)**
- Amazon Elastic Compute Cloud **(Amazon EC2)**
- Amazon Elastic Container Registry **(Amazon ECR)**
- Amazon Elastic Container Service **(Amazon ECS)**
- Amazon Elastic File System **(Amazon EFS)**
- Amazon Elastic Kubernetes Service **(Amazon EKS)**
- Amazon Relational Database Service **(Amazon RDS)**
- Amazon Simple Storage Service **(Amazon S3)**
- Amazon Virtual Private Cloud **(Amazon VPC)**
- AWS Identity and Access Management **(IAM)**
- AWS Key Management Service **(AWS KMS)**

--------------------------------------------------------------------------


## F/

![[Pasted image 20241019145430.png]]
Vous vous demandez peut-être comment accéder au large éventail de services proposés par **AWS**. Trois options s’offrent à vous pour créer et gérer des ressources sur **AWS Cloud** :

1. **AWS Management Console**  
    La console fournit une **interface graphique** pour la majorité des fonctionnalités proposées par AWS.  
    _Remarque : il arrive que les nouvelles fonctions ne soient pas toutes incluses dans la console lors du lancement initial de la fonction._
    
2. **Interface de ligne de commande AWS (AWS CLI)**  
    L’interface de ligne de commande AWS fournit une suite d’utilitaires qui peuvent être lancés à partir d’un **script de commande** sous Linux, macOS ou Microsoft Windows.
    
3. **Kits de développement logiciel (SDK)**  
    AWS fournit des **packages** qui permettent d’accéder à AWS dans divers langages de programmation. Cela facilite non seulement l’utilisation d’AWS dans vos applications existantes, mais permet également de créer des applications qui déploient et surveillent des systèmes complexes entièrement via le code.
    

Ces trois options sont basées sur une **API commune de type REST** qui sert de base à AWS
