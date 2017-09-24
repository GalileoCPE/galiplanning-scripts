# Scripts pour la mise en place du site/planning

## Rôle des différents scripts

Une tâche cron lance le script shell `Planning` toutes tes heures, de 8 à 18h.

La recette `Dockerfile` est utilisée pour créer un container dédié à la conversion
des fichiers excel (voir section dédiée).

Le script `script.py` est présent dans le container (bien qu'il pourrait être
déplacé en dehors dans une prochaine révision), et remet en forme le fichier
converti.

Afin que l'utilisateur sous le nom duquel le serveur tourne puisse lancer
docker sans souci de sécurité, un binaire `setgid` est lancé à la place.
Il s'agit du code présent dans `docker-prestage.c`

## Note sur l'utilisation du site

Le site n'est pas vraiment exploitable sans les pages html et php présents dans [un autre dépot](https://github.com/GalileoCPE/galiplanning-www-data).

## Compilation/mise en place du container

Après avoir installé docker (`apt install docker.io` sous debian), lancer:

	docker build -t galianglais .

Puis lancer une fois le container afin de créer une instance nommée avec les paramètres qui vont bien:

	docker run --cap-drop=all -v /repertoire/fichiers/entree:/mnt --name container-anglais galianglais:latest

Ensuite, les fichiers seront placés dans le /repertoire/fichiers/entree avant de lancer:

	docker start -a container-anglais

note: le -a sert pour ne pas détacher l'invite de commande. Si il est omis, cela fonctionne aussi, mais de manière asynchrone (et silencieusement)

## Licence

Le code est libre, fourni sous Licence AGPLv3. La licence est disponible
(en anglais) dans le fichier `LICENSE`.
Les fichiers sont copyrightés (c) au nom de l'association Galiléo, et
des contributeurs individuels (voir les en-têtes des fichiers).
