# AWS Identity and Access Management (IAM)


## A/

![[Pasted image 20241025033401.png]]



**AWS Identity and Access Management (IAM)** est un service qui permet de gérer et de contrôler les accès aux services AWS (calcul, stockage, bases de données, etc.). Il centralise la gestion des autorisations, en définissant qui peut accéder à quelles ressources et comment. IAM permet un contrôle précis des accès, y compris la gestion des appels d'API.

Avec **IAM**, vous pouvez :

- Gérer les utilisateurs et définir des autorisations spécifiques pour chaque ressource.
- Accorder un accès complet à certains services pour certains utilisateurs (ex. : Amazon EC2, Amazon S3).
- Restreindre l'accès d'autres utilisateurs à des actions spécifiques, comme uniquement lire des données dans Amazon S3 ou accéder à des informations de facturation.

IAM est un outil gratuit inclus avec votre compte AWS.



--------------------------------------------------------------------------



## B/

![[Pasted image 20241025033723.png]]

Pour comprendre comment utiliser **IAM** pour sécuriser votre compte AWS, il est essentiel de connaître les quatre composants principaux :

1. **Utilisateur IAM** : Représente une personne ou une application qui doit effectuer des appels d’API vers les services AWS. Chaque utilisateur IAM doit avoir un nom unique et des autorisations de sécurité spécifiques, différentes de celles de l'utilisateur racine.
    
2. **Groupe IAM** : C'est un ensemble d'utilisateurs IAM qui partagent les mêmes autorisations. Les groupes facilitent la gestion des accès pour plusieurs utilisateurs.
    
3. **Stratégie IAM** : Il s'agit d'un document qui définit les autorisations, précisant les actions que les utilisateurs ou groupes peuvent effectuer sur des ressources spécifiques. Les stratégies peuvent aussi refuser explicitement des accès.
    
4. **Rôle IAM** : Permet d'accorder des accès temporaires à certaines ressources AWS. Les rôles sont souvent utilisés pour accorder des permissions sans associer de manière permanente des autorisations à un utilisateur ou à une application.




--------------------------------------------------------------------------

## C/

![[Pasted image 20241025033838.png]]

L'authentification est un principe fondamental de la sécurité informatique, où un utilisateur ou un système doit prouver son identité avant d'accéder à une ressource. Dans AWS, cela se fait via **IAM**, où deux types d'accès peuvent être attribués à un utilisateur :

1. **Accès par programmation** : Nécessite un ID de clé d'accès et une clé d'accès secrète pour interagir avec AWS via des outils tels que l'AWS CLI ou le kit SDK AWS.
    
2. **Accès à la console AWS** : L'utilisateur se connecte via un navigateur en saisissant son ID de compte ou un alias, son nom d'utilisateur et son mot de passe. Si l'authentification multifacteur (MFA) est activée, un code d'authentification sera requis.
    

Ces méthodes garantissent que seuls les utilisateurs autorisés accèdent aux ressources AWS.



--------------------------------------------------------------------------



## D/

![[Pasted image 20241025034017.png]]

Les services et ressources AWS peuvent être accédés via **AWS Management Console**, **AWS CLI**, ou des **SDK et API**. Pour renforcer la sécurité, il est recommandé d'activer l'**authentification multifacteur (MFA)**. Avec la MFA, les utilisateurs doivent fournir un jeton d'authentification en plus de leurs identifiants habituels pour accéder aux ressources AWS. Les jetons MFA peuvent être générés par :

- Des applications virtuelles compatibles avec MFA, comme **Google Authenticator** ou **Authy 2-Factor Authentication**.
- Des clés de sécurité **U2F**.
- Des dispositifs **MFA matériels**.

Cela ajoute une couche de protection supplémentaire contre les accès non autorisés.




--------------------------------------------------------------------------



## E/

![[Pasted image 20241025034525.png]]

