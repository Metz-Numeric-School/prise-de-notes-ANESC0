

Lorsque vous utilisez un **switch Layer 3**, il n'y a plus besoin de sous-interfaces comme dans une configuration de **routeur on a stick**.

# Explication détaillée :

- Sur un **routeur** (avec la configuration "router on a stick"), chaque **sous-interface** est utilisée pour effectuer le routage entre les VLANs, chaque sous-interface étant liée à un VLAN spécifique.
    
- En revanche, sur un **switch Layer 3**, chaque VLAN est associé à une **interface VLAN** (souvent appelée "SVI" pour **Switched Virtual Interface**). Ces interfaces VLAN sur le switch sont équivalentes aux sous-interfaces sur le routeur, mais la différence est que tout le **routage inter-VLAN** se fait directement au niveau du switch, sans avoir besoin d'un routeur supplémentaire.
    

Donc, dans un switch Layer 3, vous créez simplement une **interface VLAN** pour chaque VLAN, et vous attribuez une **adresse IP** à chaque interface VLAN. Le routage inter-VLAN est ensuite effectué de manière native sur le switch, sans sous-interfaces comme dans la configuration "router on a stick".

## Exemple :

Sur un switch Layer 3 :

- Vous avez des **interfaces VLAN 10, VLAN 20**, etc., et vous leur attribuez des adresses IP. Ces interfaces seront utilisées pour le routage entre les VLANs.

## Résumé :

- **Routeur** : Sous-interfaces pour chaque VLAN.
- **Switch Layer 3** : Interfaces VLAN pour chaque VLAN, avec une adresse IP assignée pour le routage inter-VLAN. Pas besoin de sous-interfaces comme sur un routeur.