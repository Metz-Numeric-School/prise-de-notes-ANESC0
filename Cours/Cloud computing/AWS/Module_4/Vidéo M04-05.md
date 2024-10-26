
# Sécurisation des données sur AWS


## A/

![[Pasted image 20241026014651.png]]


Le **chiffrement des données** est essentiel pour protéger les **données numériques**. Il transforme des données lisibles en données **illisibles** pour ceux qui n'ont pas la **clé secrète**. Ainsi, même si une personne non autorisée accède à vos données, elle ne peut pas les exploiter.

Les **données au repos** sont celles physiquement stockées sur disque ou bande. Vous pouvez créer des **systèmes de fichiers chiffrés** sur AWS pour chiffrer toutes vos données et métadonnées au repos avec l'**algorithme AES-256**. Avec **AWS KMS**, le chiffrement et le déchiffrement sont gérés automatiquement, sans modification nécessaire de vos applications. Si votre organisation doit respecter des **réglementations** sur le chiffrement, AWS recommande de l'activer sur tous les services de stockage de données. Vous pouvez chiffrer les données dans n'importe quel service supporté par **AWS KMS**.



--------------------------------------------------------------------------


## B/

![[Pasted image 20241026014823.png]]

Les **données en transit** désignent celles qui circulent sur le réseau. Leur chiffrement est effectué grâce au protocole **Transport Layer Security (TLS) 1.2** avec un chiffrement **AES-256**. TLS était auparavant connu sous le nom de **Secure Sockets Layer (SSL)**.

**AWS Certificate Manager** est un service qui permet de **mettre en service**, gérer et déployer des **certificats SSL ou TLS** pour sécuriser les communications réseau et établir l'identité des sites web. Avec ce service, vous pouvez demander un certificat et le déployer sur des ressources AWS, comme un **équilibreur de charge** ou des distributions **CloudFront**. AWS Certificate Manager s'occupe également du **renouvellement des certificats**.

Le trafic web utilisant le protocole **HTTP** n'est pas sécurisé, tandis que le trafic **HTTPS** est chiffré via TLS ou SSL, offrant ainsi une protection contre les écoutes et les attaques de type **intercepteur (MITM)**.

Les services AWS prennent en charge le chiffrement des données en transit. Par exemple, une instance **EC2** peut monter un système de fichiers partagé **Amazon EFS**, où tout le trafic est chiffré avec TLS. Un autre exemple est **AWS Storage Gateway**, qui chiffre les données en transit lorsqu'il est connecté à **Amazon S3**.




--------------------------------------------------------------------------

## C/

![[Pasted image 20241026014953.png]]

Par défaut, tous les **compartiments S3** sont **privés**, ce qui signifie que seuls les utilisateurs ayant reçu un accès explicite peuvent y accéder. La gestion et le contrôle de l'accès aux données Amazon S3 sont essentiels. AWS offre plusieurs outils et options pour cela :

- **Amazon S3 Block Public Access** : Ces paramètres supplantent toutes les autres stratégies ou autorisations. En activant **Block Public Access** pour tous les compartiments, vous évitez l'exposition involontaire des données.
    
- **Stratégies IAM** : Elles spécifient que les utilisateurs peuvent accéder à des compartiments et objets spécifiques.
    
- **Stratégies de compartiment** : Elles définissent l'accès à des compartiments ou objets spécifiques, souvent utilisées lorsque l'utilisateur ne peut pas s'authentifier via IAM. Ces stratégies peuvent permettre l'accès entre comptes AWS ou accorder un accès public. Les déclarations de **refus** peuvent être utilisées pour restreindre l'accès, même si des autorisations sont accordées par d'autres stratégies.
    
- **Listes de contrôle d'accès (ACL)** : Bien que moins couramment utilisées, les ACL peuvent être définies sur des compartiments et objets. Si vous choisissez cette méthode, veillez à ne pas accorder un accès trop ouvert.
    
- **AWS Trusted Advisor** : Cette fonctionnalité propose une vérification des autorisations des compartiments pour s'assurer qu'aucun compartiment de votre compte n'a d'autorisations accordant un accès global.



--------------------------------------------------------------------------


