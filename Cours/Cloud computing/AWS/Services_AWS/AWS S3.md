
![[Pasted image 20241030022317.png]]
**Amazon S3** fournit un **stockage de niveau objet**, nécessitant de recharger le fichier entier pour toute modification. Les données sont stockées sous forme d'**objets** dans des **compartiments**.



![[Pasted image 20241030022422.png]]


**Amazon S3** est un service de **stockage cloud géré et scalable**, conçu pour une **durabilité de 99,999999999%**. Les données sont stockées sous forme d'**objets** dans des **compartiments** de capacité virtuelle illimitée, chaque objet pouvant atteindre jusqu'à **5 To**. Par défaut, les données sont **répliquées** sur plusieurs installations pour garantir la résilience et ne sont pas partagées publiquement. 

L'accès aux données peut être contrôlé en détail via des **politiques IAM** et **listes de contrôle d'accès**. Des options de **chiffrement** et des **notifications d'événements** permettent une gestion automatisée. Enfin, l'**analyse de la classe de stockage** optimise le cycle de vie des données en transférant les données peu consultées vers des options de stockage moins coûteuses comme **Amazon S3 Standard-IA**.