
# Empoisonnement ARP

Dans la figure, l'acteur de menace envoie deux réponses ARP usurpées gratuitement en utilisant sa propre adresse MAC pour les adresses IP de destination indiquées. PC-A met à jour son cache ARP avec sa passerelle par défaut qui pointe maintenant vers l'adresse MAC hôte de l'acteur de menace. R1 met également à jour son cache ARP avec l'adresse IP de PC-A pointant vers l'adresse MAC de l'acteur de menace.

L'hôte de l'acteur de menace exécute une attaque d'empoisonnement ARP. L'attaque d'empoisonnement ARP peut être passive ou active. L'empoisonnement passif par ARP est l'endroit où les acteurs de menace volent des informations confidentielles. L'empoisonnement ARP actif est l'endroit où les acteurs de menace modifient les données en transit ou injectent des données malveillantes.



![[Pasted image 20250121100008.png]]



# Attaques DNS

Le protocole DNS (Service de nom de domaine) définit un service automatisé qui fait correspondre les noms de ressources, tels que www.cisco.com, avec l'adresse réseau numérique requise, telle que l'adresse IPv4 ou IPv6. Il inclut le format des requêtes, des réponses et des données, et utilise les enregistrements de ressource (RR) pour identifier le type de réponse DNS.

La sécurisation du protocole DNS est souvent négligée. Toutefois, celui-ci est indispensable à l'exploitation d'un réseau et doit être sécurisé en conséquence.

Les attaques DNS sont les suivantes:

- Attaques DNS résolveur ouvert
- Attaques furtives DNS
- Les attaques de ombrage de domaine DNS
- Attaques de Tunnellisation (tunneling) DNS

----

# Tunnelisation DNS

Les réseaux de zombies constituent désormais une méthode d'attaque privilégiée par les cyberpirates. Le plus souvent, les réseaux de zombies sont utilisés pour propager des malwares ou pour lancer des attaques DDoS et de phishing.

1. Les données se divisent en plusieurs blocs encodés.
2. Chaque bloc est placé sous une étiquette de nom de domaine d'un niveau inférieur à celui de la requête DNS.
3. Le protocole DNS local ou en réseau n'apportant aucune réponse à la requête, celle-ci est envoyée aux serveurs DNS récursifs du fournisseur d'accès à Internet.
4. Le service DNS récursif transmet la requête au serveur de noms de référence du hacker.
5. Le processus est répété jusqu'à ce que toutes les requêtes contenant les blocs soient envoyées.
6. Lorsque le serveur de noms de référence du hacker reçoit les requêtes DNS des appareils infectés, il envoie une réponse pour chaque requête DNS contenant les commandes encapsulées encodées.
7. Le malware de l'hôte compromis recombine les blocs et exécute les commandes dissimulées à l'intérieur.


----

# DHCP

Les serveurs DHCP fournissent dynamiquement des informations de configuration IP aux clients. La figure montre la séquence typique d'un échange de messages DHCP entre le client et le serveur.

![[Pasted image 20250121104715.png]]

---


## Attaques DHCP

**Attaque d'Usurpation DHCP**

Une attaque par mystification via le service DHCP se produit lorsqu'un serveur DHCP non autorisé (rogue) se connecte au réseau et fournit des paramètres de configuration IP incorrects aux clients légitimes. Un serveur non autorisé peut fournir de nombreuses informations erronées:

- **Passerelle par défaut incorrecte -** L'acteur de la menace fournit une passerelle non valide, ou l'adresse IP de son hôte pour créer une attaque MiTM. Cette approche peut passer totalement inaperçue, car l'intrus intercepte le flux de données via le réseau.
- **Mauvais serveur DNS -** L'acteur de la menace fournit une adresse de serveur DNS incorrecte qui fait pointer l'utilisateur vers un site web malveillant.
- **Mauvaise adresse IP -** L'acteur de la menace fournit une adresse IP non valide, une adresse IP de passerelle par défaut non valide, ou les deux. L'acteur de menace crée ensuite une attaque DoS sur le client DHCP.
![[Pasted image 20250121104804.png]]