
# Amazon CloudFront



## A/

![[Pasted image 20241029013555.png]]

La **performance du réseau** peut être impactée par la distance et le nombre de **sauts de réseau** nécessaires pour atteindre un **serveur d'origine** qui stocke les versions **originales et définitives** des objets, tels que les **pages web, images et fichiers multimédias**. Lorsque vous accédez à un site web ou regardez une vidéo en streaming, chaque saut et la distance parcourue influencent les **performances** et la **réactivité** de l’application.

Pour réduire la **latence réseau** liée aux **emplacements géographiques** éloignés, l'utilisation d'un **réseau de diffusion de contenu** (CDN) peut s'avérer bénéfique. Un CDN permet d’optimiser la **vitesse** de chargement des ressources en les stockant plus près de l’utilisateur final, ce qui améliore ainsi l'expérience utilisateur en rendant les contenus **plus rapides et plus réactifs**.





## B/

![[Pasted image 20241029013644.png]]



## C/ [[AWS Amazon CloudFront]]



## D/

![[Pasted image 20241029013816.png]]

**Amazon CloudFront** distribue le contenu via un **réseau mondial** de **centres de données** appelés **emplacements périphériques**. Lorsqu’un **utilisateur** demande du contenu diffusé avec CloudFront, sa requête est dirigée vers l’**emplacement périphérique** offrant la **latence la plus faible** pour une diffusion avec les **meilleures performances possibles**.

Ces **emplacements périphériques CloudFront** sont optimisés pour diffuser rapidement les **contenus populaires**. Lorsque certains objets perdent en popularité, les emplacements périphériques peuvent les **supprimer** pour libérer de la place pour des contenus plus demandés. Pour les contenus moins populaires, CloudFront utilise des **caches périphériques régionaux**, qui sont des **emplacements CloudFront** à l'échelle mondiale, situés **entre le serveur d'origine et les emplacements périphériques mondiaux**. 

Les **caches périphériques régionaux** ont une **capacité de stockage plus grande**, permettant aux objets d'y **rester plus longtemps**. Cette configuration maintient une **grande partie du contenu** à proximité des utilisateurs, ce qui **réduit la nécessité d’accéder au serveur d'origine** et améliore les **performances globales** pour votre audience.



## E/

![[Pasted image 20241029013904.png]]


**Amazon CloudFront** offre plusieurs **avantages clés** :

- **Rapide et de portée mondiale** : Amazon CloudFront est **massivement évolutif** et distribué à travers un **réseau mondial** d'emplacements périphériques et de caches régionaux pour assurer une **faible latence** aux utilisateurs finaux.

- **Sécurité à la périphérie** : CloudFront offre des **protections intégrées** pour la sécurité réseau et applicative. Par exemple, **AWS Shield Standard** assure une protection sans coût supplémentaire. Vous pouvez également utiliser **AWS Certificate Manager (ACM)** pour gérer des certificats SSL personnalisés.

- **Hautement programmable** : CloudFront est **personnalisable** pour des besoins applicatifs spécifiques, avec des intégrations telles que **Lambda@Edge**, permettant de **déployer du code** proche des utilisateurs pour une meilleure réactivité. Il prend en charge les environnements **CI/CD** pour des intégrations DevOps.

- **Étroitement intégré à AWS** : CloudFront est **directement connecté à l'infrastructure AWS** mondiale, et peut être géré par **API** ou via la **Console de gestion AWS** pour une configuration simplifiée.

- **Économique** : CloudFront fonctionne **sans engagement minimum** et facture uniquement les **ressources utilisées**, réduisant les coûts associés au **maintien d’un réseau de serveurs de cache** sur plusieurs sites. Il limite la charge des serveurs d’origine en regroupant les demandes simultanées, et si vous utilisez des serveurs d’origine AWS comme **Amazon S3** ou **Elastic Load Balancing**, vous ne payez que les frais de stockage, et non les transferts de données entre ces services et CloudFront.



--------------------------------------------------------------------------



## F/

![[Pasted image 20241029014016.png]]




--------------------------------------------------------------------------



![[Pasted image 20241029014046.png]]
