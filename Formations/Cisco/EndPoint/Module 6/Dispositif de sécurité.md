

# Pare-feu
![[Pasted image 20250202150553.png]]

### Propriétés communes des pare-feu

Tous les pare-feu partagent certaines propriétés communes:

- Les pare-feu résistent aux attaques réseau.
- Les pare-feu représentent le seul point de transit entre les réseaux d'entreprises internes et les réseaux externes, car tout le trafic passe par le pare-feu.
- Les pare-feu appliquent la politique de contrôle d'accès.

### Avantages du pare-feu

Il y a plusieurs avantages à utiliser un pare-feu dans un réseau:

- Il empêche les utilisateurs non fiables d'accéder aux hôtes, aux ressources et aux applications sensibles.
- Il assainit le flux de protocoles pour empêcher l'exploitation des failles.
- Il bloque les données malveillantes provenant des serveurs et des clients.
- Il simplifie la gestion de la sécurité en confiant la majeure partie du contrôle d'accès réseau à quelques pare-feu sur le réseau.
### Limitations du pare-feu

Les pare-feu ont également certaines limites:

- Un pare-feu mal configuré peut avoir des conséquences graves pour le réseau. Il peut par exemple constituer un point de défaillance unique.
- Les données de nombreuses applications ne peuvent pas traverser les pare-feu en toute sécurité.
- Les utilisateurs peuvent rechercher proactivement des façons de contourner le pare-feu afin de recevoir des données bloquées, ce qui expose le réseau à des attaques potentielles.
- Les performances du réseau peuvent baisser.
- Le trafic non autorisé peut être placé en tunnel ou masqué comme trafic légitime à travers le pare-feu.
-


## 6.1.3 Architectures de sécurité communes

### **Privés et publics**

Comme illustré à la figure, le réseau public (ou extérieur) n'est pas fiable et le réseau privé (ou intérieur) est fiable.

En règle générale, un pare-feu avec deux interfaces est configuré comme suit:

- Le trafic provenant du réseau privé est autorisé et inspecté au fur et à mesure qu'il se déplace vers le réseau public. Le trafic retour inspecté provenant du réseau public et associé au trafic issu du réseau privé est autorisé.
- Le trafic provenant du réseau public et voyageant vers le réseau privé est généralement bloqué.
![[Pasted image 20250202150757.png]]



-----

### Zone démilitarisée

Une zone démilitarisée (DMZ) est un système de pare-feu comportant généralement une interface interne connectée au réseau privé, une interface externe connectée au réseau public et une interface DMZ, comme illustré à la figure.

- Le trafic provenant du réseau privé est inspecté lorsqu'il se déplace vers le réseau public ou la DMZ. Ce trafic est autorisé avec peu ou pas de restriction. Le trafic inspecté revenant de la DMZ ou du réseau public au réseau privé est autorisé.
- Le trafic provenant du réseau DMZ et se déplaçant vers le réseau privé est généralement bloqué.
- Le trafic provenant du réseau DMZ et voyageant vers le réseau public est autorisé de manière sélective en fonction des exigences du service.
- Le trafic provenant du réseau public et voyageant vers la DMZ est inspecté et autorisé de manière sélective. Il s'agit généralement de trafic e-mail, DNS, HTTP ou HTTPS. Le trafic de retour de la DMZ vers le réseau public est autorisé de manière dynamique.
- Le trafic provenant du réseau public et voyageant vers le réseau privé est bloqué
- ![[Pasted image 20250202150856.png]]


-----

### Pare-feu à politique basée sur les zones

Les pare-feu à politique basée sur les zones (ZPF) utilisent le concept de zones pour assurer une meilleure flexibilité. Une zone est un groupe d'une ou plusieurs interfaces partageant des fonctions ou des caractéristiques similaires. Les zones vous aident à spécifier à quel endroit une règle ou une politique de pare-feu Cisco IOS doit être appliquée. Dans la figure, les politiques de sécurité de LAN 1 et LAN 2 sont semblables et peuvent être regroupées en une zone pour les configurations de pare-feu. Par défaut, le trafic entre les interfaces de la même zone ne fait l'objet d'aucune politique et passe librement. Cependant, tout le trafic entre les zones est bloqué. Pour autoriser le trafic entre les zones, une politique permettant ou inspectant le trafic doit être configurée.

