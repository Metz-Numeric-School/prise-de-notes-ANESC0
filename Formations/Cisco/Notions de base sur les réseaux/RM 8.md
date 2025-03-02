
**Fiche de Révision : L'Adresse IPv4**

**1. Objectif de l'adresse IPv4**

- Une adresse IPv4 est une adresse réseau logique qui identifie un hôte.
- Elle doit être unique et correctement configurée sur un LAN pour la communication locale.
- Elle doit être unique et bien configurée sur un réseau mondial pour la communication distante.
- Une adresse IPv4 est attribuée à l'interface réseau d'un hôte, souvent une carte réseau.
- Chaque paquet envoyé via Internet contient une adresse IPv4 source et une adresse IPv4 de destination.
- Les appareils réseau utilisent ces informations pour assurer l'acheminement des données et des réponses.

**2. Structure des adresses IPv4**

- Une adresse IPv4 est une adresse logique de 32 bits, divisée en deux parties :
    - **Partie réseau** : Identifie le réseau auquel appartient l'hôte.
    - **Partie hôte** : Identifie l'hôte unique sur ce réseau.
- Exemple : Adresse IPv4 **192.168.5.11** avec un masque **255.255.255.0** :
    - Partie réseau : **192.168.5**
    - Partie hôte : **11**
- Cet adressage est **hiérarchique** :
    - Il permet aux routeurs d'acheminer les données en ne connaissant que les réseaux et non chaque hôte individuel.
    - Il permet de regrouper plusieurs réseaux logiques sur un même réseau physique si leurs parties réseau sont différentes.




## Questionnaire

Voici tes réponses avec des explications pour en faire une fiche de révision :

---

### **Correction et explications du questionnaire sur IPv4**

#### **Question 1 :**

✅ **Chaque adresse IP doit être unique au sein du réseau local.**  
**Explication :** Une adresse IPv4 est une adresse logique qui doit être unique dans un réseau local (LAN) pour éviter les conflits d’adresses et permettre une communication correcte entre les périphériques.

#### **Question 2 :**

✅ **4**  
**Explication :** Une adresse IPv4 est composée de **32 bits**, soit **4 octets** (1 octet = 8 bits).

#### **Question 3 :**

✅ **Partie réseau**  
✅ **Partie hôte**  
**Explication :** Une adresse IPv4 est divisée en **deux parties** :

- **Partie réseau** : Identifie le réseau auquel appartient l’hôte.
- **Partie hôte** : Identifie l’équipement spécifique au sein du réseau.

#### **Question 4 :**

✅ **À déterminer le sous-réseau auquel l'hôte appartient**  
**Explication :** Le **masque de sous-réseau** est utilisé pour identifier la partie réseau et la partie hôte d’une adresse IPv4, permettant ainsi de savoir à quel sous-réseau appartient un appareil.

#### **Question 5 :**

✅ **Une imprimante avec une carte réseau intégrée**  
✅ **Un serveur avec deux cartes réseau**  
✅ **Un téléphone IP**  
**Explication :** Les périphériques nécessitant une adresse IP sont ceux qui communiquent sur un réseau. Une imprimante en réseau, un serveur et un téléphone IP ont tous besoin d’une IP pour fonctionner.

#### **Question 6 :**

✅ **Un réseau physique peut connecter plusieurs périphériques de différents réseaux logiques IPv4.**  
**Explication :** Un même réseau physique (LAN) peut transporter plusieurs réseaux logiques IPv4 grâce au **routage** et à l’utilisation de VLANs.

#### **Question 7 :**

✅ **32 bits**  
**Explication :** Une adresse IPv4 est composée de **32 bits** répartis en 4 octets (exemple : 192.168.1.1).

#### **Question 8 :**

✅ **172.16.34.0**  
**Explication :** Avec un **masque 255.255.255.0**, la partie réseau est déterminée par les **trois premiers octets**. Ici, l’adresse **172.16.34.10** appartient au réseau **172.16.34.0**.

#### **Question 9 :**

✅ **IPv4 est un schéma d'adressage logique.**  
✅ **Un schéma d'adressage IPv4 est hiérarchique.**  
**Explication :**

- IPv4 est **logique** car elle est attribuée par configuration logicielle, contrairement aux adresses MAC qui sont physiques.
- L’adressage IPv4 est **hiérarchique**, car il sépare la partie réseau et la partie hôte.

#### **Question 10 :**

✅ **192.168.10.2**  
✅ **192.168.10.56**  
**Explication :** Avec un masque **255.255.255.0**, les adresses appartenant au même réseau doivent partager les **trois premiers octets**. Ici, **192.168.10.2** et **192.168.10.56** appartiennent au même réseau **192.168.10.0**.

#### **Question 11 :**

✅ **Routage**  
**Explication :** Pour permettre aux équipements de **différents réseaux logiques** de communiquer, un **routeur** est nécessaire. Il assure l’acheminement des paquets entre réseaux distincts.
