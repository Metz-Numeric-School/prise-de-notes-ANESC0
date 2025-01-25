
## **Communications sans fil**

Les périphériques de mise en réseau sans fil se connectent à un **point d'accès (AP)** ou à un **contrôleur de réseau local sans fil (WLC)** conformément à la norme **802.11**.

### **Principes de fonctionnement :**

- Le **format de trame 802.11** est similaire à celui de l'Ethernet mais comporte des champs additionnels.
- Les appareils WLAN utilisent un accès multiple à **détection de porteuse avec prévention des collisions (CSMA/CA)** pour déterminer comment et quand envoyer des données.
- Processus de connexion au WLAN :
    1. **Découverte** d'un point d'accès.
    2. **Authentification** auprès du point d'accès.
    3. **Association** au point d'accès.

Les points d'accès peuvent être :

- **Autonomes** : Configurés individuellement.
- **Centralisés** : Gérés par un WLC pour faciliter la configuration et la surveillance de plusieurs points d'accès.

---

## **Menaces visant le réseau WLAN**

Les réseaux sans fil sont vulnérables à plusieurs menaces :

1. **Interception de données**
2. **Intrus sans fil**
3. **Attaques DoS**
4. **Points d'accès malveillants**

### **Détails des menaces :**

- **Attaques DoS sans fil** :
    
    - Causées par des appareils mal configurés.
    - Interférences intentionnelles ou accidentelles avec la communication sans fil.
- **Point d'accès non autorisé** :
    
    - Connecté sans autorisation à un réseau d'entreprise.
    - Permet à un acteur malveillant de capturer des **adresses MAC**, **paquets de données**, ou de lancer une attaque MITM.
- **Attaque MITM (Homme au Milieu)** :
    
    - L'attaquant intercepte ou modifie les données entre deux parties légitimes.
    - Exemple courant : **"Evil Twin AP"**, où un point d'accès malveillant imite le **SSID** d’un AP légitime pour tromper les utilisateurs.

### **Prévention des menaces :**

- Configurer les **WLC** avec des politiques spécifiques pour détecter et bloquer les AP malveillants.

---

## **Sécurisation des WLAN**

Pour protéger les données et repousser les intrus, les options de sécurité suivantes sont disponibles :

### **Mesures de base :**

1. **Masquage du SSID**.
2. **Filtrage des adresses MAC**.

### **Techniques d'authentification :**

- **WEP**
- **WPA**
- **WPA2** (préféré sur les routeurs domestiques pour sa robustesse).
- **WPA3** (dispositifs encore rares).

### **Cryptage des données :**

- Les normes WPA et WPA2 utilisent les protocoles :
    - **TKIP** (Temporal Key Integrity Protocol).
    - **AES** (Advanced Encryption Standard).

### **Sécurité avancée :**

Pour des environnements avec des exigences de sécurité strictes :

- Utiliser une authentification et une connexion supplémentaires.
- Mettre en place un serveur **RADIUS** pour :
    - **Authentification**.
    - **Autorisation**.
    - **Comptabilité** (AAA).