La seule exception à cette politique **nier tout** est la zone auto du routeur. La zone auto est le routeur lui-même et comprend toutes les adresses IP de l'interface du routeur. Les configurations de politique qui incluent la zone auto s'appliquent au trafic destiné au routeur et provenant de celui-ci. Par défaut, il n'y a pas de politique pour ce type de trafic. Le trafic qui doit être pris en compte lors de la conception d'une politique pour la zone auto comprend le trafic du plan de gestion et du plan de contrôle, tel que SSH, SNMP et les protocoles de routage.

La figure de pare-feu de stratégie basée sur une zone montre un cloud Internet dans un cercle étiqueté public. Le cloud se connecte à un pare-feu. Le pare-feu se connecte à un cercle marqué DMZ qui a deux serveurs, un cercle labellisé LAN privé 1 qui a un serveur et deux PC dedans, ainsi qu'un cercle avec un serveur et deux PC dans celui-ci étiqueté LAN privé 2. Il y a une zone de texte avec une flèche indiquant LAN privé 1 et une flèche séparée indiquant LAN privé 2 avec les mots membres de la même zone.

![[Pasted image 20250202151103.png]]


-----


## 6.1.4 Descriptions des types de Pare-feu


### Pare-feu de filtrage de paquets (Sans état)

Les pare-feu de filtrage de paquets sont généralement intégrés aux routeurs et **autorisent ou interdisent le trafic en fonction des informations des couches 3 et 4**. Les pare-feu **«sans état»** effectuent une **recherche simple** dans une table de politiques pour **filtrer le trafic en fonction de critères précis**. Par exemple, un administrateur peut configurer le pare-feu pour **bloquer le port 25** afin d'empêcher la diffusion de virus via le serveur SMTP.

![[Pasted image 20250202151624.png]]

----


### Pare-feu dynamique (Avec état)

Les pare-feu dynamiques, également appelés **pare-feu avec état**, sont très polyvalents et courants. Ils effectuent un **filtrage dynamique des paquets** en utilisant des informations de connexion mises à jour dans une **table d'états**. Ils analysent également le trafic au niveau des **couches OSI 4 et 5**.
![[Pasted image 20250202151632.png]]

----

### Pare-feu de passerelle d'application

Les pare-feu de passerelle d'application (ou **pare-feu proxy**) filtrent les informations aux niveaux des **couches 3, 4, 5 et 7** du modèle OSI. Lorsqu'un client a besoin d'accéder à un serveur distant, il se connecte d'abord à un **serveur proxy**, qui se connecte ensuite au serveur distant au nom du client. Le serveur distant ne voit donc qu'une connexion provenant du serveur proxy.

![[Pasted image 20250202151639.png]]
### Pare-feu de nouvelle génération (NGFW)

Les **pare-feu de nouvelle génération** vont au-delà des pare-feu dynamiques en offrant des fonctionnalités supplémentaires telles que :
- **La prévention des intrusions intégrée**
- **La reconnaissance et le contrôle des applications** pour détecter et bloquer celles présentant un risque
- **Des voies d'évolution** pour inclure les futurs flux d'informations
- **Des techniques pour faire face à l'évolution des menaces pour la sécurité**

### d'autres méthodes d'implémentation d'un pare-feu:

- **Pare-feu basé sur l'hôte (serveur et personnel) -** Un PC ou un serveur sur lequel fonctionne un logiciel de pare-feu.
- **Pare-feu transparent -** Filtre le trafic IP entre une paire d'interfaces pontées.
- **Pare-feu hybride -** Une combinaison des différents types de pare-feu. Par exemple, un pare-feu d'inspection d'application combine un pare-feu dynamique (avec état) avec un pare-feu de passerelle d'application.


