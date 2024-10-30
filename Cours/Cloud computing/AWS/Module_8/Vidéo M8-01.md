# Amazon Relational Database Service


## A/

![[Pasted image 20241030213448.png]]

![[Pasted image 20241030213520.png]]



----

## B/ [[AWS RDS]]


![[Pasted image 20241030213627.png]]




![[Pasted image 20241030213646.png]]


----


## C/

![[Pasted image 20241030213702.png]]

Dans Amazon RDS, **l’instance de base de données** est un environnement de base de données isolé pouvant héberger plusieurs bases de données. Les **ressources** d'une instance sont définies par sa **classe** et le **type de stockage** utilisé, qui influencent les performances et les coûts. Cela permet d’ajuster ces paramètres selon les besoins. Lors de la création d'une instance, il faut choisir un **moteur de base de données**, avec six options disponibles : MySQL, Amazon Aurora, Microsoft SQL Server, PostgreSQL, MariaDB et Oracle.


-----


## D/

![[Pasted image 20241030213758.png]]

Avec Amazon Virtual Private Cloud (VPC), vous pouvez exécuter une instance de base de données Amazon RDS dans un **environnement réseau contrôlé** où vous définissez la plage d’adresses IP, les sous-réseaux, le routage, et les ACL. Bien que la fonctionnalité d’Amazon RDS reste identique, l’instance est souvent **isolée dans un sous-réseau privé**, accessible uniquement par certaines instances d'application. Chaque sous-réseau d’un VPC est associé à une **zone de disponibilité**, ce qui vous permet de choisir l’emplacement physique de votre instance de base de données.



![[Pasted image 20241030213834.png]]

La fonctionnalité de **déploiement multi-AZ** d'Amazon RDS permet de configurer une instance de base de données avec une **réplication synchrone** dans une autre zone de disponibilité du même VPC. En cas de maintenance ou de défaillance, cette copie de secours garantit une **haute disponibilité** en basculant automatiquement vers l'instance secondaire. Cette configuration renforce la résilience de la base de données face aux interruptions et améliore sa disponibilité.


![[Pasted image 20241030213902.png]]



En cas de **défaillance** de l'instance principale dans un déploiement multi-AZ, Amazon RDS bascule automatiquement vers l'**instance de secours**, désormais en ligne en tant que nouvelle principale. Grâce à la **réplication synchrone**, le risque de perte de données est limité. Vos applications, qui accèdent à la base via un **point de terminaison RDS DNS**, n'ont besoin d'aucune modification pour se connecter à cette instance de secours lors du basculement.


----



## E/

![[Pasted image 20241030213939.png]]


![[Pasted image 20241030213956.png]]


-----


## F/

![[Pasted image 20241030214014.png]]


![[Pasted image 20241030214024.png]]


----

## G/


![[Pasted image 20241030214055.png]]

![[Pasted image 20241030214120.png]]




-----------


![[Pasted image 20241030214140.png]]

