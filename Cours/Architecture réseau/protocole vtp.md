
les informations entre les VLAN et les routeur sont trunké et ne peuvent pas circuler librement par accès


enable
 # configure terminal
 vtp mode client/serveur
vtp domain BRSC2


vtp password MNS




conf t
vlan10
name SALES
exit
vlan20
name R&D
vlan 30
name MGT
vlan 40
name IT
vlan 50
name PRINTERS
vlan 60
name SERVERS



## trunk :




**dans le switch 1,2,3:**

conf t
int G0/2
sw
switchport ?
switchport mode tr



