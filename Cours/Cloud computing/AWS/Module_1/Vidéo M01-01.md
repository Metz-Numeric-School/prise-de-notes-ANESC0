![[Pasted image 20241020150317.png]]
Le **cloud computing** désigne la mise à disposition à la demande de ressources informatiques telles que la puissance de calcul, le stockage, les bases de données, les applications, et bien d'autres, via Internet. Ces services sont facturés en fonction de l'utilisation réelle.





![[Pasted image 20241019002631.png]]
Il peut être difficile d'évaluer le stockage nécessaire à l'avance. Soit il y en plus qu'il n'en faut donc une perte d'argent soit moins donc impossible de satisfaire les besoins d'une entreprise.

## 3 principaux modèles de services :


![[Pasted image 20241019002957.png]]
### Iaas
Concerne les fonctions réseaux, que ce soit des ordinateurs, que ce soit virtuels ou dédiés et fournis un espace de stockage . + haut niveau de flexibilité et de sécurité sur les ressources informatiques 

### Paas
dispense de gérer l'infrastructure sous-jacente ( matériel ou système d'exploitation) par le biais d'automatisation . Permet de se concentrer sur le déploiement et la gestion des applications plutôt que l'approvisionnement

### SaaS
Fournit un produit complet qui est exploité et géré par le fournisseur de services . Dans la plupart des cas, le logiciel fait référence à des applications pour l'utilisateur final . Pas de maintenance à gérer seulement l'utilisation que l'on va en faire

## 3 modèles de déploiement : 

![[Pasted image 20241019003206.png]]
### Cloud
tout est déployé dans le cloud (rien n'est géré en interne)

Une application basée sur le cloud est entièrement déployée dans le cloud, où tous ses composants y sont exécutés. Ces applications peuvent être créées directement dans le cloud ou migrées depuis une infrastructure existante afin de bénéficier des avantages du cloud computing. Les applications cloud peuvent être développées sur une infrastructure de base ou utiliser des services de niveau supérieur qui simplifient la gestion, l'architecture et l'évolutivité de l'infrastructure sous-jacente.

### Hybride
semi cloud semi interne . (ressources connecté avec le système internes)

Un déploiement hybride permet de connecter des infrastructures et des applications entre des ressources basées sur le cloud et des ressources existantes qui ne se trouvent pas dans le cloud. Le scénario de déploiement hybride le plus fréquent relie le cloud à une infrastructure locale. Ce modèle est souvent utilisé par les organisations pour étendre et améliorer leurs infrastructures, en connectant les ressources cloud aux systèmes internes.

### Cloud privé
respecte la nomenclature du cloud mais il n'y a pas vraiment de différence avec un réseaux privé d'entreprise

Le déploiement de ressources sur site, à l'aide de la virtualisation et d'outils de gestion des applications, est parfois désigné sous le terme de **cloud privé**. Bien que le déploiement sur site n'offre pas les nombreux avantages du cloud computing, il est utile pour fournir des ressources dédiées. Dans la plupart des cas, ce modèle de déploiement ressemble à une infrastructure informatique traditionnelle, mais peut intégrer la gestion des applications et des technologies de virtualisation pour optimiser l'utilisation des ressources.


## Similitudes entre AWS et l'informatique traditionnelle sur site


![[Pasted image 20241019004606.png]]

Les parallèles entre Amazon Web Services (AWS) et l'infrastructure informatique sur site sont nombreux. Voici quelques exemples de correspondances entre les services AWS et les éléments traditionnels d’un centre de données :

- **Groupes de sécurité AWS, ACL réseau et IAM**  
    Similaires aux **pare-feu**, aux **listes de contrôle d’accès** (ACL) et aux **administrateurs** en environnement sur site.
    
- **Elastic Load Balancing (ELB) et Amazon Virtual Private Cloud (VPC)**  
    Comparables aux **routeurs**, aux **pipelines réseau** et aux **commutateurs**.
    
- **AMI (Amazon Machine Images) et instances Amazon EC2**  
    Équivalents aux **serveurs sur site**.
    
- **Amazon Elastic Block Store (EBS), Amazon Elastic File System (EFS), Amazon Simple Storage Service (S3) et Amazon Relational Database Service (RDS)**  
    Similaires aux solutions de stockage telles que le **DAS** (Direct Attached Storage), les réseaux **SAN** (Storage Area Network), le **NAS** (Network Attached Storage) et les **RDBMS** (systèmes de gestion de bases de données relationnelles).
    

---

Avec les services et fonctionnalités d'AWS, vous pouvez effectuer presque toutes les tâches qu'un centre de données traditionnel permettrait d'accomplir.