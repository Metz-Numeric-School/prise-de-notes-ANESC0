# Infrastructure mondiale AWS

## Introduction à l'infrastructure mondiale

- **AWS** offre une infrastructure **flexible**, **fiable**, **sécurisée** et **évolutive** avec des **performances réseau mondiales**.
- L'empreinte AWS est régulièrement mise à jour.

## Régions AWS

![[Pasted image 20241023005153.png]]


- **22 régions** dans le monde.
- Une **région AWS** est un emplacement géographique avec une ou plusieurs **zones de disponibilité**.
- Les **zones de disponibilité** (AZ) sont des groupes de centres de données isolés.
- Les régions AWS introduites avant le **20 mars 2019** sont activées par défaut.
- Régions postérieures au **20 mars 2019** (ex. Hong Kong, Bahreïn) désactivées par défaut.
- **GovCloud (USA)** : Régions réservées aux administrations américaines.

### Sélection d'une région

- Facteurs importants :
    - **Gouvernance des données et obligations légales** (ex. directive de l'UE sur la protection des données).
    - **Proximité** avec les utilisateurs (pour réduire la latence).
    - Disponibilité des **services** dans chaque région.
    - **Coûts** variant selon la région (exemple : USA Est vs Asie Pacifique).

## Zones de disponibilité (AZ)

- **Chaque région** comprend plusieurs **zones de disponibilité** (généralement **3 centres de données** ou plus).
- **Partitionnement complet** pour assurer l'isolation des défaillances (ex : catastrophes naturelles).
- **Réseau privé à haut débit** interconnectant les zones de disponibilité.
- AWS recommande de **répliquer les données** entre les AZ pour plus de résilience.

## Centres de données AWS

- Chaque **centre de données** AWS est sécurisé et conçu pour la redondance.
- Évalués pour limiter les **risques environnementaux**.
- Composants critiques **sauvegardés** dans plusieurs zones de disponibilité.
- Capacité et disponibilité sont surveillées en continu pour garantir la performance.

Voici un résumé des avantages de l'infrastructure mondiale AWS :

---

### Avantages de l'infrastructure mondiale AWS

1. **Élasticité et scalabilité** :
    
    - Les ressources peuvent s'ajuster dynamiquement pour répondre aux variations des besoins de capacité.
    - Adaptation aisée à la croissance des demandes.
2. **Tolérance aux pannes** :
    
    - Redondance des composants, permettant de maintenir les opérations même en cas de défaillance d'un composant.
3. **Haute disponibilité** :
    
    - Fonctionnement avec un minimum d'intervention humaine, garantissant une disponibilité élevée et réduisant les temps d'arrêt.




![[Pasted image 20241023005300.png]]