## 6.1.5 Check

![[Pasted image 20250202151735.png]]
![[Pasted image 20250202151911.png]]
![[Pasted image 20250202152613.png]]
![[Pasted image 20250202152721.png]]
![[Pasted image 20250202152756.png]]

----


## 6.1.6 Dispositifs de prévention et de détection des intrusions

Un changement de paradigme de l'architecture réseau est nécessaire pour se défendre contre les attaques qui évoluent rapidement. Il doit inclure des systèmes de détection et de prévention rentables, tels que les systèmes de détection d'intrusion (IDS) ou les systèmes de prévention d'intrusion (IPS), plus évolutifs. L'architecture du réseau intègre ces solutions dans les points d'entrée et de sortie du réseau.

Lorsque vous implémentez IDS ou IPS, il est important de connaître les types de systèmes disponibles, à savoir les approches basées sur l'hôte et sur le réseau, le positionnement de ces systèmes, le rôle des catégories de signature et les mesures possibles qu'un routeur Cisco IOS peut prendre quand une attaque est détectée.

La figure montre comment un IPS gère le trafic malveillant refusé.

**Caractéristiques des systèmes de prévention et de détection des intrusions**
![[Pasted image 20250202152904.png]]

### **IDS et IPS** : Détection et Prévention des Intrusions

1. **Le trafic malveillant est envoyé à l'hôte cible à l'intérieur du réseau.**

2. **Le trafic est acheminé vers le réseau et reçu par un capteur compatible IPS où il est bloqué.**

3. **Le capteur compatible IPS envoie des informations de journalisation concernant le trafic à la console de gestion de la sécurité réseau.**

4. **Le capteur IPS tue le trafic (envoyé au « Bit Bucket »).**

**Technologies IDS et IPS** :
   - Les technologies IDS (Intrusion Detection System) et IPS (Intrusion Prevention System) sont toutes deux déployées comme des capteurs.

**Formes de capteurs IDS/IPS** :
   - Un routeur configuré avec le logiciel Cisco IOS IPS
   - Un appareil spécialement conçu pour fournir des services IDS ou IPS dédiés
   - Un module réseau installé dans un ASA (Adaptive Security Appliance), un commutateur ou un routeur

**Utilisation des signatures** :
   - Les technologies IDS et IPS utilisent des **signatures** pour détecter des modèles dans le trafic réseau.
   - Une signature est un ensemble de règles qu'un IDS ou un IPS utilise pour détecter les activités malveillantes.
   - Les signatures peuvent être utilisées pour :
     - Détecter les violations graves de la sécurité
     - Détecter les attaques de réseau courantes
     - Recueillir des informations

 **Types de signatures** :
   - Les technologies IDS et IPS peuvent détecter les modèles de signature **atomiques** (paquet unique) ou **composites** (multipaquets).



-----


## 6.1.7 Avantages et inconvénients des IDS et IPS

### Avantages et Inconvénients des Systèmes IDS et IPS

| La solution | Avantages | Désavantages |
|-------------|-----------|--------------|
| **IDS**         | - Aucun impact sur le réseau (latence, gigue) <br> - Aucun impact sur le réseau en cas de panne du capteur <br> - Aucun impact sur le réseau en cas de surcharge du capteur | - L'action de réponse ne peut pas arrêter les paquets déclencheurs <br> - Réglage correct requis pour les actions de réponse <br> - Plus vulnérable aux techniques de contournement de la sécurité du réseau |
| **IPS**         | - Arrête les paquets déclencheurs <br> - Peut utiliser des techniques de normalisation de flux | - Des problèmes de capteur peuvent affecter le trafic réseau <br> - La surcharge du capteur a un impact sur le réseau <br> - Un certain impact sur le réseau (latence, gigue) |

### Avantages et inconvénients des systèmes **IDS et IPS**

#### IDS (Intrusion Detection System)

✅ **Avantages** :

