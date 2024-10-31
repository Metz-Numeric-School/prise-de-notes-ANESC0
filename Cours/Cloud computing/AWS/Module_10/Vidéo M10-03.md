
# Amazon EC2 Auto Scaling



## A/

![[Pasted image 20241031150635.png]]


La **mise à l’échelle** permet d’ajuster dynamiquement les ressources de calcul en fonction de la charge de travail de l’application, optimisant ainsi **disponibilité** et **coûts**. Voici les deux approches évoquées :

1. **Sur-allocation de capacité** : En allouant des ressources pour la demande la plus élevée (le mercredi), l'application reste performante, mais les ressources sont sous-utilisées les autres jours, ce qui entraîne des coûts élevés.

2. **Sous-allocation de capacité** : En allouant moins de capacité, les coûts sont réduits, mais les jours de forte demande, l'application risque de sous-performer ou de devenir inaccessible.

En conclusion, la mise à l'échelle permet de gérer les fluctuations tout en équilibrant les **coûts** et les **performances** de l'application.


----

## B/


![[Pasted image 20241031150726.png]]

![[Pasted image 20241031150734.png]]

![[Pasted image 20241031150759.png]]




-----


## C/

![[Pasted image 20241031150812.png]]

Un **groupe à scalabilité automatique** dans Amazon EC2 est une **collection d'instances** traitée comme une unité pour **adapter dynamiquement la capacité de calcul** selon la demande. Les paramètres configurables sont :

1. **Taille minimale** : le nombre d'instances minimum pour garantir la disponibilité. Amazon EC2 Auto Scaling empêche le groupe de descendre sous ce seuil.
2. **Capacité souhaitée** : le nombre idéal d'instances, qui peut être défini manuellement ou modifié en fonction des besoins. Auto Scaling ajuste la taille du groupe pour atteindre cette cible.
3. **Taille maximale** : limite le nombre d'instances dans le groupe pour éviter une surconsommation de ressources.

En définissant des **stratégies de mise à l’échelle**, Amazon EC2 Auto Scaling peut **ajuster le nombre d’instances automatiquement** pour répondre aux variations de charge, dans les limites définies. Par exemple, avec une taille minimale d’une instance, une capacité souhaitée de deux, et une taille maximale de quatre, Auto Scaling modifie le nombre d'instances en fonction des critères de charge, pour maintenir l’équilibre entre **coût** et **disponibilité**.


![[Pasted image 20241031150821.png]]

Dans Amazon EC2 Auto Scaling, la **scalabilité horizontale** désigne le **lancement de nouvelles instances** pour répondre à une demande croissante. À l'inverse, la **diminution d'échelle** consiste à **résilier des instances** lorsqu'elles ne sont plus nécessaires, ce qui optimise les ressources et réduit les coûts. Ces ajustements permettent de maintenir les performances de l’application en fonction de la charge de travail, tout en évitant les ressources excédentaires lors des périodes de faible demande.


-----



## D/

![[Pasted image 20241031150932.png]]

![[Pasted image 20241031150944.png]]


-----



## E/

![[Pasted image 20241031151000.png]]

AWS Auto Scaling étend la mise à l’échelle automatique en offrant une approche **globale** pour ajuster la capacité de plusieurs services AWS. En plus des instances EC2, AWS Auto Scaling peut gérer la mise à l’échelle de services comme **Amazon ECS** pour des conteneurs, **Amazon DynamoDB** pour des tables et index, ainsi que **Amazon Aurora** pour des réplicas de bases de données. Grâce à cette solution unifiée, AWS Auto Scaling optimise automatiquement la capacité pour maintenir des performances **stables** et **prévisibles** au **coût le plus bas** possible, en utilisant des plans de mise à l’échelle basés sur des modèles de demande prédictifs. 

En combinant **Amazon EC2 Auto Scaling** avec **AWS Auto Scaling**, vous pouvez ajuster dynamiquement les ressources pour d'autres services AWS, assurant ainsi une réactivité aux fluctuations de charge tout en optimisant l'allocation des ressources dans toute l'infrastructure AWS.




----


![[Pasted image 20241031151011.png]]



