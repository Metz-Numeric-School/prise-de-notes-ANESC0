# Sécurisation des comptes



## A/

![[Pasted image 20241026013756.png]]

AWS Organizations est un service centralisé permettant de gérer plusieurs comptes AWS dans une organisation. Il offre plusieurs fonctionnalités de sécurité :

1. **Groupement en unités d’organisation (UO)** : Permet de regrouper des comptes avec des règles spécifiques. Par exemple, on peut bloquer l'accès à certains services pour des comptes soumis à des réglementations strictes en créant une UO avec des stratégies d'accès restreint.

2. **Intégration avec IAM** : AWS Organizations étend le contrôle de sécurité IAM au niveau des comptes et impose des règles basées sur les stratégies des UO, limitant les actions autorisées par IAM au niveau du compte.

3. **Stratégies de contrôle des services (SCP)** : Définissent les autorisations maximales pour chaque compte membre, interdisant des services ou actions spécifiques, même si un administrateur local accorde des permissions.

En résumé, AWS Organizations centralise la gestion et restreint l'accès de manière rigoureuse en combinant UO, IAM et SCP pour un contrôle granulaire des permissions.



--------------------------------------------------------------------------


## B/

![[Pasted image 20241026013831.png]]

Les SCP dans AWS Organizations définissent les autorisations maximales pour tous les comptes, en limitant les actions autorisées même si les stratégies IAM les permettent. Elles servent de barrière de sécurité globale mais ne donnent pas directement de permissions.

--------------------------------------------------------------------------


## C/

![[Pasted image 20241026014008.png]]

**AWS Key Management Service (KMS)** permet de **créer** et **gérer des clés de chiffrement**, tout en contrôlant leur utilisation pour **sécuriser** les services AWS et les applications. Sécurisé par des **modules de sécurité matériels** (**HSM**) conformes à la norme **FIPS 140-2**, **AWS KMS** enregistre aussi les actions via **CloudTrail** pour répondre aux exigences de **conformité**. Les **clés principales client** (**CMK**) gèrent l'**accès** et le **chiffrement des données**, avec la possibilité d’**importer des clés** depuis d'autres infrastructures de gestion. **AWS KMS** est intégré à divers **services AWS**, facilitant le contrôle du **chiffrement des données stockées**.



--------------------------------------------------------------------------




## D /

![[Pasted image 20241026014151.png]]

**Amazon Cognito** propose des solutions pour **contrôler l’accès** aux **ressources AWS** depuis votre application, en définissant des **rôles** pour mapper les **utilisateurs** et limiter l’accès aux **ressources autorisées** pour chacun. **Cognito** prend en charge des standards comme **Security Assertion Markup Language (SAML) 2.0**, une norme pour **échanger des informations d'identité** et de **sécurité**. Les applications compatibles **SAML** permettent une **authentification unique (SSO)** avec les **identifiants de votre annuaire d’entreprise** (ex. **Microsoft Active Directory**). Cognito facilite la conformité aux réglementations telles que la **HIPAA**, la norme **PCI DSS**, et les normes **ISO/CEI** (27001, 27017, 27018), essentielles pour les entreprises réglementées (santé, finance).



--------------------------------------------------------------------------


## E/

![[Pasted image 20241026014303.png]]

**AWS Shield** est un service de protection **DDoS** (Déni de service distribué) géré, conçu pour protéger les **applications** exécutées sur **AWS**. Il offre une **détection continue** et une **atténuation automatique** des risques, réduisant ainsi les interruptions et la latence des applications, sans nécessiter l'intervention d'**AWS Support**. AWS Shield protège contre tous les types d'attaques DDoS, y compris :

- **Attaques ciblant la couche d'infrastructure** (ex. inondations UDP)
- **Attaques de type « state exhaustion »** (ex. inondations TCP SYN)
- **Attaques visant la couche d'application** (ex. inondations HTTP GET ou POST)

**AWS Shield Standard** est activé automatiquement pour tous les clients **AWS** sans frais supplémentaires. En revanche, **AWS Shield Advanced** est un service payant qui offre des protections accrues contre des attaques plus importantes et sophistiquées sur des services tels que **Amazon EC2**, **Elastic Load Balancing**, **Amazon CloudFront**, **AWS Global Accelerator**, et **Amazon Route 53**. Pour accéder à l’équipe d’intervention DDoS, les clients doivent avoir un contrat de support **Enterprise** ou **Business** avec **AWS Support**.

