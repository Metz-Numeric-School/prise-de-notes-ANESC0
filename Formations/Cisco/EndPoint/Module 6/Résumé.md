
# Dispositifs de sécurité

Il existe plusieurs types de pare-feu :

- **Pare-feu de filtrage des paquets (apatride)** : Assure le filtrage de couche 3 et parfois de couche 4. La conception des pare-feu repose principalement sur des interfaces d'appareils qui autorisent ou refusent le trafic en fonction de la source, de la destination et du type de trafic.
  
- **Pare-feu d'inspection (avec état)** : Autorise ou bloque le trafic selon l'état, le port et le protocole.
  
- **Pare-feu de la passerelle d'applications (pare-feu proxy)** : Filtre les informations au niveau des couches 3, 4, 5 et 7.
  
- **Pare-feu de nouvelle génération** : Fournissent des services supplémentaires au-delà des passerelles d'application, tels que :
  - La prévention intégrée des intrusions
  - La sensibilisation et le contrôle des applications pour voir et bloquer les applications à risque
  - L'accès aux futurs flux d'informations
  - Des techniques permettant de faire face aux menaces de sécurité en constante évolution

Les **systèmes de prévention des intrusions (IPS)** et les **systèmes de détection des intrusions (IDS)** sont utilisés pour détecter les risques potentiels de sécurité et alerter/arrêter le trafic dangereux. IDS/IPS peut être implémenté en tant qu'hôte ou réseau avec des avantages et des inconvénients spécifiques à chaque implémentation.

Des **appliances de sécurité spécialisées** sont disponibles, notamment :
- Protection avancée contre les logiciels malveillants de Cisco (AMP)
- Cisco Web Security Appliance (WSA)
- Cisco Email Security Appliance (ESA)

Ces appliances de sécurité utilisent les services de **Cisco Talos Security Intelligence and Research Group**. L'équipe Talos identifie et met en corrélation les attaques en temps réel grâce au réseau de détection le plus étendu au monde.



-----


# Services de sécurité

Les services de sécurité réseau incluent les technologies suivantes :

- **Listes de contrôle d'accès (ACL)** : Une série de commandes qui déterminent si un routeur achemine ou abandonne les paquets en fonction des informations contenues dans l'en-tête de paquet.
  
- **NTP (Network Time Protocol)** : Synchronise l'heure sur tous les appareils du réseau afin d'assurer un horodatage précis et cohérent des messages système.
  
- **Serveurs Syslog** : Permettent d'accéder aux messages système générés par les périphériques réseau.
  
- **SNMP (Simple Network Management Protocol)** : Permet aux administrateurs réseau de contrôler et de gérer les performances du réseau, d'identifier et de résoudre les problèmes et d'anticiper la croissance du réseau.
  
- **NetFlow** : Une technologie Cisco qui fournit des statistiques sur les paquets transitant par un routeur ou un commutateur multicouche Cisco.
  
- **Mise en miroir du port** : Une fonctionnalité qui permet à un commutateur de dupliquer des copies du trafic qui le traverse, puis d'envoyer les données depuis un port équipé d'un système de surveillance du réseau.
  
- **AAA (Authentication, Authorization, and Accounting)** : Un cadre pour configurer les services d'authentification, d'autorisation et de comptabilité des utilisateurs. AAA utilise généralement un serveur TACACS+ ou RADIUS pour cette fin.
  
- **VPN (Virtual Private Network)** : Des réseaux privés créés entre deux terminaux sur un réseau public.




-----

# Fiche de Révision : Infrastructure de Sécurité des Réseaux

**Quel est le but d'un pare-feu personnel sur un ordinateur ?**
- **Pour filtrer le trafic qui se déplace à l'intérieur et à la sortie du PC** : Un pare-feu personnel est conçu pour contrôler le trafic réseau entrant et sortant de l'ordinateur, protégeant ainsi contre les accès non autorisés.

