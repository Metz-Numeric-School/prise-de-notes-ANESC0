###  *Amazon Machine Image (AMI)
 
est un modèle utilisé pour créer des instances EC2 sur AWS. Elle contient les informations nécessaires pour lancer une machine virtuelle, incluant le système d'exploitation, les applications préinstallées, les bibliothèques et les configurations.

1. **Contenu** : Comprend un système d'exploitation (Linux, Windows, etc.), le middleware, les applications, et les configurations.
2. **Personnalisable** : Tu peux créer une AMI à partir d'une instance existante, ce qui permet de déployer des configurations récurrentes rapidement.
3. **Types d'AMI** :
    - **Publiques** : Offertes par AWS ou la communauté pour des configurations standards.
    - **Privées** : Personnalisées et accessibles uniquement par ton compte.
4. **Régions** : Les AMIs sont spécifiques à une région, mais peuvent être copiées d'une région à une autre.
5. **Utilisation** : Sert de point de départ pour créer une nouvelle instance EC2 avec un environnement pré-configuré.

Les AMI permettent un déploiement rapide d'instances avec une configuration prédéfinie et cohérente.