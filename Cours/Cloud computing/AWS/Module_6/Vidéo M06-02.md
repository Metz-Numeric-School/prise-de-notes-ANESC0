
# Amazon EC2

## A/

![[Pasted image 20241029134820.png]]

L'exécution de serveurs sur site peut s'avérer **coûteuse** et **inefficace** en raison des coûts d'approvisionnement en matériel, de la maintenance des centres de données et de la nécessité de prévoir suffisamment de capacité pour les pics de charge. Cela entraîne souvent des **périodes d'inactivité** où les ressources sont sous-utilisées, ce qui représente un **gaspillage** financier.

Amazon Elastic Compute Cloud (Amazon EC2) offre une solution à ces problèmes en fournissant des **machines virtuelles redimensionnables** et **sécurisées** dans le cloud. EC2 permet aux entreprises d'héberger des applications de la même manière que sur des serveurs traditionnels, mais avec l'avantage de pouvoir adapter dynamiquement les ressources selon les besoins. Les **instances EC2** peuvent gérer une variété de charges de travail, notamment :

- **Serveurs d'application**
- **Serveurs web**
- **Serveurs de bases de données**
- **Serveurs de jeu**
- **Serveurs de messagerie**
- **Serveurs de médias**
- **Serveurs de catalogue**
- **Serveurs de fichiers**
- **Serveurs de calcul**
- **Serveurs proxy**

Ce modèle permet non seulement d'optimiser les coûts, mais aussi d'améliorer la **flexibilité** et la **réactivité** aux variations de la demande.



--------------------------------------------------------------------------


## B/

![[Pasted image 20241029134946.png]]
[[AWS EC2]]


Vous pouvez contrôler le **trafic entrant et sortant** des instances EC2 à l'aide des **groupes de sécurité**. Ces groupes de sécurité agissent comme des pare-feu virtuels, permettant de définir des règles précises concernant le type de trafic autorisé à entrer ou à sortir de vos instances. Voici quelques points clés à retenir :

- **Contrôle granulaire** : Les groupes de sécurité vous permettent de spécifier des règles basées sur l'adresse IP source, le protocole, et les ports, offrant ainsi un contrôle fin sur le trafic réseau.

- **Modification dynamique** : Vous pouvez modifier les règles de groupe de sécurité à tout moment, et ces changements prennent effet immédiatement sans avoir à redémarrer vos instances.

- **Isolation** : Chaque instance peut être associée à plusieurs groupes de sécurité, permettant ainsi de personnaliser la sécurité en fonction des besoins spécifiques de chaque application ou service.

De plus, étant donné que les serveurs s'exécutent dans le **cloud AWS**, vous pouvez créer des solutions qui intègrent **plusieurs services AWS**. Par exemple, vous pourriez utiliser :

- **Amazon S3** pour le stockage de données
- **Amazon RDS** pour des bases de données gérées
- **Amazon CloudFront** pour la diffusion de contenu
- **AWS Lambda** pour des fonctions serverless

Cette intégration entre différents services AWS facilite la création d'architectures complexes, scalables et résilientes, adaptées aux exigences spécifiques de votre application.



--------------------------------------------------------------------------



## C/

![[Pasted image 20241029135330.png]]

Voici un résumé détaillé du processus de création et d'utilisation d'une **Amazon Machine Image (AMI)** à partir d'une instance EC2 :

### Étape 1 : Création de l'AMI
- **À partir d'une instance EC2** : Une AMI peut être créée directement à partir d'une instance EC2 existante. Cela inclut la possibilité d'importer une machine virtuelle existante pour qu'elle devienne une instance EC2. 
- **Utilisation d'une AMI existante** : Vous pouvez également commencer avec une AMI fournie par AWS, comme les AMI **Quick Start**, qui sont préconfigurées pour divers systèmes d'exploitation et applications.

### Étape 2 : Configuration de l'instance
- **Instance non modifiée** : Initialement, l'instance lancée à partir d'une AMI est considérée comme une instance non modifiée.
- **Instance principale** : Vous pouvez ensuite configurer cette instance selon vos besoins en installant des logiciels, en modifiant des paramètres ou en personnalisant le système d'exploitation. Cela donne naissance à une instance que vous avez adaptée pour votre cas d'utilisation spécifique.

### Étape 3 : Capturer l'AMI
- **Création de l'AMI personnalisée** : Une fois que vous avez configuré votre instance principale, vous pouvez la capturer en tant que nouvelle AMI. 
  - Amazon EC2 arrête l'instance pour garantir que l'instantané est cohérent.
  - Il génère ensuite un **instantané** du volume racine de l'instance, qui sera utilisé pour créer l'AMI.

### Étape 4 : Utilisation de l'AMI
- **Lancer de nouvelles instances** : Une fois l'AMI enregistrée, elle peut être utilisée pour lancer de nouvelles instances EC2 dans la même région AWS.
- **Copie d'AMI dans d'autres régions** : Vous avez également la possibilité de copier l'AMI dans d'autres régions AWS. Cela vous permet de déployer des instances EC2 dans différents emplacements géographiques, ce qui peut améliorer la disponibilité et la latence pour vos utilisateurs.

