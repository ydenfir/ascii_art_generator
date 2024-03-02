import re
import os
from googlesearch import search
import requests
from bs4 import BeautifulSoup





# Creer un dossier pour les images
if not os.path.exists("pokemons"):
    os.mkdir("pokemons")

# Liste des noms des 151 premiers Pokemon en français
pokemons = ["bulbizarre", "herbizarre", "florizarre", "salameche", "reptincel", "dracaufeu", "carapuce", "carabaffe", "tortank", "chenipan", "chrysacier", "papilusion", "aspicot", "coconfort", "dardargnan", "roucool", "roucoups", "roucarnage", "rattata", "rattatac", "piafabec", "rapasdepic", "abo", "arbok", "pikachu", "raichu", "sabelette", "sablaireau", "nidoran", "nidorina", "nidoqueen", "nidoran", "nidorino", "nidoking", "melofee", "melodelfe", "goupix", "feunard", "rondoudou", "grodoudou", "nosferapti", "nosferalto", "mystherbe", "ortide", "rafflesia", "paras", "parasect", "mimitoss", "aeromite", "taupiqueur", "triopikeur", "miaouss", "persian", "psykokwak", "akwakwak", "ferosinge", "colossinge", "caninos", "arcanin", "ptitard", "tetarte", "tartard", "abra", "kadabra", "alakazam", "machoc", "machopeur", "mackogneur", "chetiflor", "bebiflor", "empiflor", "tentacool", "tentacruel", "racaillou", "gravalanch", "grolem", "ponyta", "galopa", "ramoloss", "flagadoss", "magneti", "magneton", "canarticho", "doduo", "dodrio", "otaria", "lamantine", "tadmorv", "grotadmorv", "kokiyas", "crustabri", "fantominus", "spectrum", "ectoplasma", "onix", "soporifik", "hypnomade", "krabby", "krabboss", "voltorbe", "electrode", "noeunoeuf", "noadkoko", "osselait", "ossatueur", "kicklee", "tygnon", "excelangue", "smogo", "smogogo", "rhinocorne", "rhinoferos", "leveinard", "saquedeneu", "kangourex", "hypotrempe", "hypocean", "poissirene", "poissoroy", "stari", "staross", "m. mime", "insecateur", "lippoutou", "elektek", "magmar", "scarabrute", "tauros", "magicarpe", "leviator", "lokhlass", "metamorph", "evoli", "aquali", "voltali", "pyroli", "porygon", "amonita", "amonistar", "kabuto", "kabutops", "ptera", "ronflex", "artikodin", "electhor", "sulfura", "minidraco", "draco", "dracolosse", "mewtwo", "mew"]



# Fonction pour télécharger une image
def telecharger_image(nom_pokemon):
    # Définir l'URL de recherche Google Images
    query = "pokemon {}".format(nom_pokemon)
    search_url = "https://www.google.com/search?q={}&tbm=isch".format(query)

    # Envoyer une requête à Google Images et récupérer le HTML
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trouver toutes les balises d'images
    images = soup.find_all('img', {'src': re.compile(r'^https://')})

    # Extraire l'URL de la première image
    if images:
        img_url = images[0].get('src')

        # Télécharger l'image
        response = requests.get(img_url)

        # Enregistrer l'image
        with open(os.path.join("pokemons", "{}.png".format(nom_pokemon)), "wb") as f:
            f.write(response.content)
        print("Image téléchargée pour {}".format(nom_pokemon))
    else:
        print("Aucune image trouvée pour {}".format(nom_pokemon))

# Télécharger les images pour chaque pokémon
for pokemon in pokemons:
    telecharger_image(pokemon)

print("Téléchargement terminé !")
