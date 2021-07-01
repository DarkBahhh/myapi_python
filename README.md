# Travaux Pratiques : My API Python on Docker

## Les applicatifs

Les applicatifs sont publiés sur un dépôt Github, dans les sous dossiers de ce dépôts :

- API Frontend : api-frontend
- API Backend : api-backend

L'API Frontend est un script écrit en python et utilisant le framework Flask. Elle présente 2 endpoints qui sont :

 - / (GET) : Cette uri est censé renvoyer une réponse HTTP au format JSON avec un code 200. Un call est fait sur l'API Backend qui renvoi une réponse au format JSON.

 - /traceback (GET) : Cette uri permet de générer une erreur mettant fin au processus en cours d'éxécution dans le container. Cela permet de vérifier, lors de la correction, que l'ID du processus est bien le 1 et que l'applicatif se recharge  automatiquement en cas d'arrêt inopiné.


 L'API Backend est sensiblement similaire à l'API frontend. Elle présente 2 endpoints qui sont :

 - / (GET) : Cette uri renvoi est censé renvoyé une réponse avec un code HTTP 200. Cette réponse est récupéré depuis le fichier configuré avec la variable d'environnement API_DATA_PATH.

 - /traceback (GET) : Cette uri permet de générer une erreur mettant fin au processus en cours d'éxécution dans le container. Cela permet de vérifier, lors de la correction, que l'ID du processus est bien le 1 et que l'applicatif se recharge  automatiquement en cas d'arrêt inopiné.

Chaque applicatif est codé en Python et nécessite la version 2.7 du langage. Ils utilisent les bibliothèques supplémentaires suivantes :

  - python-requests
  - python-flask

Chacunes des API peuvent être lancées via la commande `python api.py`. Voici un schéma du chemin d'une requête HTTP du navigateur vers les APIs.

Requête HTTP <--> API FRONTEND <--> API BACKEND

Pour vérifier le fonctionnement des applicatifs, voici les requêtes HTTP que vous pourrez effectuer et le résultat attendu :

Sur l'API frontend :
  - http://127.0.0.1:8000/ : Cette requête devrait retourner le résultat ``` {
  "return": {
    "body": "Je suis une r\u00e9ponse du backend"
  },
  "status": "[SUCESS]"
}```. L'API frontend fait une requête HTTP sur l'API backend qui retourne la réponse. Assurez vous que les deux containers puissent communiquer sur le même réseau bridge.
  - http://127.0.0.1:8000/traceback : Ne devrait retourner aucun résultat mais l'application devrait s'arrêter. Le but étant que le container exécutant l'application se relance automatiquement dans ce cas là

Le conteneur Frontend doit disposer de deux variables d'environnement contenant le nom d'hôte à utiliser pour communiquer avec l'autre conteneur, soit les variables `API_BACKEND_URL` et `API_BACKEND_PORT`. Ces variables d'environement sont utilisées par l'applicatif et doivent absolument être renseignées.

  Sur l'API backnd :
  - http://127.0.0.1:8001/ : Cette requête devrait retourner le résultat `{"body": "Je suis une r\u00e9ponse du backend"}`.
  - http://127.0.0.1:8001/traceback : Ne devrait retourner aucun résultat mais l'application devrait s'arrêter. Le but étant que le container exécutant l'application se relance automatiquement dans ce cas là.