### Conclusion
Le processus de création et de gestion d'AMIs dans AWS permet une flexibilité significative dans la manière dont vous déployez et maintenez vos applications, en facilitant le partage et la réplication des environnements configurés.




--------------------------------------------------------------------------



## D/

![[Pasted image 20241029135449.png]]

Après avoir choisi l'**AMI** pour lancer l'instance, vous devez sélectionner un **type d'instance**. **Amazon EC2** propose plusieurs types d'instances optimisés pour différents cas d'utilisation, basés sur des capacités telles que le **CPU**, la **mémoire**, le **stockage** et la **mise en réseau**.

Chaque type d'instance est disponible en plusieurs **tailles**, vous permettant d'ajuster les ressources selon vos besoins. Les catégories incluent :

- **Polyvalentes**
- **Optimisées pour le calcul**
- **Optimisées pour la mémoire**
- **Optimisées pour le stockage**
- **Calcul accéléré**

Chaque catégorie offre une large sélection de types d'instances adaptés à diverses applications.


--------------------------------------------------------------------------


## E/

![[Pasted image 20241029140234.png]]



Lorsque vous examinez un type d'**instance EC2**, son nom est composé de plusieurs parties. Prenons par exemple le type **t3**. Le **"t"** représente la famille, tandis que le **"3"** indique la génération de ce type d'instance. Ainsi, une instance **t3** est la troisième génération de la famille T. En général, les types d'instances avec un numéro de génération plus élevé sont plus puissants et offrent un meilleur rapport qualité-prix.

La partie suivante du nom indique la **taille de l'instance**. Par exemple, une instance **t3.2xlarge** possède le double de vCPUs et de mémoire par rapport à une instance **t3.xlarge**, qui, elle-même, a le double de ressources qu'une instance **t3.large**.

Enfin, il est important de noter que la **bande passante réseau** est également liée à la taille de l'instance. Si vous exécutez des tâches nécessitant beaucoup de bande passante, vous devrez peut-être opter pour une instance avec des spécifications plus élevées.


--------------------------------------------------------------------------


## F/

![[Pasted image 20241029140315.png]]


Les types d'**instances** varient sur plusieurs points, notamment le type de **CPU**, le nombre de **processeurs** ou de **cœurs**, le type et la quantité de **stockage**, la mémoire et les **performances réseau**. Le graphique présente les différentes catégories d'instances, ainsi que les familles de types d'instances et leurs numéros de génération correspondants.

### Examen de certains types d'instances :

- **Instances T3** :
    
    - Capacité extensible et polyvalente, servant de référence pour les performances en CPU, avec la possibilité de dépasser le seuil de base.
    - Cas d'utilisation : sites web, applications web, environnements de développement, serveurs de développement, référentiels de codes, microservices, environnements de test et applications professionnelles.
- **Instances C5** :
    
    - Optimisées pour les applications de calcul intensives, offrant des performances élevées à un coût avantageux.
    - Cas d'utilisation : modélisation scientifique, traitement par lots, diffusion de publicités, jeux multijoueurs évolutifs, et encodage vidéo.
- **Instances R5** :
    
    - Optimisées pour les applications exigeantes en mémoire.
    - Cas d'utilisation : bases de données hautes performances, analyses de données, bases de données en mémoire, caches distribués à l'échelle web, applications de traitement en temps réel de données Big Data non structurées, clusters Apache Hadoop ou Apache Spark, et autres applications d'entreprise.




--------------------------------------------------------------------------


## G/

![[Pasted image 20241029140428.png]]


--------------------------------------------------------------------------



## H/

![[Pasted image 20241029140453.png]]
Après avoir choisi une **AMI** et un **type d'instance**, spécifiez l'**emplacement réseau** pour déployer l'instance **EC2**. Choisissez la **région** avant de lancer l'assistant. Vérifiez que vous êtes sur la bonne page de la console **Amazon EC2**.

### Attribution d'adresses IP :

- Dans un **VPC** par défaut, AWS attribue une **adresse IP publique** automatiquement.
- Dans un VPC non par défaut, la configuration du **sous-réseau** détermine l'attribution d'adresses IP publiques. Par défaut, aucune adresse IP publique n'est attribuée.

### Options :

Vous pouvez :

- Modifier l'attribut d'adressage IP public du sous-réseau.
- Activer ou désactiver l'attribution d'une adresse IP publique lors du lancement de l'instance.


---------------------------------------------------------------------------


## I/

![[Pasted image 20241029140608.png]]
es instances **EC2** sont souvent utilisées pour exécuter des applications qui effectuent des appels **API** sécurisés vers d'autres services **AWS**. Pour cela, AWS permet d'attribuer un **rôle IAM** (Gestion des identités et des accès) à une instance EC2. Il est fortement déconseillé de stocker les autorisations AWS directement sur une instance, car cela n'est pas sûr.

### Utilisation d'un rôle IAM :

