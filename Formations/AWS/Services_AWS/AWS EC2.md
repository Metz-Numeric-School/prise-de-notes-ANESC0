### *Elastic Compute Cloud

![[Pasted image 20241029134928.png]]

La dénomination **EC2** dans **Amazon EC2** signifie **Elastic Compute Cloud**, qui se décompose comme suit :

- **Elastic** : Cela fait référence à la capacité d’**ajuster dynamiquement** le nombre de serveurs utilisés pour prendre en charge une application. Vous pouvez facilement augmenter ou diminuer le nombre d’instances, ainsi que la taille des serveurs existants, en fonction de la demande.

- **Compute** : Ce terme souligne l’objectif principal des utilisateurs, qui est d’exécuter des serveurs pour des tâches telles que l’hébergement d’applications ou le traitement de données. Ces activités nécessitent des **ressources de calcul**, y compris la puissance de traitement (CPU) et la mémoire (RAM).

- **Cloud** : Cela indique que les instances EC2 sont hébergées dans le **cloud**, offrant ainsi des avantages tels que la scalabilité et la flexibilité.

Amazon EC2 fournit des **machines virtuelles** dans le cloud, donnant aux utilisateurs un **contrôle administratif total** sur le système d'exploitation qui s'exécute sur l'instance, que ce soit Windows ou Linux. Les systèmes d'exploitation pris en charge incluent :

- Windows Server 2008, 2012, 2016 et 2019
- Red Hat
- SuSE
- Ubuntu
- Amazon Linux

Un système d'exploitation qui fonctionne sur une machine virtuelle est souvent désigné comme un **système d'exploitation invité**, en opposition au **système d'exploitation hôte**, qui est installé directement sur le serveur physique.

Avec Amazon EC2, vous avez la possibilité de **lancer un nombre illimité d’instances** de n'importe quelle taille dans n'importe quelle zone de disponibilité à travers le monde, et ce, en quelques minutes. Les instances sont lancées à partir d'**Amazon Machine Images (AMI)**, qui sont des modèles de machines virtuelles, abordés plus en détail dans le module.









--------------------------------------------------------------------------



1. **Machines virtuelles** : EC2 permet de lancer des instances (machines virtuelles) avec des configurations personnalisables de CPU, mémoire, stockage, et réseau.
2. **Scalabilité** : EC2 s'adapte à la demande avec des capacités de mise à l'échelle verticale (changer la taille de l'instance) ou horizontale (ajouter plus d'instances).
3. **Sélection d'[[AWS AMI|AWS AMI]]** : Utilisation d'Amazon Machine Images (AMI) pour choisir un système d'exploitation et des logiciels préconfigurés (ex : Linux, Windows).
4. **Types d'instances** : Divers types d’instances optimisées pour différents besoins (standard, calcul, mémoire, GPU, etc.).
5. **Facturation à l'usage** : Modèle de paiement "à la consommation" basé sur le temps d’utilisation des instances.
6. **Sécurité** : Utilisation de **Security Groups** et **VPC** pour isoler et protéger les instances.
7. **Options de stockage** : Utilisation de disques **EBS** (Elastic Block Store) pour le stockage persistant, ou **S3** pour stocker les données.



## Concepts clés d'Amazon EC2:

### 1. *Amazon Machine Image (AMI)*

- **Description** : Un modèle préconfiguré contenant le système d'exploitation, les bibliothèques, les applications, et les configurations nécessaires pour lancer une instance EC2.
- **Utilisation** : Sert de point de départ pour créer une nouvelle instance EC2.
- **Personnalisation** : Tu peux utiliser des AMIs publiques, privées, ou en créer à partir d'une instance existante.

### 2. *Type d'instance*

- **Description** : Les types d’instances déterminent la configuration matérielle de l'instance (CPU, RAM, stockage, réseau).
- **Catégories** : Généraliste (T3, T4), optimisé pour le calcul (C5), optimisé pour la mémoire (R5), stockage élevé (I3), et GPU (P3).
- **Choix** : En fonction des besoins de ton application (ex. optimisation pour le calcul ou la mémoire).

### 3. *Paramètres réseaux*

- **VPC (Virtual Private Cloud)** : Chaque instance EC2 est lancée dans un VPC. Tu peux créer des sous-réseaux privés ou publics.
- **Adresse IP** : Chaque instance reçoit une adresse IP privée dans le VPC. Une adresse IP publique peut être attribuée pour l'accès externe.
- **Passerelle Internet** : Permet aux instances de se connecter à Internet.

### 4. *Rôle IAM (Identity and Access Management)*

- **Description** : Un rôle IAM permet à une instance EC2 d'accéder à d'autres services AWS (ex. S3, DynamoDB) sans stocker de clés API sur l'instance.
- **Utilisation** : Tu attaches un rôle IAM à l'instance pour gérer les permissions d'accès aux services AWS.

### 5. *Données utilisateur (User Data)*

- **Description** : Un script ou des commandes que tu peux spécifier lors du lancement d'une instance EC2, qui s'exécuteront automatiquement au démarrage de l'instance.
- **Utilisation** : Configurer automatiquement le logiciel ou exécuter des tâches au démarrage (ex. mise à jour, installation de paquets).

### 6. *Option de stockage*

- **Elastic Block Store (EBS)** : Disques virtuels attachés à une instance pour le stockage persistant. Ils peuvent être sauvegardés, redimensionnés ou détachés d'une instance.
- **Instance Store** : Stockage temporaire lié à l'instance, qui se perd à l’arrêt ou à la terminaison de l'instance.
- **S3** : Stockage d'objets utilisé pour stocker des fichiers ou des données volumineuses séparées des instances EC2.

### 7. *Balises (Tags)*

- **Description** : Paires clé-valeur que tu peux attacher aux ressources EC2 pour les identifier et les organiser.
- **Utilisation** : Facilite la gestion et l'identification des instances (ex. définir le propriétaire, l'environnement : prod/dev, etc.).

### 8. *Groupe de sécurité*

- **Description** : Fonctionne comme un pare-feu virtuel pour contrôler le trafic entrant et sortant des instances EC2.
- **Paramètres** : Tu peux configurer les règles pour autoriser ou refuser le trafic basé sur les adresses IP, les protocoles, et les ports.
- **Stateful** : Les réponses aux requêtes autorisées sont automatiquement acceptées.

### 9. *Paire de clés (Key Pair)*

- **Description** : Utilisée pour authentifier une connexion SSH (Linux) ou RDP (Windows) à une instance EC2. AWS génère une paire de clés publique/privée.
- **Utilisation** : La clé publique est stockée sur l'instance et la clé privée est utilisée par l'utilisateur pour se connecter de manière sécurisée.

Ces éléments sont essentiels pour la configuration, la gestion, et la sécurité des instances EC2 dans AWS.


