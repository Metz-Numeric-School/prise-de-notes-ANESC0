
![[Pasted image 20241030023735.png]]

![[Pasted image 20241030023803.png]]


Lors de l'utilisation d'**Amazon S3 Glacier** pour l'archivage de données, vous pouvez bénéficier de coûts de stockage très bas. Cependant, la récupération de ces données nécessite du temps, car elle peut prendre plusieurs heures. Voici les **trois concepts clés** d'Amazon S3 Glacier :

### Concepts clés

1. **Archive** :
   - Un **archive** est tout objet que vous stockez dans Amazon S3 Glacier, comme une photo, une vidéo, un fichier ou un document. 
   - C'est l'unité de stockage de base, chaque archive ayant son propre **ID** et pouvant contenir une **description**.

2. **Coffre** :
   - Un **coffre** est un conteneur pour stocker des archives. 
   - Lorsque vous créez un coffre, vous devez spécifier son **nom** et la **région** dans laquelle il sera créé.

3. **Stratégie d'accès au coffre** :
   - Elle détermine qui peut accéder aux données stockées dans le coffre et les opérations qu'ils peuvent effectuer.
   - Vous pouvez créer une **politique d'autorisations** pour gérer ces accès, ainsi qu'une **politique de verrouillage** pour empêcher les modifications.

### Options de récupération de données

Amazon S3 Glacier propose trois options de récupération, chacune avec des délais et des coûts différents :

- **Récupérations accélérées** : généralement disponibles en **1 à 5 minutes**, mais à un coût plus élevé.
- **Récupérations standard** : durent environ **3 à 5 heures**, avec un tarif inférieur à celui des récupérations accélérées.
- **Récupérations en bloc** : prennent **5 à 12 heures**, et sont la solution la moins coûteuse.

### Autres caractéristiques

- Amazon S3 Glacier assure une durabilité de **99,999999999%** pour les objets stockés.
- Il prend en charge le **chiffrement des données** en transit et au repos via SSL ou TLS.
- La fonctionnalité de verrouillage de coffre garantit la conformité via des politiques définies.

Cette structure rend Amazon S3 Glacier particulièrement adapté à l'archivage à long terme, où le coût est une priorité, mais où un accès instantané n'est pas nécessaire.

