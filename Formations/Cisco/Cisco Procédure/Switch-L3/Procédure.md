
### **Objectif** : Configurer une topologie réseau avec plusieurs VLANs, 3 switchs, et le VTP, avec un switch Layer 3 pour le routage inter-VLAN.

---

### **Matériel requis** :

- **1 Switch Layer 3** (remplaçant le routeur)
- **2 Switchs Layer 2**
- **6 PC** (2 par switch pour représenter différents départements/services)
- **1 Serveur**
- **1 Imprimante**

---

### **Étapes détaillées**

---

#### **1. Configuration matérielle et câblage**

1. **Reliez les switchs entre eux** :
    - **Switch 1 (Switch Layer 3)** connecté à **Switch 2** via un câble.
    - **Switch 1 (Switch Layer 3)** connecté à **Switch 3** via un autre câble.
2. **Reliez les PC, le serveur et l’imprimante** aux ports des switchs :
    - **2 PC** sur **Switch 2** pour le VLAN Commercial.
    - **2 PC** sur **Switch 3** pour le VLAN Technique.
    - **1 Serveur** et **1 Imprimante** sur **Switch 1** pour le VLAN Imprimantes_Serveurs.

---

#### **2. Définition des VLANs et des adresses IP**

|**VLAN ID**|**Nom**|**Plage IP**|**Utilisation**||
|---|---|---|---|---|
|VLAN 10|Administratif|192.168.10.0/24|Administration||
|VLAN 20|Commercial|192.168.20.0/24|Département Commercial||
|VLAN 30|Technique|192.168.30.0/24|Département Technique||
|VLAN 40|Imprimantes_Serveurs|192.168.40.0/24|Serveur et Imprimantes||

---

#### **3. Configuration des trunks entre les switchs**

Sur chaque switch, configurez les ports de liaison entre les switchs en mode **trunk** pour permettre la propagation des VLANs via le protocole VTP.

##### **Exemple sur Switch 1 (Switch Layer 3, vers Switch 2 et Switch 3)**

```plaintext
Switch> enable
Switch# configure terminal
Switch(config)# interface gi0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)# exit

Switch(config)# interface gi0/2
Switch(config-if)# switchport mode trunk
Switch(config-if)# exit
```

Répétez pour **Switch 2** et **Switch 3** sur leurs ports respectifs.

---

#### **4. Configuration du VTP**

##### **Sur Switch 1 (Serveur VTP)**

1. Configurez le switch comme serveur VTP :
    
    ```plaintext
    Switch> enable
    Switch# configure terminal
    Switch(config)# vtp mode server
    Switch(config)# vtp domain EntrepriseVLAN
    Switch(config)# vtp password MonMotDePasse
    ```
    
2. Ajoutez les VLANs sur ce switch uniquement :
    
    ```plaintext
    Switch(config)# vlan 10
    Switch(config-vlan)# name Administratif
    Switch(config-vlan)# exit
    
    Switch(config)# vlan 20
    Switch(config-vlan)# name Commercial
    Switch(config-vlan)# exit
    
    Switch(config)# vlan 30
    Switch(config-vlan)# name Technique
    Switch(config-vlan)# exit
    
    Switch(config)# vlan 40
    Switch(config-vlan)# name Imprimantes_Serveurs
    Switch(config-vlan)# exit
    ```
    

##### **Sur Switch 2 et Switch 3 (Clients VTP)**

Configurez-les en mode **client** pour recevoir les VLANs propagés par le serveur :

```plaintext
Switch> enable
Switch# configure terminal
Switch(config)# vtp mode client
Switch(config)# vtp domain EntrepriseVLAN
Switch(config)# vtp password MonMotDePasse
```

---

#### **5. Configuration des ports en mode access**

##### **Sur Switch 1 (Switch Layer 3)**

Attribuez les ports à leurs VLANs respectifs :

```plaintext
! Port pour les PC ADMIN (VLAN 10)
Switch(config)# interface range fa0/1 - 18
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
Switch(config-if)# exit
```

##### **Sur Switch 2**

Attribuez les ports aux VLANs :

```plaintext
! Ports pour VLAN 20 (Commercial)
Switch(config)# interface range fa0/1 - 18
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 20
Switch(config-if)# exit

Switch(config)# interface fa0/19 - 24
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 40
Switch(config-if)# exit
```

##### **Sur Switch 3**

Même logique pour le VLAN Technique :

```plaintext
! Ports pour VLAN 30 (Technique)
Switch(config)# interface range fa0/1 - 18
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 30
Switch(config-if)# exit

OU Pour une seule machine

Switch(config)# interface fa0/2
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 30
Switch(config-if)# exit
```

---

#### **6. Configuration du Switch Layer 3 (Routage inter-VLANs)**

Ne pas oublier de ne pas désactiver les interfaces VLAN sur le switch Layer 3, car elles peuvent être inactives par défaut.

```plaintext
Switch(config)# interface vlan 10
Switch(config-if)# no shutdown

Switch(config)# interface vlan 20
Switch(config-if)# no shutdown

Switch(config)# interface vlan 30
Switch(config-if)# no shutdown

Switch(config)# interface vlan 40
Switch(config-if)# no shutdown
```

Ensuite, configurez des **adresses IP** sur chaque interface VLAN du switch Layer 3 pour activer le routage entre les VLANs :

```plaintext
Switch(config)# interface vlan 10
Switch(config-if)# ip address 192.168.10.254 255.255.255.0
Switch(config-if)# exit

Switch(config)# interface vlan 20
Switch(config-if)# ip address 192.168.20.254 255.255.255.0
Switch(config-if)# exit

Switch(config)# interface vlan 30
Switch(config-if)# ip address 192.168.30.254 255.255.255.0
Switch(config-if)# exit

Switch(config)# interface vlan 40
Switch(config-if)# ip address 192.168.40.254 255.255.255.0
Switch(config-if)# exit
```

Le switch Layer 3 va maintenant router le trafic entre les VLANs sans avoir besoin d'un routeur externe.

---

#### **7. Configuration du DHCP**

Le **DHCP** peut être configuré directement sur le **switch Layer 3** pour fournir des adresses IP aux hôtes dans chaque VLAN.

```plaintext
Switch(config)# ip dhcp pool VLAN10
Switch(config-dhcp)# network 192.168.10.0 255.255.255.0
Switch(config-dhcp)# default-router 192.168.10.254
Switch(config-dhcp)# exit

Switch(config)# ip dhcp pool VLAN20
Switch(config-dhcp)# network 192.168.20.0 255.255.255.0
Switch(config-dhcp)# default-router 192.168.20.254
Switch(config-dhcp)# exit

Switch(config)# ip dhcp pool VLAN30
Switch(config-dhcp)# network 192.168.30.0 255.255.255.0
Switch(config-dhcp)# default-router 192.168.30.254
Switch(config-dhcp)# exit

Switch(config)# ip dhcp pool VLAN40
Switch(config-dhcp)# network 192.168.40.0 255.255.255.0
Switch(config-dhcp)# default-router 192.168.40.254
Switch(config-dhcp)# exit
```

---

#### **8. Vérifications finales**

- Testez la propagation des VLANs sur les clients VTP avec :
    
    ```plaintext
    Switch# show vlan brief
    ```
    
- Testez la connectivité entre les VLANs avec des commandes **ping** entre PC.
    

---

Avec cette configuration, le switch **Layer 3** remplace le **routeur** pour effectuer le **routage inter-VLAN**, ce qui simplifie l'architecture et améliore les performances du réseau.