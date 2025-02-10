
# 9.1.11 Gérer les menaces liées aux dispositifs


Vous avez indiqué que @Apollo peut mettre en œuvre un certain nombre de mesures pour gérer les menaces qui pèsent sur les équipements.

- Développer des stratégies pour les mots de passe et la protection par mot de passe sur tous les appareils.
- Activer le verrouillage d'écran pendant les périodes d'inactivité.
- Désactiver les droits d'administrateur pour les utilisateurs.
- Définir les politiques, les normes, les procédures et les directives en matière de contrôle d'accès.
- Mettre à jour et appliquer un correctif à l'ensemble des systèmes d'exploitation et des logiciels.
- Implémenter des solutions antivirus automatisées qui analysent le système et mettent à jour le logiciel antivirus afin de garantir une protection adéquate.
- Désactivez tous les ports CD, DVD et USB.
- Activez les analyses antivirus automatiques pour tout CD, DVD ou clé USB inséré.
- Utilisez le filtrage de contenu pour bloquer l'accès à des contenus Web inappropriés ou offensants.
- Rendre obligatoire une formation annuelle de sensibilisation à la sécurité ou mettre en œuvre des campagnes et des programmes de sensibilisation à la sécurité.
- Développez une liste d'applications approuvées pour empêcher l'installation de logiciels non autorisés.


----

# 9.2.5 Check

**Vrai.** Les points d’extrémité sont tous les périphériques connectés au réseau et auxquels d'autres points d’extrémité peuvent accéder ou y être accédés.

**Les logiciels antivirus/antimalwares basés** sur les signatures détectent les virus sur la base des détails spécifiques des fichiers de virus.

Les tables IP et les wrappers TCP sont des exemples de logiciels de **pare-feu basés** sur l'hôte Linux.

Un **dispositif de sécurité Web** filtre les demandes adressées à l'Internet et utilise la liste de blocage pour empêcher les points d'extrémité d'accéder à des sites Web malveillants.

**NAC (Network Admission and Control)** Permet uniquement aux systèmes autorisés et conformes de se connecter au réseau.



----

# 9.3

**iptables** permet aux administrateurs de systèmes Linux de configurer les règles d'accès au réseau qui font partie des modules Netfilter du noyau Linux.

**Pare-feu Windows** utilise une approche basée sur les profils pour configurer les fonctionnalités de pare-feu.

**TCP Wrappers** est un système de contrôle et de journalisation basé sur des règles pour Linux.

**La stratégie basée sur les anomalies** utilise un modèle de base appris de comportement normal.


----

# 9.4 
## Résumé des Surfaces d'Exposition aux Attaques

### Surface d'Exposition aux Attaques Réseau
Les attaques réseau exploitent les vulnérabilités des réseaux, y compris les protocoles filaires et sans fil classiques, ainsi que d'autres protocoles sans fil utilisés par les smartphones et les appareils IoT. Ces attaques ciblent également les vulnérabilités des couches réseau et transport.

#### Surface d'Exposition aux Attaques par Logiciels
Les attaques exploitent les vulnérabilités dans les applications logicielles, qu'elles soient web, en nuage ou basées sur l'hôte.

#### Surface d'Exposition aux Attaques Humaines
Les attaques exploitent les faiblesses du comportement des utilisateurs. Cela inclut l'ingénierie sociale, le comportement malveillant de personnes de confiance et les erreurs de l'utilisateur.


## 9.4.2 Liste de Blocage et Liste d'Autorisation des Applications

#### Liste de Blocage
- Réduit la surface d'exposition aux attaques en limitant l'accès aux menaces potentielles.
- Dicte quelles applications utilisateur ne sont pas autorisées à s'exécuter sur un ordinateur.

#### Liste d'Autorisation
- Spécifie quels programmes sont autorisés à s'exécuter.
- Créée en fonction d'une base de sécurité établie par une organisation.
- Les logiciels non autorisés peuvent violer la ligne de base de sécurité établie, augmentant ainsi le risque.

#### Applications de Liste Blanche et Liste Noire
- Sites web et applications peuvent figurer sur des listes blanches et des listes noires.
- Les listes noires sont mises à jour par des services de sécurité et distribuées aux pare-feu et autres systèmes de sécurité.

## Résumé : 9.4.3 Sandboxing Basé sur les Systèmes

#### Sandboxing
- Technique consistant à analyser les fichiers suspects et à les exécuter dans un environnement sécurisé.
- Analyse automatisée des malwares pour déterminer leurs caractéristiques et créer des défenses contre eux.

#### Evolution des Malwares
- Les malwares polymorphes évoluent fréquemment, et de nouveaux malwares apparaissent régulièrement.
- Même les systèmes de sécurité les plus résistants peuvent laisser passer des malwares.

#### Systèmes de Détection et Sandboxing
- Systèmes tels que Cisco AMP et Cisco Threat Grid Glovebox suivent et analysent les fichiers.
- Cuckoo Sandbox est une sandbox gratuite populaire pour l'analyse des malwares.
- Services en ligne comme VirusToTAL, Joe Sandbox et CrowdStrike Falconon Sandbox permettent de télécharger des échantillons de malwares pour analyse.

#### Outil en Ligne ANY.RUN
- Offre une fonctionnalité de reporting interactif riche avec des détails sur les malwares.
- Capture des captures d'écran du programme malveillant et affiche l'activité réseau et les requêtes DNS.
- Fournit des indicateurs de compromission et mappe les tactiques des malwares à la matrice MITRE ATTACK.
