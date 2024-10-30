
# Amazon Aurora


[[AWS Aurora]]

## A/

![[Pasted image 20241030215537.png]]

Voici quelques **avantages clés** d'Amazon Aurora :

- **Haute disponibilité** : Conçu pour offrir un sous-système de stockage rapide et distribué.
- **Facilité de configuration** : Utilise des requêtes SQL standard pour simplifier l'intégration.
- **Compatibilité** : Directement compatible avec MySQL et PostgreSQL, permettant l'utilisation de la plupart des outils de base de données existants sans modifications majeures.
- **Tarification à l'utilisation** : Vous ne payez que pour les services et fonctionnalités que vous utilisez.
- **Intégration avec d'autres services AWS** : Compatible avec des outils comme AWS Database Migration Service (DMS) et AWS Schema Conversion Tool, facilitant le transfert de vos données vers Amazon Aurora.


![[Pasted image 20241030215546.png]]



Voici pourquoi **recourir à Amazon Aurora** peut être préférable à d'autres options comme **SQL avec Amazon RDS** :

- **Haute disponibilité** : Amazon Aurora stocke plusieurs copies de vos données dans différentes zones de disponibilité, assurant ainsi une robustesse face aux défaillances.

- **Sauvegardes continues** : Les données sont continuellement sauvegardées sur Amazon S3, offrant une protection supplémentaire.

- **Réplicas en lecture** : Aurora permet d'utiliser jusqu'à 15 réplicas en lecture, ce qui aide à répartir la charge et réduit le risque de perte de données.

- **Récupération rapide** : La conception d’Aurora permet une récupération après incident instantanée, ce qui est essentiel en cas de problème avec la base de données principale. 

Ces caractéristiques font d'Amazon Aurora une solution robuste et fiable pour des applications nécessitant une disponibilité et une performance élevées.



----
![[Pasted image 20241030215737.png]]

Après un incident, **Amazon Aurora** optimise le processus de récupération de manière significative :

- **Récupération rapide** : Au lieu de relire le journal de rétablissement à partir du dernier point de sauvegarde, Aurora gère cela à chaque opération de lecture. Cela permet de réduire le temps de redémarrage de la base de données à moins de **60 secondes** dans la plupart des cas.

- **Cache de mémoire tampon** : Le cache de mémoire tampon est situé en dehors du processus de base de données, ce qui signifie qu'il est immédiatement disponible au redémarrage. Cela évite de restreindre l'accès jusqu'à ce que le cache soit à nouveau rempli, prévenant ainsi les baisses de performance.

Ces caractéristiques font d'Amazon Aurora une solution efficace pour assurer la continuité des opérations, même après un incident.



----



![[Pasted image 20241030215820.png]]

