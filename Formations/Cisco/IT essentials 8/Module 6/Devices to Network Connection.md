


## Address MAC

![[Pasted image 20250222134352.png]]


## IPv4 address
![[Pasted image 20250222134416.png]]

## IPv6 address
![[Pasted image 20250222134431.png]]
### 2 Règles
![[Pasted image 20250222134018.png]]
![[Pasted image 20250222134038.png]]
![[Pasted image 20250222134105.png]]


---

## **6.1.1.9 Static Addressing**

### 📌 **Définition**

Le **Static Addressing** (adressage statique) consiste à attribuer manuellement une adresse IP unique à chaque appareil d’un réseau. Cette méthode offre un contrôle total sur l’adressage mais peut devenir difficile à gérer dans de grands environnements.

### ⚙️ **Configuration d'une adresse IPv4 sur Windows**

Sur un PC Windows, il est possible de configurer les paramètres IP suivants :

- **IP Address** 🏠 : Identifie l’appareil sur le réseau.
- **Subnet Mask** 🌐 : Délimite le réseau auquel l’appareil appartient.
- **Default Gateway** 🚪 : Adresse du routeur utilisé pour accéder à Internet ou à d’autres réseaux.
- **Valeurs optionnelles** :
    - **DNS principal** 🔍 : Serveur DNS utilisé pour la résolution des noms de domaine.
    - **DNS secondaire** 🔄 : Serveur de secours en cas d’indisponibilité du DNS principal.

### ✅ Avantages et ❌ Inconvénients

✅ **Avantages**  
✔️ Contrôle total des adresses IP attribuées.  
✔️ Idéal pour les serveurs et équipements nécessitant une IP fixe.  
✔️ Pas de dépendance à un serveur DHCP.

❌ **Inconvénients**  
⚠️ Configuration manuelle longue et source d’erreurs.  
⚠️ Gestion complexe dans les grands réseaux.  
⚠️ Risque de conflits d’adresses IP.

### 🏗️ **Cas d'utilisation**

🔹 Serveurs (web, mail, fichiers, DNS, etc.).  
🔹 Imprimantes et périphériques réseau.  
🔹 Appareils IoT critiques.  
🔹 Stations de travail nécessitant une IP fixe.

---

## 6.1.1.10 **Dynamic Addressing**

### 📌 **Définition**

Le **Dynamic Addressing** repose sur un **serveur DHCP** (Dynamic Host Configuration Protocol) qui attribue automatiquement une adresse IP aux appareils d’un réseau. Cela simplifie la gestion et réduit les risques d’erreurs (adresses dupliquées ou invalides).

### ⚙️ **Comment fonctionne le DHCP ?**

Par défaut, la plupart des appareils demandent automatiquement une adresse IP à un serveur DHCP.  
Lorsqu’un ordinateur est configuré pour obtenir une IP **automatiquement**, toutes les autres options de configuration IP deviennent inaccessibles.

### 🛠️ **Informations attribuées par le serveur DHCP**

- **IPv4 Address** 🏠 : Adresse IP attribuée dynamiquement.
- **Subnet Mask** 🌐 : Identifie le réseau auquel l’appareil appartient.
- **Default Gateway** 🚪 : Routeur utilisé pour accéder à d’autres réseaux.
- **Valeurs optionnelles** 🔍 : Serveurs DNS principal et secondaire.

### 🌍 **DHCP et IPv6**

Le DHCP est également disponible pour l’adressage IPv6.

**📌 Remarque :** La configuration d’un PC Windows pour obtenir une adresse IP via DHCP se fait dans **Panneau de configuration > Centre Réseau et partage > Modifier les paramètres de la carte**.

---

# 6.1.4 Firewall Settings

----

## **6.1.4.2 UPnP**

### 📌 **Définition**

Le **Universal Plug and Play (UPnP)** permet aux appareils de s’ajouter dynamiquement à un réseau sans intervention utilisateur. Bien que pratique, ce protocole présente de **nombreux risques de sécurité**.

### ⚠️ Risques de sécurité

❌ **Absence d’authentification** : Tous les appareils sont considérés comme fiables.  
❌ **Vulnérabilités multiples** : Exploitable par des malwares pour rediriger le trafic vers des adresses malveillantes.  
❌ **Exposition des routeurs** : De nombreux routeurs domestiques activent UPnP par défaut, augmentant les risques d’attaques.

### 🔒 **Bonnes pratiques**

