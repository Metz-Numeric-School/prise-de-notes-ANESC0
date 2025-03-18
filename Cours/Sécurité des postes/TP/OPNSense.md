
configuration de la VM 

2 interfaces : 
- Une interface LAN 
- Une interface WAN ( VMNAT )

mettre 20 GB d'espace



# Dans PNET

taper les commandes 

````
cd /opt/unetlab/addons/qemu/opnsense-24.7/  
  
/opt/qemu/bin/qemu-img create -f qcow2 virtioa.qcow2 20G  
  
cd  

/opt/unetlab/wrappers/unl_wrapper -a fixpermissions

````







Ensuite on peut démarrer la VM

se logger en root en mode live qui n'enregistre pas ou on peut se logger en installeur pour sauvegarde ce qu'on fait

id : installer
mdp :  opnsense

clavier french (accent key)


installer en ZFS

mirro pour sauvegarder sur 2 disque différents




ensuite on peut désactiver le cd rom

Une fois redémarré

vérifier sir les interfaces ont les bonne ip si les interfaces sont inversé il faudra les modifier.



activer le dhcp sur opnsense et donner l'etendue



Utiliser une vm windows existante et la mettre sur le même vmNet que l'interfaces LAN
de opnsense

on se connectera a l'interface de opnsense sur cette VM

id root 
mdp opnsense

cliquer sur suivant au debut et modifier qlq petite trucs

modifier le server mtp dans "Assistant"

changer le mot de passe 

faire la mise a jour du parefeu

dans l'onglet systeme -> firmware -> mise a jour - > status
cliquer sur verifier les mise a jour

en bas de cette page on va cliquer sur mise a jour



renommer le certificat en .CRT


