
**Fiche de Révision : Adressage IP & DHCP**

---

**1. Numéro de réseau du LAN**

> **Réponse :** 192.168.10.0  
> **Explication :** L'adresse IP et le masque /24 indiquent que les trois premiers octets définissent le réseau.

**2. Numéro d'hôte de l'adresse IP**

> **Réponse :** 2  
> **Explication :** L'adresse IP est 10.10.10.2 avec un masque /24, donc le numéro d'hôte est le dernier octet (2).

**3. Nombre de bits dans une adresse IPv4**

> **Réponse :** 32  
> **Explication :** Une adresse IPv4 est composée de 4 octets (8 bits chacun), soit 32 bits.

**4. Fonction du masque de sous-réseau**

> **Réponse :** La partie de l'adresse IP qui identifie le réseau  
> **Explication :** Il permet de déterminer quelle partie de l'adresse IP appartient au réseau.

**5. Tous les périphériques ont-ils besoin d'une IP ?**

> **Réponse :** Vrai  
> **Explication :** Une adresse IP est indispensable pour la communication sur un réseau.

**6. Utilité du masque de sous-réseau**

> **Réponse :** À déterminer le sous-réseau auquel l'hôte appartient  
> **Explication :** Il permet de savoir si une adresse IP est sur le même réseau.

**7. Plages d'adresses privées**

> **Réponses :** 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16  
> **Explication :** Ces plages sont réservées aux réseaux internes.

**8. Raisons de création de sous-réseaux**

> **Réponses :** Simplifier la mise en œuvre des stratégies de sécurité, Améliorer les performances réseau  
> **Explication :** La segmentation réduit la congestion et facilite la sécurisation.

**9. Association d'adresses IP**

> **Réponses :**
> 
> - 169.254.1.5 -> Adresse link-local
> - 172.19.20.5 -> Une adresse privée
> - 127.0.0.1 -> Adresse de bouclage
> - 240.2.6.255 -> Adresse expérimentale

**10. Adresse 169.254.x.x attribuée ?**

> **Réponse :** Serveur DHCP inaccessible  
> **Explication :** L'APIPA assigne ces adresses quand le DHCP ne répond pas.

**11. Adoption d'IPv6**

> **Réponse :** L'IoT ajoute des millions de capteurs réseau qui ont besoin d'adresses IP.  
> **Explication :** IPv4 manque d'adresses pour répondre à la demande croissante.

**12. Forme compressée d'une adresse IPv6**

> **Réponse :** 2001:DB8:0:AB00::1234  
> **Explication :** Les groupes de zéros consécutifs sont remplacés par `::`.

**13. Coexistence IPv4/IPv6**

> **Réponses :**
> 
> - Double pile -> IPv4 et IPv6 coexistent sur le même réseau.
> - Tunnellisation -> IPv6 est encapsulé dans IPv4.
> - Translation -> Conversion entre IPv4 et IPv6.

**14. Adresse abrégée correcte IPv6**

> **Réponse :** 2001:db8:0:0:ab00::  
> **Explication :** On simplifie en supprimant les zéros inutiles.

**15. Nombre de bits dans une adresse IPv6**

> **Réponse :** 128  
> **Explication :** IPv6 utilise 16 octets, soit 128 bits.

**16. Messages de diffusion DHCP**

> **Réponses :** DHCPDISCOVER, DHCPREQUEST  
> **Explication :** Le client utilise la diffusion pour découvrir et demander une adresse.

**17. Adresse destination DHCPDISCOVER**

> **Réponse :** 255.255.255.255  
> **Explication :** C'est une diffusion pour contacter n'importe quel serveur DHCP.

**18. Vrai sur DHCP**

> **Réponse :** Lorsqu'un périphérique configuré pour le protocole DHCP démarre, le client diffuse un message DHCPDISCOVER pour identifier les serveurs DHCP disponibles sur le réseau.  
> **Explication :** Le client envoie un message pour trouver un serveur DHCP.

**19. Message pour accepter une adresse DHCP**

> **Réponse :** Diffusion DHCPREQUEST  
> **Explication :** Le client informe tous les serveurs qu'il accepte une offre.

**20. Périphériques avec adresses statiques**

> **Réponses :** Imprimantes, serveurs Web  
> **Explication :** Ces appareils doivent avoir des IP fixes pour fonctionner correctement.