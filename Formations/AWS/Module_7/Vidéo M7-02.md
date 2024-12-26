
# Amazon Simple Storage Service

[[AWS S3]]



## A/

![[Pasted image 20241030022618.png]]

**Amazon S3** propose plusieurs classes de stockage adaptées à des besoins variés :

- **Amazon S3 Standard** : Stockage performant pour les données fréquemment consultées, avec une latence faible et un débit élevé. Idéal pour les applications web, la distribution de contenu, et le Big Data.
  
- **Amazon S3 Intelligent-Tiering** : Optimise les coûts en déplaçant automatiquement les données vers le niveau de stockage le moins coûteux (accès fréquent ou peu fréquent), sans frais de récupération ni de transfert. Convient aux données dont le modèle d'accès est imprévisible.

- **Amazon S3 Standard - Accès peu fréquent (Standard-IA)** : Conçu pour les données moins souvent consultées mais nécessitant un accès rapide. Parfait pour les sauvegardes et la reprise après sinistre.

- **Amazon S3 One Zone - Accès peu fréquent (One Zone-IA)** : Une option économique pour les données de sauvegarde secondaires ou pouvant être recréées. Les données sont stockées dans une seule zone de disponibilité, ce qui diminue les coûts.

- **Amazon S3 Glacier** : Classe pour l'archivage à coût réduit avec trois options de récupération (quelques minutes à plusieurs heures). Idéal pour le stockage sécurisé et durable de données archivées.

- **Amazon S3 Glacier Deep Archive** : Solution la moins coûteuse pour le stockage de longue durée (7-10 ans ou plus), particulièrement adaptée aux secteurs réglementés nécessitant la conservation de données. Les objets sont répliqués et peuvent être restaurés en 12 heures.

Ces options permettent une gestion flexible et économique de divers besoins de stockage à long terme dans le cloud.


--------------------------------------------------------------------------


## B/

![[Pasted image 20241030022720.png]]

![[Pasted image 20241030022736.png]]



--------------------------------------------------------------------------


## C/

![[Pasted image 20241030022800.png]]

**Amazon S3** est un service de stockage évolutif qui ajuste automatiquement la capacité en fonction de l'augmentation du volume de données dans votre compartiment. Il peut être utilisé immédiatement sans nécessiter de configuration préalable, et le stockage évolue selon les besoins de vos applications. En prenant en charge un volume élevé de requêtes, Amazon S3 évite d'avoir à gérer l'allocation de stockage ou de débit, offrant une solution pratique où les frais sont uniquement basés sur l'utilisation réelle.


![[Pasted image 20241030022839.png]]

**Amazon S3** offre plusieurs méthodes d'accès : la console de gestion AWS, l'interface de ligne de commande (AWS CLI) et les kits de développement logiciel (SDK). Il permet aussi un accès direct aux données via des points de terminaison REST compatibles HTTP et HTTPS. 

Pour garantir la compatibilité avec l'accès par URL, les noms de compartiment doivent être uniques au niveau mondial et conformes aux normes DNS. Les clés d'objet, quant à elles, doivent utiliser des caractères sécurisés pour les URL, assurant ainsi une interaction fluide avec les données stockées.


![[Pasted image 20241030022920.png]]




--------------------------------------------------------------------------


## D/

![[Pasted image 20241030022948.png]]


**Amazon S3** propose des solutions pour plusieurs cas d’usage courants : 

1. **Hébergement d'applications** : déploiement, installation et gestion d'applications web sur une infrastructure flexible.
2. **Hébergement de contenus multimédias** : stockage et diffusion de fichiers multimédias tels que vidéos, photos, et musique, grâce à une infrastructure évolutive et hautement disponible.
3. **Distribution de logiciels** : hébergement d’applications téléchargeables pour les clients, optimisé pour la livraison rapide et fiable.

Ces services sont soutenus par une infrastructure redondante pour assurer la disponibilité et la résilience des contenus hébergés.



--------------------------------------------------------------------------



## E/

![[Pasted image 20241030023048.png]]

![[Pasted image 20241030023100.png]]


![[Pasted image 20241030023158.png]]




--------------------------------------------------------------------------


![[Pasted image 20241030023229.png]]

