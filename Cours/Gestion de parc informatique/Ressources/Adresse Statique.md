###### Pour configurer une adresse en statique sur VMWorkstation

IP ->   /etc/network/interfaces

iface cns 33 inet static
adress 10.10.10.100
netmask 255.255.255.0
gateway 10.10.10.2
dns-nameservers 8.8.8.8 4.4.4.4

DNS ->    /etc/resolv.conf
nameserver 10.10.10.2