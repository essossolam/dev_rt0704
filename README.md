# dev_rt0704 Mise en place
## Configurations
#### MACHINE
###### OS: debian 
addresse IP utilisé: 172.17.0.1

###### Conteneur RabbitMQ: 
port forwadé "5672:5672", "15672:15672" 

###### Flask: 
config: host='0.0.0.0', port=5000

###### GITHUB: 
username: essossolam
password: rt0704@2020
reporisitory: dev_rt0704

###### Fichiers: 
Remplacer le chemin vers le fichier Dockerfile par celui de votre environement exact dans le fichier dev_rt0704/app/src/mydocker.py

## Exécution
#### Se logé dans le répertoire ~/dev_rt0704/app/src
1. Exécuté python3 server.py pour démarrer le server, en ayant déjà démarré le conteneur rabbitmq
2. Exécuté python3 setup.py pour crééer la file logs
3. Exécuté python3 client.py pour démarrer mettre à disposition le projet commanditaire (résoudre le problème des nqueens) 
4. Exécuté sudo python3 mydocker.py pour build un worker
5. Démarrer l'outils de supervision avec python3 superviseur.py
6. Pour la gestion de la panne mettre un timout assez élevé

PS: En raison d'un problème avec mes fonctions git, pour envoyer une tâche il faudrait que les workers soient pas fonctionnels, sinon il récuperons la tâche sans les paramètres. Ce qui posera un problème.