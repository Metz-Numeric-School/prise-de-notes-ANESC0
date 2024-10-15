est un service de calcul **serverless** qui permet d'exécuter du code en réponse à des évaénements sans avoir à gérer de serveurs. Il est idéal pour les tâches ponctuelles ou événementielles et fonctionne sur la base d'un modèle de facturation **à l'utilisation** (pay-as-you-go).

1. **Sans gestion de serveurs** : AWS gère automatiquement l'infrastructure, de sorte que tu n'as pas besoin de provisionner ni de gérer des serveurs.
2. **Déclencheurs événementiels** : Lambda peut être déclenché par des événements provenant d’autres services AWS, comme des modifications dans un bucket **S3**, des messages dans une file d’attente **SQS**, ou des requêtes HTTP via **API Gateway**.
3. **Support multi-langage** : Lambda supporte plusieurs langages, notamment Python, Node.js, Java, Ruby, Go, et C#.
4. **Mise à l’échelle automatique** : Lambda s'adapte automatiquement à la charge de travail, en exécutant le nombre exact de fonctions nécessaires selon le volume d'événements.
5. **Facturation à la milliseconde** : Tu ne paies que pour le temps d’exécution de ton code, avec une facturation au milliseconde, ce qui en fait une solution économique pour les tâches de courte durée.