L’**autorisation** est le processus qui détermine les droits d'accès d'un utilisateur, d'un service ou d'une application. Après l'**authentification**, un utilisateur doit être autorisé à accéder aux services AWS. Par défaut, les utilisateurs IAM n'ont pas accès aux ressources ni aux données d'un compte AWS. Il est donc nécessaire d'accorder explicitement des autorisations en créant une **stratégie**, qui est un document au format **JSON**. Cette stratégie précise les permissions accordées ou refusées pour l'accès aux ressources du compte AWS.



--------------------------------------------------------------------------


## F/

![[Pasted image 20241025034656.png]]

Pour attribuer des autorisations à un utilisateur, un groupe ou un rôle, il est nécessaire de créer une **stratégie IAM** (ou d'en rechercher une existante dans le compte). Par défaut, aucune autorisation n'est accordée, ce qui signifie que toutes les actions sont implicitement refusées à moins d'être explicitement autorisées. Si une action n'est pas autorisée, elle est refusée, et toute action refusée explicitement sera toujours bloquée.

Le **principe du moindre privilège** est crucial en matière de sécurité. Il s'agit d'accorder à l'utilisateur uniquement les privilèges nécessaires pour accomplir ses tâches. En créant des stratégies IAM, il est conseillé de commencer avec un minimum d'autorisations et d'en ajouter si nécessaire, plutôt que de commencer avec des autorisations trop larges, puis de tenter de les restreindre.

Enfin, il est important de noter que la portée des configurations de service IAM est **mondiale** et s'applique à toutes les régions AWS, sans être définie au niveau de chaque région.


--------------------------------------------------------------------------


## G/

![[Pasted image 20241025034903.png]]
Une **stratégie IAM** est un document définissant les autorisations accordées à une entité (utilisateur, groupe, rôle, ressource) dans AWS. Elle précise quelles actions sont autorisées, sur quelles ressources et dans quelles conditions.

### Types de stratégies IAM

1. **Stratégies basées sur l'identité** :
    
    - Attachable à un utilisateur, groupe ou rôle.
    - Comprend :
        - **Stratégies gérées** : attachées à plusieurs entités.
        - **Stratégies intégrées** : directement liées à une entité spécifique.
2. **Stratégies basées sur les ressources** :
    
    - Associées à des ressources spécifiques (ex. : compartiments S3).
    - Contrôlent les actions qu'un mandataire peut effectuer sur la ressource.

### Évaluation des stratégies

Toutes les stratégies sont évaluées simultanément, sans ordre d'importance. En cas de conflit, la stratégie la plus restrictive prévaut.



--------------------------------------------------------------------------



## H/

![[Pasted image 20241025040019.png]]
### Stratégies basées sur l'identité
- **Définition** : Attachées à des entités telles qu'un utilisateur, un groupe ou un rôle.
- **Fonction** : Spécifient les actions autorisées ou refusées pour ces entités sur des ressources AWS.

### Stratégies basées sur les ressources
- **Définition** : Attachées directement à une ressource (ex. : compartiment S3).
- **Fonction** : Déterminent qui peut accéder à la ressource et quelles actions sont possibles.
- **Création** : Définies au niveau de la ressource, sans document IAM séparé.
  - Exemple : Pour un compartiment S3, accédez à l'onglet **Permissions** et définissez la stratégie au format JSON.

### Exemple de stratégie pour un compartiment S3
- **Accès accordé** : Utilisateur (ex. : MaryMajor) peut répertorier et lire les objets d'un compartiment S3 nommé `photos`.
- **Déclaration de refus** : Peut être intégrée dans la stratégie de compartiment pour restreindre l'accès à certains utilisateurs IAM, même si l'accès est accordé par une stratégie d'identité distincte.

### Priorité des déclarations
- Une déclaration de refus explicite a toujours la priorité sur une déclaration d'autorisation, assurant ainsi un contrôle strict sur l'accès.


--------------------------------------------------------------------------

## I/

![[Pasted image 20241025040219.png]]
### Processus d'autorisation IAM
1. **Refus explicite** : Vérifie d'abord s'il y a une stratégie de refus. Si oui, accès refusé.
2. **Autorisation explicite** : Si aucun refus, vérifie une stratégie d'autorisation. Si trouvée, accès accordé.
3. **Refus implicite** : Si aucune stratégie n'est appliquée, l'accès est refusé par défaut.

### Conditions
- Accès accordé uniquement si l'action n'est pas explicitement refusée et est explicitement autorisée.

### Outil
- **Simulateur de stratégie IAM** : Outil pour tester et dépanner les stratégies d'autorisation.


--------------------------------------------------------------------------



## J/
![[Pasted image 20241025040450.png]]
### Groupe IAM

Un groupe IAM est une collection d'utilisateurs IAM qui simplifie la gestion des autorisations :

- **Gestion simplifiée** : Attachez des stratégies au groupe pour accorder des autorisations à tous ses membres.
- **Ajout facile** : Ajoutez un utilisateur au groupe pour lui attribuer automatiquement les autorisations.
- **Changement de rôle** : Retirez un utilisateur du groupe pour modifier ses autorisations sans les changer individuellement.

### Caractéristiques clés :

- Un groupe peut avoir plusieurs utilisateurs, et un utilisateur peut être dans plusieurs groupes.
- Les groupes ne peuvent pas contenir d'autres groupes.
- Aucun groupe par défaut n'inclut tous les utilisateurs ; il faut créer un groupe manuellement.

--------------------------------------------------------------------------


## K/

![[Pasted image 20241025040700.png]]

### Rôle IAM

Un rôle IAM est une identité dans AWS que vous pouvez créer avec des autorisations spécifiques, semblable à un utilisateur IAM, mais sans informations d'identification à long terme comme un mot de passe ou des clés d'accès. Voici les principales caractéristiques et utilisations des rôles IAM :

- **Délégation d'accès** : Les rôles permettent de donner temporairement des autorisations à des utilisateurs, applications ou services qui n'ont pas normalement accès à vos ressources AWS.
    
- **Utilisateurs multiples** : Contrairement à un utilisateur IAM, un rôle peut être adopté par plusieurs entités selon les besoins.
    
- **Sécurité temporaire** : Lorsqu'un rôle est endossé, il fournit des autorisations de sécurité temporaires pour la session.
    
- **Cas d'utilisation** :
    
    - Accorder des accès temporaires à des utilisateurs d'autres comptes AWS.
    - Permettre à des applications mobiles d'accéder à des ressources AWS sans stocker de clés d'accès.
    - Fournir l'accès à des utilisateurs avec des identités externes, comme celles d'un annuaire d'entreprise.
    - Accorder un accès à des tiers pour des audits.

Les rôles IAM sont essentiels pour gérer l'accès dans un environnement cloud de manière sécurisée et flexible.


--------------------------------------------------------------------------


## L/

![[Pasted image 20241025040816.png]]
Dans cet exemple, un développeur exécute une application sur une instance EC2 qui a besoin d'accéder à un compartiment S3 nommé **photos**. Voici comment cela fonctionne :

1. **Création du rôle IAM** : Un administrateur crée un rôle IAM spécifique qui contient une stratégie d'autorisation.
    
2. **Attribution des autorisations** : Ce rôle inclut une stratégie d'autorisation qui accorde un accès en lecture seule au compartiment S3 **photos**.
    
3. **Stratégie de confiance** : Le rôle comprend également une stratégie de confiance qui permet à l'instance EC2 d'endosser le rôle et d'obtenir des autorisations temporaires.
    
4. **Accès sécurisé** : Lorsque l'application s'exécute sur l'instance EC2, elle utilise les autorisations temporaires fournies par le rôle pour accéder au compartiment **photos**.
    
5. **Simplicité et sécurité** : L'administrateur n'a pas besoin de donner au développeur directement l'autorisation d'accéder au compartiment S3, ce qui simplifie la gestion des autorisations et élimine le besoin pour le développeur de partager ou de gérer ces autorisations.
    

Cet exemple illustre comment les rôles IAM facilitent la gestion des accès tout en renforçant la sécurité dans un environnement AWS.


--------------------------------------------------------------------------




![[Pasted image 20241025041023.png]]




