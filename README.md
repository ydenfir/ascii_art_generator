# pokemon_ascii_art_generator
Ce projet Python, "Pokemon ASCII Art Generator", vous permet de créer des œuvres d'art ASCII à partir de noms de pokémons en récupérant des images associées à ces noms et en les transformant en art ASCII.

## Fonctionnalités principales

- **Recherche d'Images :** Le générateur utilise des services en ligne pour récupérer des images correspondant aux mots spécifiés.
- **Conversion Automatique :** Transformez un mot en une représentation artistique en ASCII directement depuis une image.

## Comment ça marche :

- **Récupération des images des pokémons voulus** à l'aide du script get_pokemon_images.py
- **Conversion en ASCII :** Les images précédemment téléchargées sont ensuite converties en art ASCII à l'aide du script image_to_ascii.py

## Dépendances :

- Python 3.x
- Bibliothèques Python : PIL, pywhatkit, BeautifulSoup, googlesearch, os, re



________________________________________________________________________________________________________________________________________________________________________________________________________
Notez que ce projet prend pour exemple la génération d'œuvres d'art ASCII de pokémons mais il peut être étendu à d'autres univers en modifiant la liste des noms recherchés dans le fichier get_pokemon_images.py
N'oubliez pas de renommer les répertoires d'entrée et de sortie du script image_to_ascii.py
Par défaut, le répertoire dans lequel les images sont téléchargées est celui dans lequel le script get_pokemon_images.py a été lancé
