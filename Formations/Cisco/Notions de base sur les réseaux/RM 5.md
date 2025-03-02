

# Fiche Récapitulative - Protocoles et Modèles de Communication

## Importance des Protocoles Réseau

Les protocoles sont indispensables pour assurer une communication convenable des ordinateurs sur tout le réseau. Ils définissent les règles suivantes :

- **Format du message** : Utilisation d'un format ou d'une structure spécifique pour l'envoi de messages.
    
- **Taille du message** : Règles strictes pour la taille des pièces communiquées sur le réseau.
    
- **Temporisation** : Détermination de la vitesse de transmission des bits, le moment d'envoi des données, et le volume total de données transmissibles lors d'une seule transmission.
    
- **Encodage** : Conversion des messages en bits par l'hôte émetteur, codage des bits en modèles de sons, d'ondes lumineuses ou d'impulsions électriques selon le support du réseau.
    
- **Encapsulation** : Ajout d'une en-tête contenant des informations d'adressage aux données qui composent le message.
    
- **Modèle de message** : Certains messages nécessitent un accusé de réception avant l'envoi du message suivant, tandis que d'autres sont diffusés sans se soucier de savoir s'ils atteignent leur destination.
    

## Normes de Communication

Les topologies nous permettent de visualiser le réseau à travers la représentation des terminaux et des périphériques intermédiaires. Les normes réseau et Internet garantissent que tous les appareils qui se connectent au réseau appliquent les mêmes règles ou protocoles, permettant ainsi la transmission d'informations via Internet. Les normes Internet sont développées, publiées et maintenues par des organisations comme l'IETF. Les étapes d'élaboration et d'approbation des nouvelles normes sont notées dans des documents RFC numérotés.

## Modèles de Communication en Réseau

### Règles qui régissent les communications

Une communication réussie entre les hôtes suppose une interaction entre plusieurs protocoles (HTTP, TCP, IP, Ethernet). Ces protocoles sont implémentés dans le logiciel et le matériel installés sur chaque hôte et chaque appareil réseau. L'interaction entre les différents protocoles sur un appareil est illustrée par une pile de protocoles, où chaque couche de la pile fonctionne indépendamment des autres.



-----
## Modèle de communication en réseau

### Modèle TCP/IP et Description

| **Couche du Modèle TCP/IP** | **Description**                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------ |
| **Application**             | Représente des données pour l'utilisateur, ainsi que du codage et un contrôle du dialogue. |
| **Transport**               | Prend en charge la communication entre plusieurs périphériques à travers divers réseaux.   |
| **Internet**                | Détermine le meilleur chemin à travers le réseau.                                          |
| **L'accès au réseau**       | Contrôle les périphériques matériels et les supports qui constituent le réseau.            |

---
### Modèle OSI et Description

| **Couche du Modèle OSI** | **Description** |
| --- | --- |
| **7 - Application** | La couche application contient des protocoles utilisés pour les communications de processus à processus. |
| **6 - Présentation** | La couche présentation fournit une représentation commune des données transférées entre des services de couche application. |
| **5 - Session** | La couche session fournit des services à la couche présentation pour organiser son dialogue et gérer l'échange de données. |
| **4 - Transport** | La couche transport définit des services pour segmenter, transférer et réassembler les données de communications individuelles entre les périphériques finaux. |
| **3 - Réseau** | La couche réseau fournit des services pour échanger les parties de données individuelles sur le réseau entre des périphériques finaux identifiés. |
| **2 - Liaison de Données** | Les protocoles de couche liaison de données décrivent des méthodes d'échange de trames de données entre des périphériques sur un support commun. |
| **1 - Physique** | Les protocoles de la couche physique décrivent les moyens mécaniques, électriques, fonctionnels et méthodologiques permettant d'activer, de gérer et de désactiver des connexions physiques pour la transmission de bits vers et depuis un périphérique réseau. |



----
## Comparaison des modèles OSI et TCP/IP

![[Pasted image 20250223144554.png]]
## Similitudes et Différences

### Similitudes
Les principales similitudes se trouvent dans les couches de transport et de réseau.

### Différences
Les deux modèles diffèrent dans la manière dont ils se rapportent aux couches situées au-dessus et au-dessous de chaque couche :

### Correspondances entre les Couches

1. **Couche Réseau**
   - **Modèle OSI** : **Couche 3 (Réseau)**
   - **Modèle TCP/IP** : **Couche Internet**
   - **Description** : Cette couche sert à décrire les protocoles qui adressent et acheminent les messages via un réseau interne.

2. **Couche Transport**
   - **Modèle OSI** : **Couche 4 (Transport)**
   - **Modèle TCP/IP** : **Couche Transport**
   - **Description** : Cette couche décrit les services et les fonctions généraux qui assurent une livraison ordonnée et fiable des données entre les hôtes source et destination.

### Couches Supérieures

1. **Couche Application**
   - **Modèle TCP/IP** : **Couche Application**
   - **Description** : La couche application TCP/IP inclut plusieurs protocoles qui fournissent des fonctionnalités spécifiques à plusieurs applications d'utilisateur final. 

### Références pour les Développeurs

1. **Couches 5, 6 et 7 du Modèle OSI**
   - **Modèle OSI** : **Couches Session, Présentation, Application**
   - **Description** : Ces couches servent de références aux développeurs et aux éditeurs de logiciels d'application pour créer des applications qui fonctionnent sur les réseaux.

### Utilisation Courante des Modèles

- Les modèles **TCP/IP** et **OSI** sont couramment utilisés lors de la référence aux protocoles de différentes couches.
- Le **modèle OSI**, qui sépare la couche liaison de données de la couche physique, est généralement utilisé pour faire référence aux couches inférieures.



----

