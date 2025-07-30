# Soundcloud Sync

> **Synchroniser vos playlists, musiques et artistes Soundcloud sur votre PC**

![screen](ressources/screen1.png)


## Fonctionnement et options:

**Téléchargez et synchronisez des playlistes, albums, musiques, artistes depuis Soundcloud sur votre PC.**

Les métadonnées tels que l'artiste, le genre, et l'artwork sont conservés.
En synchronisant un élément, les titres manquants seront téléchargés.
Si le paramètre n'est pas désactivé, les titres téléchargés qui ne sont plus dans la playlist/album soundcloud seront supprimés.

Des paramètres sont disponibles pour par exemple convertir les fichiers en MP3,
ou pour supprimer les fichiers locaux lorsqu'un élément est supprimé.


## Installation:

Vous avez besoin de `Python 3.9` minimum et de `ffmpeg`.

Pour installer `ffmpeg` sur Windows, utilisez cette commande: `winget ffmpeg`
Sur Linux, utilisez votre gestionnaire de paquet.

__Un éxécutable .exe est disponible pour Windows: https://github.com/Robin-mlh/Soundcloud-Sync/releases__

__Sinon:__

Pour installer les dépendances, entrez cette commande dans le répertoire du projet.

    python -m pip install -r requirements.txt

Pour lancer le programme:

    python "soundcloud sync.py"


## Paramètres:

![screen](ressources/screen2.png)

#### Token Soundcloud
Vous devez entrer votre Token d'authentification Soundcloud pour pouvoir télécharger les musiques:
Vous trouverez votre token dans les cookies Soundcloud
(Connectez-vous à soundcloud.com > appuyez sur F12 > onglet Application > cookies > Value de `oauth_token`).


#### Répertoire de synchronisation
Vous devez spécifier le chemin du répertoire dans lequel seront téléchargées les musiques.
Choisissez un dossier vide, par exemple `Musiques/Soundcloud/`
Chaque répertoir est indépendant et contient un fichier JSON avec tous les liens soundcloud ajoutés.


## Notes:

Si l'installation des dépendances du requirements.txt échoue avec une version récente de Python, essayez d'utiliser `Python 3.9`.

Il n'est pas possible de télécharger deux musiques avec le même titre dans la même playlist.

Désactiver les services de synchronisation de fichier comme OneDrive et ne pas convertir les fichiers au format MP3
sont des moyens d'accélérer le téléchargement des contenus.

Sur Windows, certains bugs liés au format des noms de fichiers peuvent affecter l'affichage du status de synchronisation d'un élément.
Voir les caractères interdits dans les noms de fichier Windows.
