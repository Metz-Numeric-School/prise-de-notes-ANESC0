# Services et catégories de services AWS


### *Infrastructure Mondiale AWS*

1. **Régions** : Zones géographiques qui contiennent plusieurs zones de disponibilité.
2. **Zones de disponibilité** : Emplacements distincts au sein d'une région, isolés les uns des autres pour assurer la tolérance aux pannes.
3. **Points de présence** : Comprennent des emplacements périphériques pour la mise en réseau et la diffusion de contenu.

### *Services AWS*

AWS propose une vaste gamme de services organisés en différentes catégories. Voici un aperçu des services les plus utilisés :

![[Pasted image 20241023010129.png]]


#### *1. Services de stockage*

![[Pasted image 20241023010158.png]]


- **Amazon Simple Storage Service (S3)** : Stockage d'objets évolutif et sécurisé.
- **Amazon Elastic Block Store (EBS)** : Stockage par bloc pour les instances EC2.
- **Amazon Elastic File System (EFS)** : Système de fichiers élastique, NFS, géré.
- **Amazon S3 Glacier** : Stockage à faible coût pour l'archivage et la sauvegarde.


--------------------------------------------------------------------------


#### *2. Services de calcul*

![[Pasted image 20241023010243.png]]


- **Amazon Elastic Compute Cloud (Amazon EC2)** : Offre une capacité de calcul redimensionnable via des machines virtuelles dans le cloud.
- **Amazon EC2 Auto Scaling** : Permet d'ajuster automatiquement le nombre d'instances EC2 selon les besoins.
- **Amazon Elastic Container Service (Amazon ECS)** : Orchestration de conteneurs hautement performante et évolutive, prenant en charge les conteneurs Docker.
- **Amazon Elastic Container Registry (Amazon ECR)** : Registre géré pour stocker, gérer et déployer des images de conteneur Docker.
- **AWS Elastic Beanstalk** : Service pour déployer et mettre à l'échelle des applications web sur des serveurs comme Apache et IIS.
- **AWS Lambda** : Exécution de code sans gestion de serveurs, facturation basée sur le temps de calcul utilisé.
- **Amazon Elastic Kubernetes Service (Amazon EKS)** : Gestion et mise à l'échelle des applications conteneurisées avec Kubernetes sur AWS.
- **AWS Fargate** : Moteur de calcul pour exécuter des conteneurs sans gérer de serveurs ou clusters.

--------------------------------------------------------------------------


#### *3. Services de base de données*

![[Pasted image 20241023010311.png]]


- **Amazon RDS** : Simplifie la gestion des bases de données relationnelles avec redimensionnement et automatisation.
- **Amazon Aurora** : Base de données relationnelle compatible MySQL/PostgreSQL, plus rapide que les versions standard.
- **Amazon Redshift** : Data warehouse pour requêtes analytiques à grande échelle sur des pétaoctets de données.
- **Amazon DynamoDB** : Base de données NoSQL rapide (millisecondes), avec sécurité et options de sauvegarde.

--------------------------------------------------------------------------


#### *4. Services de mise en réseau et de diffusion de contenu*

![[Pasted image 20241023010341.png]]


- **Amazon Virtual Private Cloud (VPC)** : Réseaux isolés dans le cloud.
- **Elastic Load Balancing** : Répartition automatique du trafic.
- **Amazon CloudFront** : CDN pour la diffusion de contenu.
- **AWS Direct Connect** : Connexion réseau privée à AWS.
- **Amazon Route 53** : Service DNS scalable.
- **AWS Transit Gateway** : Connecte plusieurs VPC et réseaux.
- **AWS VPN** : Connexion VPN sécurisée vers AWS.

--------------------------------------------------------------------------


#### *5. Services de sécurité, d'identité et de conformité*

![[Pasted image 20241023010414.png]]


- **AWS IAM** : Gère l'accès sécurisé aux services et ressources AWS avec des utilisateurs et groupes.
- **AWS Organizations** : Gère les services et actions autorisées dans plusieurs comptes.
- **Amazon Cognito** : Permet la création de comptes et l'authentification des utilisateurs pour les applications.
- **AWS Artifact** : Accès aux rapports de sécurité et de conformité d'AWS.
- **AWS KMS** : Gère des clés pour le chiffrement dans les services AWS.
- **AWS Shield** : Protection contre les attaques D


--------------------------------------------------------------------------


#### *6. Services de gestion des coûts*

![[Pasted image 20241023010454.png]]

- **AWS Budgets** : Budgétisation personnalisée.
- **AWS Cost Explorer** : Visualisation des coûts et utilisation.
- **AWS Cost and Usage Report** : Détails sur l'utilisation et les coûts.
- **AWS Pricing Calculator** : Estimation des coûts des services AWS.

--------------------------------------------------------------------------


#### *7. Services de gestion et de gouvernance*

![[Pasted image 20241023010924.png]]


- **Console de gestion AWS** : Interface web pour accéder et gérer votre compte AWS.
- **AWS Config** : Suivi de l'inventaire des ressources et des modifications apportées.
- **Amazon CloudWatch** : Surveillance des ressources et des applications.
- **AWS Auto Scaling** : Dimensionnement automatique des ressources en fonction de la demande.
- **Interface de ligne de commande AWS** : Outil pour gérer les services AWS via des commandes.
- **AWS Trusted Advisor** : Outils pour optimiser performances et sécurité.
- **AWS Well-Architected Tool** : Vérification et amélioration des charges de travail.
- **AWS CloudTrail** : Suivi de l'activité des utilisateurs et de l'utilisation de l'API.