- Un **profil d'instance** sert de conteneur pour un rôle IAM. Lors de la création d'un rôle pour Amazon EC2 via la Console de gestion AWS, un profil d'instance est automatiquement créé avec le même nom que le rôle.
- Lorsque vous lancez une instance EC2 avec un rôle IAM, vous associez ce rôle à l'instance. La liste affichée dans la console comprend les noms des profils d'instance.

### Cas d'utilisation :

Par exemple, un rôle IAM peut accorder des autorisations à une application sur une instance EC2 pour accéder à un compartiment **Amazon S3**.

### Attacher un rôle :

- Vous pouvez attacher un rôle IAM lors du lancement de l'instance ou à une instance déjà en cours d'exécution.
- En définissant un rôle, vous spécifiez quels comptes ou services AWS peuvent l’adopter, ainsi que les actions API et les ressources autorisées.

Si un rôle est modifié, ces changements sont automatiquement appliqués à toutes les instances qui utilisent ce rôle.




--------------------------------------------------------------------------



## J/

![[Pasted image 20241029140709.png]]


Lors de la création d'**instances EC2**, vous pouvez transmettre des **données utilisateur** pour automatiser l'installation et la configuration au lancement. Par exemple, un script de données utilisateur peut appliquer des correctifs, mettre à jour le système d'exploitation, installer des clés de licence ou des logiciels supplémentaires.

### Exemple de script :



- **Première ligne** : Indique que le script doit être exécuté par le shell Bash.
- **Deuxième ligne** : Utilise l'utilitaire **YUM** pour mettre à jour les packages.
- **Troisième ligne** : Installe l'utilitaire **Wget** pour télécharger des fichiers depuis le web.

Pour les instances **Windows**, le script doit être compatible avec l'invite de commandes (commandes par lots) ou **Windows PowerShell**. Consultez la documentation pour plus d’informations : [Scripts de données utilisateur Windows](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-windows-user-data.html).

### Exécution du script :
![[Pasted image 20241029140955.png]]


Le script de données utilisateur s'exécute avec les privilèges du compte racine lors des dernières étapes du démarrage de l'instance :

- **Instances Linux** : Exécuté par le service **cloud-init**.
- **Instances Windows** : Exécuté par **EC2Config** ou **EC2Launch**.

Les données utilisateur s'exécutent uniquement au démarrage initial de l'instance. Si vous souhaitez que votre script s'exécute à chaque démarrage, vous pouvez créer un script de données utilisateur **MIME**, bien que ce processus ne soit pas courant.


--------------------------------------------------------------------------



## K/

![[Pasted image 20241029141041.png]]

Lors du lancement d'une **instance EC2**, vous pouvez configurer les **options de stockage** :

- **Taille du volume racine** : Définissez la taille du volume sur lequel le système d'exploitation invité est installé.
- **Volumes supplémentaires** : Vous pouvez attacher des volumes de stockage supplémentaires lors du lancement de l'instance.
- **Images AMI** : Certaines AMI sont configurées pour lancer plusieurs volumes de stockage par défaut, offrant ainsi un espace distinct du volume racine.

### Options de configuration pour chaque volume :

- **Taille des disques** : Déterminez la capacité de chaque volume.
- **Types de volume** : Choisissez le type de volume (par exemple, SSD, HDD).
- **Conservation des volumes** : Indiquez si le stockage doit être conservé lors de la résiliation de l'instance.
- **Chiffrement** : Vous avez également la possibilité d'activer le chiffrement pour les volumes.


--------------------------------------------------------------------------



## L/

![[Pasted image 20241029141134.png]]


## M/

![[Pasted image 20241029141413.png]]


**Instance 1** : Le volume racine, sur **Amazon EBS**, reste intact lors d'un redémarrage. Les données sur le volume éphémère 1 sont perdues.

**Instance 2** : Le volume racine est sur un stockage d'instance (éphémère 2). Cette instance ne peut pas être arrêtée par l'API EC2 et sera résiliée si le système d'exploitation échoue. Toutes les données sur le volume éphémère 2 seront perdues.

Utilisez **Amazon EBS**, **Amazon EFS** ou **Amazon S3** pour conserver des données importantes à long terme.



--------------------------------------------------------------------------



## M/

![[Pasted image 20241029141554.png]]

![[Pasted image 20241029141609.png]]

![[Pasted image 20241029141620.png]]



## O/
![[Pasted image 20241029141638.png]]

- **En attente** : État initial lors du lancement ou du démarrage d'une instance arrêtée.
- **En cours d'exécution** : L'instance est prête et accessible via Internet.
- **Redémarrage** : Redémarrage de l'instance via la console ou AWS CLI, sans perte de données sur les volumes de stockage d'instance.
- **En cours d'extinction** : État intermédiaire avant la résiliation.
- **Résiliée** : Instance non accessible, mais visible dans la console pendant un certain temps.
- **En cours d'arrêt** : État transitoire avant de devenir complètement arrêtée.
- **Arrêtée** : Instance sans coût opérationnel ; peut être redémarrée sur un nouvel hôte.


--------------------------------------------------------------------------


![[Pasted image 20241029141727.png]]
