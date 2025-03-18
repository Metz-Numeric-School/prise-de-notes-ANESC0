
**Packet Tracer - Configure Extended ACLs - Scenario 1**

**Addressing Table**

| Device | Interface | IP Address   | Subnet Mask     | Default Gateway |
| ------ | --------- | ------------ | --------------- | --------------- |
| R1     | G0/0      | 172.22.34.65 | 255.255.255.224 | N/A             |
| R1     | G0/1      | 172.22.34.97 | 255.255.255.240 | N/A             |
| R1     | G0/2      | 172.22.34.1  | 255.255.255.192 | N/A             |
| Server | NIC       | 172.22.34.62 | 255.255.255.192 | 172.22.34.1     |
| PC1    | NIC       | 172.22.34.66 | 255.255.255.224 | 172.22.34.65    |
| PC2    | NIC       | 172.22.34.98 | 255.255.255.240 | 172.22.34.97    |

---

**Objectives**

- **Part 1**: Configure, Apply and Verify an Extended Numbered ACL
- **Part 2**: Configure, Apply and Verify an Extended Named ACL

**Background / Scenario**

Two employees need access to services provided by the server:

- **PC1** only needs FTP access.
- **PC2** only needs web access.
- Both computers should be able to ping the server.
- PC1 and PC2 should not communicate with each other.

---

### **Part 1: Configure, Apply and Verify an Extended Numbered ACL**

#### **Step 1: Configure an ACL to permit FTP and ICMP from PC1 LAN**

1. Determine the first valid number for an extended ACL:
    
    ```
    R1(config)# access-list ?
    ```
    
    Extended ACL range: **100-199**
    
2. Configure ACL 100 to allow FTP and ICMP from PC1 LAN:

    ```
    R1(config)# access-list 100 permit tcp 172.22.34.64 0.0.0.31 host 172.22.34.62 eq ftp
    R1(config)# access-list 100 permit icmp 172.22.34.64 0.0.0.31 host 172.22.34.62
    ```

3. Verify the ACL:
    
    ```
    R1# show access-lists
    ```
    

#### **Step 2: Apply the ACL on the correct interface**

1. Apply ACL **100** inbound on **GigabitEthernet 0/0**:
    
    ```
    R1(config)# interface gigabitEthernet 0/0
    R1(config-if)# ip access-group 100 in
    ```
    

#### **Step 3: Verify ACL Implementation**

1. Test ping from **PC1 to Server** → **Should work**
2. Test FTP from **PC1 to Server** → **Should work**
3. Test ping from **PC1 to PC2** → **Should be blocked**

---

### **Part 2: Configure, Apply and Verify an Extended Named ACL**

#### **Step 1: Configure an ACL to permit HTTP access and ICMP from PC2 LAN**

1. Create a named extended ACL **HTTP_ONLY**:
    
    ```
    R1(config)# ip access-list extended HTTP_ONLY
    ```
    
2. Permit HTTP and ICMP traffic from PC2 LAN:
    
    ```
    R1(config-ext-nacl)# permit tcp 172.22.34.96 0.0.0.15 host 172.22.34.62 eq www
    R1(config-ext-nacl)# permit icmp 172.22.34.96 0.0.0.15 host 172.22.34.62
    ```
    
3. Verify the ACL:
    
    ```
    R1# show access-lists
    ```
    

#### **Step 2: Apply the ACL on the correct interface**

1. Apply ACL **HTTP_ONLY** inbound on **GigabitEthernet 0/1**:
    
    ```
    R1(config)# interface gigabitEthernet 0/1
    R1(config-if)# ip access-group HTTP_ONLY in
    ```
    

#### **Step 3: Verify ACL Implementation**

1. Test ping from **PC2 to Server** → **Should work**
2. Open a browser on **PC2** and access **[http://172.22.34.62](http://172.22.34.62/)** → **Should work**
3. Test FTP from **PC2 to Server** → **Should fail**

---

**Conclusion**

- PC1 has **FTP and ICMP** access to the server but cannot communicate with PC2.
- PC2 has **HTTP and ICMP** access to the server but cannot communicate with PC1.
- The ACLs successfully restrict traffic as per the given scenario.