# Coût total de possession

--------------------------------------------------------------------------

## A/ Infrastructure sur Site vs. Infrastructure Cloud

![[Pasted image 20241021144637.png]]

#### Infrastructure sur Site :

- **Déploiement local** : Installée sur les serveurs et ordinateurs de l'entreprise.
- **Dépenses d'investissement (CAPEX)** :
    - Coûts fixes : installations, matériel, licences, personnel.
    - **Mise à l’échelle** :
        - **Verticale** : coûteuse et prend du temps.
        - **Réduction** : les coûts fixes restent inchangés même si l'utilisation diminue.

#### Infrastructure Cloud :

- **Déploiement chez un fournisseur** (ex : AWS) :
    - Le fournisseur gère les installations, matériel, et maintenance.
- **Modèle basé sur l'utilisation (OPEX)** :
    - Vous ne payez que pour ce que vous utilisez.
    - **Mise à l’échelle** :
        - **Verticale ou réduction** : simple et flexible.
        - Facilité d'estimation des coûts.

#### Comparaison :

- **Sur site** :
    - Dépenses d’investissement (CAPEX), cycles longs, gestion complexe.
- **Cloud (AWS)** :
    - **Flexibilité**, **agilité**, et coûts variables basés sur la consommation.


--------------------------------------------------------------------------



## B/ Comparaison de Solution sur Site vs. Solution Cloud

![[Pasted image 20241021144829.png]]

#### Coût Total de Possession (TCO) :

- **Définition** : Estimation financière qui aide à déterminer les **coûts directs et indirects** associés à un produit ou un système.
- **Inclut** :
    - Coûts du service.
    - Coûts liés à la **propriété** et à la **gestion** du service.

#### Importance du TCO pour la Comparaison :

- Utile pour **comparer les coûts d'exploitation** d'une infrastructure :
    - **Sur site** ou en **colocation**.
    - **Cloud** (AWS par exemple) pour une charge de travail donnée.

#### Objectif de la Comparaison :

- **Budgétisation** : Aide à prévoir les coûts.
- **Étude de cas** : Permet de choisir la solution de **déploiement optimale**.


--------------------------------------------------------------------------



## C/

![[Pasted image 20241021145115.png]]

### Coûts associés à la gestion d'un centre de données sur site :

1. **Coûts de serveur** :
    
    - Matériel et logiciels.
    - Installations pour héberger l'équipement.
2. **Coûts de stockage** :
    
    - Matériel.
    - Administration.
    - Installations.
3. **Coûts du réseau** :
    
    - Matériel.
    - Administration.
    - Installations.
4. **Coûts de la main-d'œuvre informatique** :
    
    - Administration de l'infrastructure complète.

---

### Comparaison Cloud vs. Sur Site :

- **Cloud** :
    - Coûts souvent payés **d'avance** et faciles à **calculer**.
    - Tarification **transparente** (basée sur RAM, stockage, bande passante, etc.).
    - Prix fixé par unité de temps (heure, mois, etc.).
    - Offre plus de **certitude** sur la tarification.
- **Sur site** :
    - Coûts **directs** (électricité, surface au sol, stockage, opérations informatiques).
    - Coûts **indirects** (réseau, infrastructure de stockage).
    - Difficulté à évaluer les **coûts réels**.

---

### Autres coûts à considérer (sur site) :

- **Coûts logiciels** : Bases de données, gestion, niveaux intermédiaires.
- **Coûts d'installation** : Mises à niveau, maintenance, sécurité du bâtiment, taxes.
- **Main-d'œuvre informatique** : Sécurité et administration des applications.



--------------------------------------------------------------------------


## D/

![[Pasted image 20241021145330.png]]

### Composants de la solution **sur site** :

- **Machine virtuelle** :
    - 4 CPU.
    - 16 Go de RAM.
    - Système d'exploitation Linux.
- Utilisation moyenne de **100%** (optimisation par la RAM).
- **Coût total sur 3 ans** : **167 422 USD**.

---

### Composants de la solution **AWS Cloud** :

- **Instance m4.xlarge** :
    - 4 CPU.
    - 16 Go de RAM.
    - **Instance réservée** avec frais initiaux partiels sur **3 ans**.
