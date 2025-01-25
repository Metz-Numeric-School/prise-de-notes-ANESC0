
## **Services IP**

### **ARP et attaques associées**

Les hôtes diffusent une requête ARP pour déterminer l’adresse MAC correspondant à une adresse IP spécifique.

- **Réponses ARP gratuites** : Un client peut envoyer une réponse ARP non sollicitée, permettant potentiellement à un acteur malveillant de prétendre posséder une adresse IP/MAC.
- **Attaque MITM (Man-in-the-Middle)** : L’empoisonnement du cache ARP peut rediriger le trafic en modifiant les tables ARP des appareils du réseau.

### **DNS et vulnérabilités**

Le protocole DNS (Domain Name System) automatise la correspondance entre les noms de ressources et les adresses IP :

- Utilise des enregistrements de ressources (RR) pour les réponses DNS.
- Vulnérabilités :
    - **Empoisonnement du cache DNS** : Fourniture d’enregistrements falsifiés aux résolveurs ouverts.
    - **Attaques d’amplification et de réflexion DNS** : Exploitent la nature du protocole pour lancer des attaques DoS/DDoS.
    - **Techniques furtives (Fast Flux)** : Changements rapides d’adresses IP ou de serveurs pour masquer des activités malveillantes.
    - **Tunnellisation DNS** : Contourne les solutions de sécurité en encapsulant du trafic non DNS dans le DNS.
    - **DNS dynamique** : Souvent utilisé par les acteurs malveillants.

### **DHCP et usurpation**

Le protocole DHCP diffuse des informations d’adressage IP.

- Une attaque par usurpation DHCP se produit lorsqu’un serveur non autorisé fournit des paramètres IP incorrects, affectant passerelles et DNS.

---

## **Services professionnels**

### **Attaques sur le web**

Les navigateurs sont une cible courante :

- **Attaques drive-by** : Une page compromise redirige vers un site malveillant.
- **Exploitations via plug-ins** : Les vulnérabilités du navigateur ou des extensions sont exploitées.
- **Détection par IDS (Intrusion Detection Systems)** : Analyse les fichiers téléchargés et émet des alertes en cas de menace.

**Prévention :**

- Mettre à jour systèmes et navigateurs.
- Utiliser un proxy web pour bloquer les sites malveillants.
- Adopter les pratiques OWASP lors du développement.

### **Courrier électronique**

- **Phishing et malwares** : Les e-mails véhiculent des charges utiles malveillantes.
- **Vulnérabilités SMTP** : Les serveurs doivent être régulièrement mis à jour.
- **Solutions de sécurité** : Bloquent phishing, spam et logiciels malveillants.

### **Applications web et bases de données**

Les bases de données, contenant des informations sensibles, sont des cibles courantes :

- **Injection SQL** : Exploite des champs d’entrée non sécurisés.
- **XSS (Cross-Site Scripting)** : Exécute des scripts malveillants sur les navigateurs clients.

**Top 10 OWASP** : Liste des principales vulnérabilités pour sécuriser les applications web.

---

## **Atténuation des attaques de réseau courantes**

### **Bonnes pratiques générales**

- Rédiger une politique de sécurité.
- Former les collaborateurs.
- Contrôler l’accès physique.
- Chiffrer les données sensibles.
- Mettre à jour les correctifs et effectuer des audits réguliers.

### **Virus, vers et chevaux de Troie**

- Les logiciels antivirus sont essentiels pour atténuer ces menaces.
- Réponse aux vers :
    - **Confinement**, **inoculation**, **quarantaine** et **traitement**.

### **Reconnaissance et accès non autorisé**

- Authentification stricte et chiffrement.
- Utilisation d’outils anti-renifleurs et de pare-feux.

### **Attaques DoS/DDoS**

- Analyse du trafic réseau en continu.
- Déploiement de systèmes de prévention des intrusions.
