## 6.2.2 Contrôle du trafic avec ACLs

Une liste de contrôle d'accès (ACL) est une série de commandes qui déterminent si un appareil achemine ou abandonne les paquets en fonction des informations contenues dans l'en-tête de paquet. Une fois configurées, les ACL assurent plusieurs fonctions :
![[Pasted image 20250202160120.png]]

- **Limitation du trafic réseau** : Elles améliorent les performances du réseau en bloquant certains types de trafic non souhaités (ex. blocage du trafic vidéo).
    
- **Contrôle du flux de trafic** : Elles restreignent la propagation des mises à jour de routage pour s'assurer qu'elles proviennent de sources reconnues.
    
- **Sécurisation de l'accès réseau** : Elles peuvent autoriser un hôte à accéder à une section du réseau tout en en bloquant un autre.
    
- **Filtrage du trafic selon son type** : Par exemple, une ACL peut autoriser le trafic des e-mails tout en bloquant Telnet.
    
- **Filtrage des hôtes et des services** : Elles permettent ou refusent l'accès à certains services comme FTP ou HTTP.
    
- **Priorisation du trafic** : Elles permettent de classer le trafic pour optimiser les performances (ex. accès prioritaire à certains services).

    

## 6.2.3 ACLs : Caractéristiques importantes

Il existe deux types de listes de contrôle d'accès IPv4 Cisco :

1. **ACLs standards** : Elles autorisent ou refusent le trafic en fonction de l'adresse IPv4 source uniquement.
    
2. **ACLs étendues** : Elles filtrent les paquets en fonction de plusieurs critères :
    
    - Type de protocole
        
    - Adresse IPv4 source
        
    - Adresse IPv4 de destination
        
    - Ports TCP/UDP source et destination
        
    - Informations supplémentaires sur le protocole pour un contrôle plus précis
        

Les ACLs peuvent être identifiées par un numéro ou un nom. L'utilisation de noms est recommandée pour une meilleure lisibilité.

Les ACLs peuvent aussi :

- Générer des journaux (log) pour suivre les activités filtrées.
    
- Autoriser uniquement le trafic TCP ayant déjà une session établie, empêchant ainsi les connexions TCP non sollicitées.
    

## 6.2.5 SNMP

Le protocole **SNMP (Simple Network Management Protocol)** permet aux administrateurs de surveiller et gérer les équipements réseau. Il se compose de :

- **Un gestionnaire SNMP** : Exécute un logiciel de gestion SNMP et collecte/modifie les informations des équipements réseau.
    
- **Des agents SNMP** : Sont intégrés aux appareils et communiquent avec le gestionnaire.
    
- **Une base de données MIB (Management Information Base)** : Stocke les données et statistiques de chaque appareil.



Le gestionnaire SNMP peut récupérer des informations (« get ») ou modifier les configurations (« set »). Les agents peuvent aussi envoyer des alertes (« trap ») en cas de problème.

![[Pasted image 20250202160146.png]]


----

## 6.2.6 NetFlow

NetFlow est une technologie Cisco qui fournit des statistiques sur les paquets circulant sur un réseau. Contrairement à SNMP, NetFlow se concentre sur l'analyse des flux de trafic.

![[Pasted image 20250202160222.png]]

NetFlow permet :

- La surveillance du réseau et la détection d'anomalies.
    
- L'analyse du trafic pour identifier les goulots d'étranglement.
    
- La facturation IP basée sur l'utilisation du réseau.
    

Un flux NetFlow est défini par 7 paramètres :

- Adresse IP source et destination
    
- Ports source et destination
    
- Type de protocole (TCP, UDP, ICMP, etc.)
    
- Marquage ToS (Type of Service)
    
- Interface logique d'entrée
    

NetFlow envoie ces données vers un serveur appelé **connecteur NetFlow** pour analyse.



-----


## 6.2.7 Miroir de port

Un **analyseur de paquets** capture le trafic réseau pour analyse. Comme les commutateurs isolent le trafic, l'analyse en temps réel peut être difficile.

![[Pasted image 20250202160241.png]]

La **mise en miroir de port** permet à un commutateur de copier le trafic et de l'envoyer à un port spécifique pour surveillance, sans perturber le trafic original. Ceci est utile pour :

- Les systèmes IDS/IPS.
    
- L'analyse des performances réseau.
    
- Le dépannage des problèmes réseau.
    

## 6.2.8 Serveurs Syslog

Le protocole **Syslog** permet aux équipements réseau (routeurs, commutateurs, pare-feu, etc.) d'envoyer leurs logs à un serveur central.

![[Pasted image 20250202160254.png]]

Les fonctions principales de Syslog :

- **Collecte des logs** pour la surveillance et le dépannage.
    
- **Filtrage des logs** selon leur importance.
    
- **Stockage et alerte** en fonction de l'impact des événements.
    

Syslog facilite la gestion des logs en centralisant les informations critiques pour la sécurité et la maintenance du réseau.



---

### **6.2.8 Serveurs Syslog**

![[Pasted image 20250202161003.png]]


Syslog est un protocole utilisé pour **centraliser les logs** des équipements réseau. Il permet :