**Quelle est la principale différence entre la mise en œuvre des dispositifs IDS et IPS ?**
- **Un IDS permettrait au trafic malveillant de passer avant qu'il ne soit adressé, alors qu'un IPS l'arrête immédiatement** : IDS (Système de détection d'intrusion) détecte le trafic suspect sans intervenir, tandis que l'IPS (Système de prévention d'intrusion) bloque activement le trafic malveillant.

**Quel protocole offrant des services d'authentification, d'intégrité et de confidentialité est également un type de réseau privé virtuel ?**
- **IPsec** : IPsec est un protocole qui assure des communications sécurisées sur un réseau IP en offrant des services d'authentification, d'intégrité et de confidentialité.

**Parmi les affirmations suivantes, laquelle est une caractéristique du protocole TACACS+ ?**
- **Il chiffre tout le corps du paquet pour des communications plus sécurisées** : TACACS+ chiffre l'intégralité du contenu des paquets, garantissant ainsi des communications sécurisées entre les dispositifs.

**Quelle fonctionnalité du pare-feu permet de s'assurer que les paquets entrants sur un réseau sont des réponses légitimes à des requêtes provenant d'hôtes internes ?**
- **Filtrage dynamique de paquets (SPI)** : SPI (Stateful Packet Inspection) vérifie que les paquets entrants correspondent à des requêtes initiées par des hôtes internes, assurant ainsi leur légitimité.

**Quel terme est utilisé pour décrire le réseau « A » qui contient plusieurs serveurs d'entreprise auxquels des hôtes accèdent via Internet ?**
- **DMZ** : La **zone démilitarisée (DMZ)** est une sous-région du réseau où les serveurs accessibles depuis l'extérieur (Internet) sont placés. Cette configuration permet de sécuriser le réseau interne tout en rendant les services externes disponibles aux utilisateurs.

**Quelle déclaration décrit la sécurité Web Cisco Cloud ?**
- **Il s'agit d'un service de sécurité basé sur le cloud permettant d'analyser le trafic à la recherche de logiciels malveillants et d'appliquer des politiques de sécurité** : Cisco Cloud Web Security (CWS) offre une protection en nuage pour analyser et filtrer le trafic Web en temps réel.

**Quels énoncés à propos des serveurs NTP dans un réseau d'entreprise sont corrects ? (Choisissez deux réponses.)**
- **Les serveurs NTP de strate 1 sont connectés directement à une source temporelle faisant autorité.**
- **Les serveurs NTP assurent un horodatage précis des informations de journalisation et de débogage.**

**Comment une adresse IP source est-elle utilisée dans une liste de contrôle d'accès standard ?**
- **Il s'agit du critère utilisé pour filtrer le trafic** : Dans une ACL standard, l'adresse IP source est utilisée pour déterminer si le trafic doit être autorisé ou bloqué.

**Quel service réseau permet aux administrateurs de surveiller et de gérer les périphériques réseau ?**
- **SNMP** : Le protocole simple de gestion de réseau (SNMP) permet aux administrateurs de surveiller et de gérer les périphériques réseau.

**Pouvez-vous citer une fonction d'un pare-feu proxy ?**
- **Il se connecte à des serveurs distants pour le compte de clients** : Un pare-feu proxy agit en tant qu'intermédiaire entre le client et le serveur, établissant la connexion en leur nom et filtrant le trafic.

**Quelle technologie de surveillance du réseau permet à un commutateur de copier et de transférer le trafic envoyé et reçu sur plusieurs interfaces, via une autre interface, vers un dispositif d'analyse du réseau ?**
- **Mise en miroir des ports** : La mise en miroir des ports permet de copier le trafic réseau de plusieurs interfaces vers une autre interface pour l'analyse.

J'espère que cette fiche de révision te sera utile ! Si tu as d'autres questions ou besoin d'aide supplémentaire, fais-le moi savoir. 😊