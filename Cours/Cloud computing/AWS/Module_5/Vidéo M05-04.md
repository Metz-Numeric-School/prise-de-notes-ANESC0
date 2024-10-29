
# Sécurité de VPC



## A /

![[Pasted image 20241029012302.png]]


Un **groupe de sécurité** agit comme un **pare-feu virtuel** pour votre instance et contrôle le **trafic entrant et sortant**. Les groupes de sécurité fonctionnent au niveau de l’**instance** et non au niveau du **sous-réseau**, permettant à chaque instance dans un sous-réseau de votre VPC d’être affectée à un ensemble différent de **groupes de sécurité**. De manière simplifiée, un groupe de sécurité constitue une méthode de **filtrage du trafic** vers vos instances.



## B/

![[Pasted image 20241029012405.png]]


![[Pasted image 20241029012425.png]]



## C/


![[Pasted image 20241029012451.png]]

Une **liste de contrôle d'accès réseau (ACL réseau)** est une couche de **sécurité optionnelle** pour un Amazon VPC, agissant comme un **pare-feu** pour gérer le **trafic entrant et sortant** de sous-réseaux. Pour renforcer la sécurité de votre VPC, vous pouvez configurer des **ACL réseau** avec des règles similaires à celles des **groupes de sécurité**. Chaque sous-réseau de votre VPC doit être associé à une ACL réseau. Si aucun sous-réseau n’est associé explicitement, il sera automatiquement lié à l'**ACL réseau par défaut**. Une ACL réseau peut être associée à plusieurs sous-réseaux, mais chaque sous-réseau ne peut être associé qu’à une seule **ACL réseau** à la fois, l’association précédente étant supprimée en cas de changement.


![[Pasted image 20241029012537.png]]



![[Pasted image 20241029012612.png]]



--------------------------------------------------------------------------




## D/

![[Pasted image 20241029012639.png]]



--------------------------------------------------------------------------






![[Pasted image 20241029012758.png]]

