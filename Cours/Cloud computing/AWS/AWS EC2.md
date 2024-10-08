### *Elastic Compute Cloud

est un service de calcul cloud qui permet de louer des machines virtuelles (instances) pour exécuter des applications dans le cloud AWS. Il offre une flexibilité et une échelle de calcul élastique, ajustable en fonction des besoins.

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