- Fonctionne en mode hors ligne, sans impact sur les performances réseau.
- N’introduit pas de latence ni de perturbations dans le trafic.
- Ne compromet pas le réseau en cas de panne du capteur.

❌ **Inconvénients** :

- Ne peut pas bloquer les paquets malveillants en temps réel.
- Détection des intrusions peut être longue à paramétrer.
- Vulnérable aux techniques d'évasion de sécurité.

---

#### IPS (Intrusion Prevention System)

✅ **Avantages** :

- Bloque les paquets suspects en temps réel.
- Permet la normalisation des flux pour détecter des attaques sur plusieurs segments.

❌ **Inconvénients** :

- Introduit une latence et peut dégrader les performances réseau.
- Risque d’impact sur les applications sensibles au temps (ex. VoIP).
- Doit être bien dimensionné pour éviter la surcharge.

---

### **Conseils de déploiement**

IDS et IPS peuvent être utilisés ensemble pour une protection optimale. Un IDS peut analyser les paquets en profondeur tandis qu’un IPS se concentre sur la prévention en temps réel. Le choix dépend des objectifs définis dans la politique de sécurité de l’entreprise.



-----
## 6.1.8 Types d’IPS

Il existe deux principaux types de systèmes de prévention des intrusions : **IPS basé sur l’hôte** et **IPS basé sur le réseau**.

### IPS basé sur l’hôte **(HIPS)**

HIPS est un logiciel installé sur un hôte pour surveiller et analyser toute activité suspecte. Il permet de :  
✅ Surveiller les processus du système d’exploitation et les processus critiques.  
✅ Détecter des comportements anormaux comme des modifications non autorisées du registre ou du système.  
✅ Empêcher l’hôte de participer à une attaque DoS ou à une session FTP illicite.  
✅ Fonctionner comme un antivirus, antimalware et pare-feu combinés.

**❌ Inconvénients** :

- Ne protège qu’un seul hôte et n’a pas de vision globale du réseau.
- Doit être installé sur chaque hôte, ce qui peut être contraignant.

---

### IPS basé sur le réseau

Un IPS en réseau repose sur des capteurs placés à des points stratégiques du réseau. Il permet de :  
✅ Détecter en temps réel les activités malveillantes et non autorisées.  
✅ Prendre des mesures immédiates en cas de menace.  
✅ Surveiller l’activité réseau indépendamment de la cible de l’attaque.

L’IPS en réseau est souvent combiné avec des solutions IDS/IPS hôte pour renforcer la sécurité.

![[Pasted image 20250202153950.png]]


---

## **6.1.9 Appareils de sécurité spécialisés**

### **AMP (Protection contre les programmes malveillants)**

Cisco AMP offre une protection avancée contre les malwares à trois niveaux :  
🔹 **Avant** : Bloque les menaces connues et émergentes.  
🔹 **Pendant** : Identifie et neutralise les fichiers malveillants.  
🔹 **Après** : Continue d’analyser l’activité des fichiers pour détecter tout comportement suspect.

AMP exploite l’intelligence du **Cisco Talos Security Intelligence and Research Group** pour identifier les menaces en temps réel.

---

### **WSA (Web Security Appliance)**

WSA est une **passerelle web sécurisée** qui :  
✅ Bloque les sites web dangereux et analyse les sites inconnus avant d’autoriser l’accès.  
✅ Protège contre les logiciels malveillants et contrôle les applications web.  
✅ Assure la sécurité des utilisateurs en mobilité avec la solution cloud **Cisco CWS**.

Cependant, **WSA ne protège pas les utilisateurs se connectant directement à Internet en dehors du réseau protégé**.

---

### **ESA (Email Security Appliance)**

Cisco ESA est une solution de sécurité des e-mails qui :  
✅ Protège contre les spams, les logiciels malveillants et le phishing.  
✅ Analyse les menaces en temps réel avec **Cisco Talos**.  
✅ Contrôle les e-mails sortants pour assurer leur conformité et leur sécurité.

