# Amazon Elastic file

[[AWS EFS]]


## A/

![[Pasted image 20241030023437.png]]

**Amazon EFS** offre un stockage de fichiers dans le cloud, permettant la création et le montage d'un système de fichiers sur des instances **Amazon EC2**. Grâce au protocole **NFS** versions 4.0 et 4.1 (NFSv4), vous pouvez accéder simultanément à votre système de fichiers à partir de plusieurs instances EC2 dans un **VPC**. Cela permet à des applications nécessitant une scalabilité de partager une source de données commune.

Dans un environnement AWS, le VPC peut contenir plusieurs zones de disponibilité, et il est recommandé d'accéder au système de fichiers via une cible de montage située dans la même zone de disponibilité. Cela optimise la performance et la latence. Un des avantages d'Amazon EFS est la possibilité pour les instances EC2 s'exécutant dans différentes zones de disponibilité d'accéder à un même système de fichiers, favorisant ainsi la collaboration et le partage de données entre utilisateurs.


![[Pasted image 20241030023514.png]]



--------------------------------------------------------------------------


## B/

![[Pasted image 20241030023531.png]]

Dans **Amazon EFS**, un **système de fichiers** est la ressource principale, possédant des propriétés clés telles que :

- **ID**
- **Jeton de création**
- **Heure de création**
- **Taille du système de fichiers** (en octets)
- **Nombre de cibles de montage** créées pour le système de fichiers
- **État du système de fichiers**

### Ressources associées

1. **Cibles de montage** :
   - Pour accéder à votre système de fichiers, il est nécessaire de créer des cibles de montage dans votre **VPC**. 
   - Chaque cible de montage a des propriétés telles que :
     - **ID de la cible de montage**
     - **ID du sous-réseau** où elle a été créée
     - **ID du système de fichiers** où elle a été créée
     - **Adresse IP** sur laquelle le système de fichiers peut être monté
     - **État de la cible de montage**
   - Vous pouvez utiliser l'adresse IP ou le nom DNS dans votre commande de montage.

2. **Balises** :
   - Pour mieux organiser vos systèmes de fichiers, vous pouvez ajouter des métadonnées à chacun d'eux sous forme de balises. 
   - Chaque balise est une **paire clé-valeur**.
   - Les balises et les cibles de montage sont considérées comme des sous-ressources, existant uniquement lorsqu'elles sont associées à un système de fichiers.

Ces propriétés et ressources facilitent la gestion et l'organisation des systèmes de fichiers dans Amazon EFS, assurant un accès efficace et structuré.




--------------------------------------------------------------------------



![[Pasted image 20241030023639.png]]