- **Coût total sur 3 ans** : **7 509 USD**.

---

### Économie réalisée avec AWS :

- **Économies totales** sur 3 ans : **159 913 USD** (96% d'économie par rapport à la solution sur site).

---

### Raisons de la différence de coûts :

- **Solution sur site** :
    
    - Nécessite une **planification préalable** de la capacité.
    - Coûts fixes continus, même si la capacité n'est pas utilisée.
- **Solution AWS** :
    
    - Flexible : la capacité peut être **augmentée ou réduite** en fonction des besoins réels.
    - Moins de frais généraux, car vous ne payez que pour ce que vous utilisez.

---

### Conclusion :

Ce comparatif montre les **économies significatives** qu'une entreprise peut réaliser en adoptant une **infrastructure cloud AWS** plutôt qu'une solution sur site, en particulier grâce à la flexibilité et aux coûts basés sur la consommation.


--------------------------------------------------------------------------


## E/ *Calculateur de prix AWS* :

![[Pasted image 20241021145629.png]]

- Outil pour **estimer une facture mensuelle** AWS.
- Permet d'**explorer les services** AWS et de créer une **estimation de coût** adaptée à vos besoins.

---

### *Utilisations principales* :

- **Modéliser vos solutions** avant leur développement.
- Explorer les **niveaux de prix** et les **calculs** qui composent l'estimation.
- Trouver les **types d'instances** disponibles et les **conditions contractuelles**.

---

### *Avantages* :

- Prendre des **décisions éclairées** sur l'utilisation d'AWS.
- **Planifier les coûts** et l'utilisation d'AWS.
- **Simuler les prix** pour un ensemble d'instances et de services.

---

### *Actions possibles* :

- **Estimer les coûts mensuels** des services AWS.
- **Identifier des opportunités** de réduction des coûts.
- **Modéliser vos solutions** avant de les concevoir.
- **Explorer les prix** et les calculs associés.
- **Déterminer les types d'instances** et les **clauses contractuelles** adaptées.

--------------------------------------------------------------------------


## F/
![[Pasted image 20241021145833.png]]

### **Estimation avec le Calculateur de prix AWS** :

#### **Catégories d'estimation** :

1. **Total pour les 12 premiers mois** :
    
    - Estimation totale pour les 12 premiers mois de votre configuration AWS.
    - Inclut les coûts initiaux et mensuels combinés.
2. **Total initial** :
    
    - Montant à payer **à l'avance** pour configurer votre pile AWS.
3. **Total mensuel** :
    
    - Estimation des **dépenses mensuelles** une fois la pile AWS en fonctionnement.

#### **Comparaison des configurations** :

- Possibilité de **comparer différents groupes** pour évaluer différentes configurations AWS.
- Estimez les coûts pour chaque service au sein d'un groupe.

---

### **Exemple d'estimation** :

- **Total pour les 12 mois** : 886,92 USD.
- **Total initial** : 0 USD.
- **Coût mensuel** : 73,91 USD.



--------------------------------------------------------------------------


## G/ **Avantages Tangibles du Cloud** :

![[Pasted image 20241021150028.png]]
 En résumé : 
- **Réduction des coûts** sur :
    
    - Calcul, stockage, réseau, sécurité
    - Matériel et logiciels
    - Coûts d'exploitation, sauvegarde, reprise après sinistre
    - Personnel d'opération
- **TCO (Coût Total de Possession)** :
    
    - Analyse des **dépenses après adoption du cloud** par rapport à l'infrastructure sur site.
    - **Comparaison entre l'infrastructure sur site et cloud** pour estimer les coûts.

---

### *Analyse du ROI (Retour sur Investissement)* :

1. **Avantages Tangibles** :
    
    - Réductions visibles et directes des coûts.
    - Amélioration de l'efficacité.
2. **Avantages Intangibles** :
    
    - **Réutilisation des services** et applications dans le cloud.
    - **Productivité accrue** des développeurs.
    - **Satisfaction client** améliorée.
    - **Processus métiers agiles** pour mieux répondre aux opportunités.
    - **Augmentation de la portée mondiale**.