- De collecter et stocker les journaux système.
- De choisir les types d’événements à enregistrer.
- De définir une destination pour les logs (serveur Syslog).

Les logs sont essentiels pour le **dépannage et la surveillance** du réseau.

### **6.2.9 NTP**

Le protocole **NTP (Network Time Protocol)** permet de synchroniser l’horloge des équipements réseau avec une source de temps fiable.
![[Pasted image 20250202161016.png]]


Le réseau NTP est organisé en **strates** :

- **Strate 0** : Horloges de référence précises (exemple : horloge atomique).
- **Strate 1** : Serveurs directement connectés aux horloges de strate 0.
- **Strate 2 et inférieures** : Appareils synchronisés avec les serveurs de strate 1.

Une **heure synchronisée** est essentielle pour la sécurité, la gestion des logs et l’analyse des événements réseau.

### **6.2.10 Serveurs AAA**

Le cadre **AAA (Authentication, Authorization, Accounting)** fournit trois fonctions essentielles :

- **Authentification** : Vérifie l’identité des utilisateurs.
- **Autorisation** : Détermine les ressources accessibles.
- **Accounting (Gestion des comptes)** : Suit les actions des utilisateurs.

#### **Comparaison entre TACACS+ et RADIUS**

|**Caractéristique**|**TACACS+** (Cisco)|**RADIUS** (Standard ouvert)|
|---|---|---|
|**Séparation AAA**|Oui (modulaire)|Non (authentification et autorisation combinées)|
|**Protocole**|TCP|UDP|
|**Chiffrement**|Chiffre tout le paquet|Chiffre uniquement le mot de passe|
|**Personnalisation**|Autorisation des commandes par utilisateur|Moins flexible|

### **6.2.11 VPN**

Un **VPN (Virtual Private Network)** permet d’établir une connexion sécurisée sur un réseau public comme Internet.
![[Pasted image 20250202161031.png]]


Les VPN peuvent être :

- **Site à site** : Connexion sécurisée entre deux réseaux distants.
- **Accès distant** : Permet aux utilisateurs de se connecter au réseau de l’entreprise depuis l’extérieur.

Le protocole **IPsec** est souvent utilisé pour sécuriser les communications avec **chiffrement et authentification**.



-----


## 6.2.12 Vérifiez votre compréhension - Infrastructure de sécurité des réseaux

#### Question 1
**Qui permet à un commutateur de dupliquer des copies du trafic qui transite via un commutateur, puis de les envoyer depuis un port équipé d'un système de surveillance du réseau ?**
- **Mise en miroir des ports** : La mise en miroir des ports (ou Port Mirroring) permet à un commutateur de copier le trafic traversant un port ou une VLAN et de l'envoyer vers un port spécifique pour la surveillance et l'analyse.

#### Question 2
**Qu'est-ce qu'une série de commandes qui contrôlent si un appareil transmet ou dépose des paquets en fonction des informations trouvées dans l'en-tête du paquet ?**
- **ACL** : Une liste de contrôle d'accès (ACL) est une série de règles qui déterminent si le trafic est autorisé ou bloqué en fonction des informations contenues dans l'en-tête des paquets.

#### Question 3
**Qu'est-ce qui fournit des statistiques sur les flux de paquets qui passent par un appareil de réseau ?**
- **NetFlow** : NetFlow est un protocole qui collecte et analyse les informations sur les flux de données traversant un appareil de réseau, fournissant des statistiques détaillées sur le trafic.

#### Question 4
**Qu'est-ce qu'un réseau privé créé sur un réseau public ?**
- **VPN** : Un réseau privé virtuel (VPN) permet de créer un tunnel sécurisé sur un réseau public comme Internet, créant ainsi un réseau privé pour les utilisateurs.

#### Question 5
**Qu'est-ce qui définit la date et l'heure sur les appareils réseau ?**
- **Protocole NTP** : Le protocole de temps réseau (NTP) synchronise les horloges des appareils réseau avec une source de temps précise et fiable, définissant ainsi la date et l'heure.

#### Question 6
**Qu'est-ce qui collecte diverses statistiques pour les appareils configurés pour consigner et envoyer des messages ?**
- **Syslog** : Syslog est un protocole standard utilisé pour envoyer des messages de journalisation et de notification à un serveur centralisé, collectant ainsi des statistiques et des informations sur les événements des appareils réseau.

#### Question 7
**Qu'est-ce qui permet aux administrateurs de contrôler et de gérer les appareils réseau ?**
- **SNMP** : Le protocole simple de gestion de réseau (SNMP) permet aux administrateurs de surveiller, de contrôler et de gérer les appareils réseau à distance.

#### Question 8
**Qu'est-ce qu'authentifie les utilisateurs pour l'accès à des ressources de réseau spécifiques et enregistre leurs activités lorsqu'ils sont connectés à ces ressources ?**
- **Serveur AAA** : Un serveur d'authentification, d'autorisation et de comptabilité (AAA) vérifie les identités des utilisateurs, contrôle leur accès aux ressources réseau et enregistre leurs activités.