ESA est constamment mis à jour pour détecter les nouvelles menaces et assurer une protection continue.



-----

## 6.1.10 Vérifier votre compréhension - Comparer les caractéristiques des IDS et des IPS
### Comparaison entre IDS et IPS

| Caractéristique                                                                                                                                             | IDS                                             | IPS                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|----------------------------------------------------|
| **Plus vulnérable aux techniques de contournement des défenses du réseau activées par diverses méthodes d'attaque du réseau**                                | ✓                                               |                                                    |
| **Peut dégrader les performances du réseau en ajoutant de la latence et de la gigue**                                                                        |                                                 | ✓                                                  |
| **Doit être implémenté pour éviter de nuire aux applications dépendantes du temps**                                                                          |                                                 | ✓                                                  |
| **Ne peut pas arrêter le paquet déclencheur et n'est pas garanti pour arrêter une connexion**                                                               | ✓                                               |                                                    |
| **Déployé en mode hors ligne**                                                                                                                               | ✓                                               |                                                    |
| **Peut utiliser des techniques de normalisation des flux pour réduire ou éliminer un grand nombre des possibilités d'évasion de la sécurité du réseau**      |                                                 | ✓                                                  |
| **Peut être configuré pour effectuer un abandon de paquets afin d'arrêter le paquet déclencheur**                                                            |                                                 | ✓                                                  |
| **Principalement axé sur l'identification d'incidents possibles, l'enregistrement d'informations sur les incidents et le signalement des incidents**         | ✓                                               |                                                    |
| **Doit être déployé en direct et le trafic doit être capable de passer au travers**                                                                          |                                                 | ✓                                                  |
| **Moins utile pour stopper les virus des e-mails et les attaques automatisées, telles que les vers**                                                         | ✓                                               |                                                    |

#### Explications

1. **Plus vulnérable aux techniques de contournement des défenses du réseau activées par diverses méthodes d'attaque du réseau** :
   - **IDS** : L'IDS détecte les attaques sans les bloquer activement, ce qui le rend plus vulnérable aux contournements.

2. **Peut dégrader les performances du réseau en ajoutant de la latence et de la gigue** :
   - **IPS** : L'IPS inspecte le trafic en temps réel, ce qui peut ajouter de la latence et de la gigue.

3. **Doit être implémenté pour éviter de nuire aux applications dépendantes du temps** :
   - **IPS** : L'IPS doit être configuré soigneusement pour ne pas perturber les applications critiques.

4. **Ne peut pas arrêter le paquet déclencheur et n'est pas garanti pour arrêter une connexion** :
   - **IDS** : L'IDS détecte et signale les incidents sans bloquer les paquets malveillants en temps réel.

5. **Déployé en mode hors ligne** :
   - **IDS** : L'IDS surveille et analyse le trafic sans interférer directement avec le flux de données.

6. **Peut utiliser des techniques de normalisation des flux pour réduire ou éliminer un grand nombre des possibilités d'évasion de la sécurité du réseau** :
   - **IPS** : L'IPS utilise des techniques de normalisation pour réduire les possibilités d'évasion des mesures de sécurité.

7. **Peut être configuré pour effectuer un abandon de paquets afin d'arrêter le paquet déclencheur** :
   - **IPS** : L'IPS peut bloquer activement le trafic malveillant en abandonnant les paquets suspects.

8. **Principalement axé sur l'identification d'incidents possibles, l'enregistrement d'informations sur les incidents et le signalement des incidents** :
   - **IDS** : L'IDS se concentre sur la détection, l'enregistrement et le signalement des activités suspectes.

9. **Doit être déployé en direct et le trafic doit être capable de passer au travers** :
   - **IPS** : L'IPS est déployé en ligne pour analyser et bloquer le trafic réseau en temps réel.

10. **Moins utile pour stopper les virus des e-mails et les attaques automatisées, telles que les vers** :
    - **IDS** : L'IDS est moins efficace pour arrêter les virus et les attaques automatisées en temps réel, car il ne bloque pas activement le trafic.

