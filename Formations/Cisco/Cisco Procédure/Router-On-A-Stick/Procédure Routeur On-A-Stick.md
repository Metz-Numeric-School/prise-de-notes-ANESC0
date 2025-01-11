

# Qu'est-ce qu'un routeur on-a-stick?

Un **router-on-a-stick** est une configuration réseau où un **routeur** utilise une seule interface physique (port) pour gérer le trafic entre plusieurs VLANs. Cela fonctionne grâce au **trunking**, qui permet à l'interface d'accepter des balises (tags) VLAN et de router le trafic entre ces VLANs. C'est une solution économique pour segmenter un réseau avec un équipement limité.


# 1ère étape

## Réaliser un plan des adresses pour chaque service afin de définir les VLAN


| **VLAN ID** | **Nom**              | **Plage IP**    | **Utilisation**        |
| ----------- | -------------------- | --------------- | ---------------------- |
| VLAN 10     | Administratif        | 192.168.10.0/24 | Administration         |
| VLAN 20     | Commercial           | 192.168.20.0/24 | Département Commercial |
| VLAN 30     | Technique            | 192.168.30.0/24 | Département Technique  |
| VLAN 40     | Imprimantes_Serveurs | 192.168.40.0/24 | Serveur et Imprimantes |

dans mon exemple j'ai pris que 4 service mais il peut en avoir beaucoup +. J'ai pris également des plages réseaux assez larges de  256 blocs mais je pouvais en utiliser beaucoup moins.

Après avoir réalisé le plan on peut dresser le plan sur Cisco comme ci-dessous

![[Pasted image 20241231002225.png]]

-----

## 2e étape Changer les ports de chaque switch

Il faut maintenant modifier les ports de tous nos switch.