✔️ **Désactiver UPnP** sur les routeurs et équipements réseau.  
✔️ **Utiliser des outils de scanning** pour détecter d’éventuelles failles liées à UPnP.  
✔️ **Préférer la configuration manuelle des ports** pour éviter les ouvertures non contrôlées.

---

## **6.1.4.3 DMZ (Demilitarized Zone)**

### 📌 Définition

Une **DMZ** est un réseau intermédiaire permettant d’exposer des services accessibles depuis Internet tout en protégeant le réseau interne.

### ⚙️ **Utilisation d’une DMZ**

- 🔹 Hébergement de **serveurs web, mail ou FTP** accessibles depuis l’extérieur.
- 🔹 **Isolation du réseau interne** pour limiter les risques d’attaques.
- 🔹 Gestion par un **pare-feu** qui filtre le trafic entrant et sortant.

### 🛡️ **Exemple**

Un serveur web peut être placé en DMZ avec une IP statique (ex. **10.10.10.50**). Cela permet aux utilisateurs externes d’y accéder sans mettre en danger le réseau interne.

---

## **6.1.4.4 Port Forwarding**

### 📌 Définition

Le **port forwarding** est une méthode permettant de rediriger le trafic réseau vers un appareil spécifique du réseau local en fonction du port utilisé.

### ⚙️ **Fonctionnement**

1️⃣ **Un pare-feu matériel** peut bloquer certains ports pour sécuriser le réseau.  
2️⃣ **Certains services nécessitent une ouverture de ports** (ex: HTTP, HTTPS, FTP).  
3️⃣ **Le routeur redirige le trafic** en fonction du port destination vers l’appareil concerné.

### 📡 **Exemple**

Un serveur web local utilise le port **80** pour HTTP. Si un utilisateur externe tente d’accéder au site, le routeur identifie la requête et redirige le trafic vers l’IP interne du serveur.

### 🔄 **Port Triggering**

Contrairement au port forwarding classique, le **port triggering** ouvre temporairement un port en fonction d’une activité sortante.

📌 **Exemple** :  
🎮 Un jeu en ligne utilise les ports **27000-27100** pour se connecter.  
💬 Une application de chat associée utilise le port **56**.  
🔄 Si du trafic sortant est détecté sur **27000-27100**, le routeur autorise temporairement l’entrée du trafic sur le port **56**.  
⏳ Dès que l’activité cesse, la redirection est désactivée.

### ✅ **Cas d’usage**

✔️ Hébergement de **serveurs web ou FTP** sur un réseau local.  
✔️ Jeux en ligne nécessitant des **connexions spécifiques**.  
✔️ Accès à des services distants sécurisés.

---

## MAC Address Filtering (6.1.4.5)

#### **Définition**

Le filtrage des adresses MAC permet de spécifier quels appareils sont autorisés ou bloqués sur un réseau. De nombreux routeurs ne permettent que l'une des deux options : autoriser ou bloquer des adresses MAC, mais pas les deux. En général, les techniciens configurent les adresses MAC autorisées.

L'adresse MAC d'un ordinateur Windows peut être obtenue avec la commande `ipconfig /all`.

#### **Limitations**

- L'ajout de nouveaux appareils nécessite une mise à jour manuelle de la liste des adresses MAC autorisées.
    
- Certains appareils nomment l'adresse MAC différemment (ex. "Physical Address" sous Windows).
    
- La gestion manuelle des adresses MAC peut devenir fastidieuse, surtout sur un grand réseau.
    

Dans certains cas, le filtrage MAC est la seule option disponible, bien que des solutions plus avancées comme la sécurité des ports nécessitent un matériel plus coûteux.

---

## *Whitelisting and Blacklisting* (6.1.4.6)

#### **Définition**

Le whitelisting (liste blanche) et le blacklisting (liste noire) permettent de spécifier quelles adresses IP sont autorisées ou bloquées sur un réseau. Cette configuration se fait généralement via une liste d'accès sur un routeur.

#### **Utilisation**

- Le **whitelisting** permet de restreindre l'accès à certains utilisateurs autorisés.
    
- Le **blacklisting** bloque explicitement l'accès à des sites ou des IP connues comme malveillantes.
    

#### **Limitations**

Comme pour le filtrage MAC, la gestion manuelle des adresses peut devenir complexe. Des solutions plus avancées existent, comme les logiciels de contrôle parental et les filtres de contenu.


