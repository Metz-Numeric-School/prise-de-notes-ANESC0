# Domaines de menace

## Définition
Un **domaine de menace** est une zone de contrôle, d'autorité ou de protection que les hackers peuvent exploiter pour accéder à un système. Les cybermenaces incluent :
- Attaques et erreurs logicielles
- Sabotage
- Erreur humaine
- Vol
- Pannes matérielles
- Interruption des services publics
- Catastrophes naturelles

## Types de menaces
### Menaces internes
- Employés actuels ou anciens
- Partenaires contractuels

### Menaces externes
- Attaquants amateurs ou qualifiés exploitant des vulnérabilités ou utilisant des techniques d'ingénierie sociale.

### Autres domaines de vulnérabilité
- **Utilisateurs** : Politiques de sécurité mal appliquées, vol de données, téléchargements non autorisés, etc.
- **Infrastructures** : Équipements, réseaux locaux, clouds privés et publics.

## Menaces complexes
- **APT** : Attaques persistantes avancées
- **Portes dérobées** : Accès non autorisé persistant, même après correction d'une vulnérabilité.
- **Rootkits** : Modification des ressources système, rendant la détection difficile.

## Dark Web et IOC
- **Dark Web** : Contenu non indexé nécessitant des accès spécifiques.
- **IOC** : Indicateurs de compromission comme les signatures de malwares.
- **AIS** : Échange d'indicateurs de menaces via STIX et TAXII.

---

# Déception et Ingénierie sociale

## Tactiques courantes
- **Prétextage** : Mensonges pour obtenir des données sensibles.
- **Quid pro quo** : Demandes d'informations en échange de quelque chose.
- **Usurpation d'identité** : Utilisation d'identités volées pour obtenir des avantages.

## Techniques utilisées
- Intimidation ou autorité
- Consensus social ou rareté
- Urgence
- Familiarité et confiance
- Surf visuel (observation directe ou via des outils comme des caméras)
- Recherche dans les poubelles
- Greffage ou talonnage pour accéder à des zones sécurisées

## Prévention
- Sensibilisation et formation des employés sur les tactiques d'ingénierie sociale.

---

# Cyberattaques

## Types de logiciels malveillants
- **Virus** : Se réplique en insérant du code dans d'autres fichiers.
- **Ver** : Exploite les vulnérabilités réseau pour se propager.
- **Cheval de Troie** : Dissimule ses intentions malveillantes.
- **Bombe logique** : Code activé par un déclencheur.
- **Rançongiciels** : Bloque l'accès aux données jusqu'à paiement.

## Attaques réseau
- **DoS** : Saturation d'un serveur avec du trafic malveillant.
- **DDoS** : DoS provenant de multiples sources.
- **DNS** : Usurpation et piratage DNS.

## Techniques avancées
- Attaques de couche 2 : Usurpation MAC, ARP, IP.
- Attaques jour zéro : Exploitation de vulnérabilités inconnues.
- Keylogging : Enregistrement des frappes clavier.

## Défenses
- Utiliser des pare-feu et des correctifs.
- Bloquer les paquets ICMP externes.
- Répartir la charge sur les systèmes serveurs.

---

# Attaques sur les terminaux mobiles et sans fil

## Menaces spécifiques
- **Grayware** : Applications indésirables.
- **SMiShing** : Messages texte contenant des liens malveillants.
- **Points d'accès malveillants** : Faux points d'accès sans fil.
- **Brouillage** : Perturbation des transmissions sans fil.
- **Bluejacking/Bluesnarfing** : Exploitation des connexions Bluetooth.

## Défenses
- Modifier les configurations par défaut.
- Détecter les points d'accès non autorisés.
- Utiliser des VPN pour l'accès WLAN.

---

# Attaques sur les applications et autres

## Types d'attaques
- **Injection de code** : XML, SQL, DLL, LDAP.
- **Dépassement de tampon** : Écriture au-delà des limites d'un tampon.
- **XSS** : Vulnérabilités dans les applications web.

## Techniques de défense
- Valider toutes les entrées externes.
- Maintenir les logiciels à jour.
- Utiliser des outils antivirus et analyser les pièces jointes.

## Phishing et variantes
- **Phishing** : E-mails frauduleux pour voler des informations.
- **Spear phishing** : E-mails personnalisés visant une cible spécifique.
- **Vishing** : Arnaques téléphoniques.
- **Pharming** : Redirection vers de faux sites web.

---

# Conclusion

Les organisations doivent :
1. Former les employés aux menaces.
2. Utiliser des outils de détection et de prévention.
3. Maintenir une hygiène numérique en mettant à jour logiciels et systèmes.
