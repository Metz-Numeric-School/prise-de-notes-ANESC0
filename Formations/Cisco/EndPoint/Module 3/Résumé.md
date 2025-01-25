
## **Détails d'IP PDU**

L'IP est un protocole sans connexion de couche 3.

- **En-tête IPv4** : Composé de plusieurs champs.
- **En-tête IPv6** : Contient moins de champs.

Les analystes en sécurité doivent être familiers avec les différents champs des en-têtes IPv4 et IPv6.

---

## **Vulnérabilités IP**

Il existe plusieurs types d'attaques ciblant les composants IP. Les attaques courantes incluent :

- **Attaques ICMP**
- **Attaque par déni de service (DoS)**
- **Attaque par déni de service distribué (DDoS)**
- **Attaques par usurpation d'adresse**
- **Attaques de l'homme-au-milieu (MiTM)**
- **Piratage de session**

### **ICMP et attaques associées**

Le protocole ICMP est conçu pour :

- Transporter des messages de diagnostic.
- Signaler des erreurs lorsque des routes, des hôtes ou des ports sont inaccessibles.

Les acteurs de menace exploitent ICMP pour des :

- **Attaques de reconnaissance**
- **Attaques DoS**
- **Techniques d'amplification et de réflexion** pour créer des attaques DoS.
- **Saturation des ressources** pour planter un hôte ou épuiser les ressources du réseau.

### **Usurpation d'adresse IP**

Les attaques par usurpation d'adresse IP se produisent lorsque :

- Un acteur malveillant crée des paquets avec de fausses informations d'adresse IP source.
- Cela permet de masquer l'identité de l'expéditeur ou de se faire passer pour un utilisateur légitime.  
    Les attaques par usurpation peuvent être :
- **Non aveugles** (détournent une session).
- **Aveugles** (créent une attaque DoS).

### **Usurpation d'adresse MAC**

Utilisée lorsque les attaquants ont accès au réseau interne.

---

## **Vulnérabilités liées aux protocoles TCP et UDP**

### **TCP**

Le segment TCP et le datagramme UDP apparaissent immédiatement après l'en-tête IP.

- **TCP** : Fournit une livraison fiable, un contrôle de flux et une communication dynamique.
    - La **communication avec état** se fait lors de la prise de contact à trois voies (TCP Handshake).
    - Les acteurs malveillants peuvent utiliser plusieurs attaques liées à TCP :
        - **Analyse de port TCP**
        - **Attaque SYN par inondation**
        - **Attaque de réinitialisation TCP**
        - **Attaque par détournement de session TCP**

### **UDP**

Le segment UDP est beaucoup plus petit que le segment TCP, ce qui le rend adapté aux transactions simples, comme celles effectuées par :

- **DNS**, **DHCP**, **SNMP**, etc.

Les acteurs de menace peuvent utiliser des **attacks UDP inondation** en balayant tous les ports UDP d'un serveur, à la recherche de ports fermés. Cela peut entraîner un déni de service (DoS).
