
### **Adresses IPv4 de Monodiffusion, de Diffusion et de Multidiffusion**

#### **Transmission Monodiffusion (Unicast)**

- La transmission monodiffusion envoie un message d'un périphérique à un autre (communication un-à-un).
- L'adresse IP de destination est une adresse monodiffusion qui va vers un seul destinataire.
- L'adresse IP source est une adresse unicast, ce qui signifie que le paquet provient d'une seule source.
- Les adresses IPv4 unicast se situent dans la plage **1.1.1.1 à 223.255.255.255**.

#### **Transmission par Diffusion (Broadcast)**

- La transmission par diffusion envoie un message à tous les appareils d'un réseau (communication un-à-tous).
- L'adresse IP de destination a tous les bits à **1** dans la partie hôte, soit **32 bits à 1**.
- La diffusion peut être :
    - **Dirigée** : envoyée à tous les hôtes d'un réseau particulier.
    - **Limitée** : envoyée à **255.255.255.255**.
- **Remarque** : Par défaut, les routeurs ne transfèrent pas les paquets de diffusion.

#### **Transmission Multidiffusion (Multicast)**

- La multidiffusion permet à un hôte d'envoyer un paquet à un groupe d'hôtes désignés inscrits à un groupe de multidiffusion.
- L'adresse IP de destination est une adresse de multidiffusion.
- Plage des adresses de multidiffusion IPv4 : **224.0.0.0 à 239.255.255.255**.
- Lorsqu'un hôte IPv4 s'abonne à un groupe de multidiffusion, il traite les paquets envoyés à cette adresse, ainsi que ceux destinés à son adresse monodiffusion.

---

### **Types d'Adresses IPv4**

#### **Adresses Publiques**

- Acheminées globalement sur l'internet entre les routeurs FAI.
- Les adresses IPv4 publiques doivent être uniques.

#### **Adresses Privées**

- Utilisées dans les réseaux internes (intranet) et non routables globalement.
- Exemples :
    - **10.0.0.0/8**
    - **172.16.0.0/12**
    - **192.168.0.0/16**
- Traduction des adresses privées en publiques via **NAT** pour permettre l'accès à Internet.

#### **Adresses de Bouclage (Loopback)**

- Plage : **127.0.0.0/8** (généralement **127.0.0.1**).
- Utilisées pour envoyer du trafic vers soi-même (localhost).

#### **Adresses Link-Local (APIPA)**

- Plage : **169.254.0.0/16**.
- Utilisées pour l'auto-configuration en l'absence de serveur DHCP.

---

### **Classes d'Adresses IPv4 (RFC 790)**

- **Classe A** : **0.0.0.0/8 à 127.0.0.0/8**
    - Réseaux de grande envergure (16 millions d'adresses hôte).
- **Classe B** : **128.0.0.0/16 à 191.255.0.0/16**
    - Réseaux de taille moyenne (65 000 adresses hôte).
- **Classe C** : **192.0.0.0/24 à 223.255.255.0/24**
    - Petits réseaux (max 254 hôtes).
- **Classe D (Multicast)** : **224.0.0.0 à 239.0.0.0**.
- **Classe E (Expérimentale)** : **240.0.0.0 à 255.0.0.0**.

---

### **Segmentation du Réseau et Sous-Réseaux**

- L'ARP utilise des diffusions pour localiser des périphériques dans un réseau local.
- Le **DHCP** envoie des diffusions pour attribuer des adresses IPv4.
- La **segmentation** réduit la taille des domaines de diffusion en créant des sous-réseaux.
- La segmentation permet de réduire le trafic global, d'améliorer les performances et de renforcer la sécurité.
