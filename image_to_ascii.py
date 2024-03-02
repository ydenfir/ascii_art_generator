from PIL import Image
import os
import pywhatkit as kt

def convert_to_ascii(image_path, output_path):
    try:
        # Charger l'image
        image = Image.open(image_path)

        # Convertir l'image en ASCII art
        ascii_art = kt.image_to_ascii_art(image_path)

        # Enregistrer le résultat dans un fichier texte
        with open(output_path, 'w') as file:
            file.write(ascii_art)

        print(f"Conversion réussie pour {image_path}. ASCII art enregistré dans {output_path}")

    except Exception as e:
        print(f"Erreur lors de la conversion pour {image_path}: {str(e)}")

def batch_convert_to_ascii(input_folder, output_folder):
    # Créer le dossier de sortie s'il n'existe pas
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Parcourir toutes les images dans le dossier d'entrée
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")
            convert_to_ascii(input_path, output_path)
    
# Spécifiez le chemin vers le dossier contenant les images PNG
input_folder = r"C:\Users\yanis\Desktop\pokemons"

# Spécifiez le chemin vers le dossier de sortie pour les fichiers ASCII art
output_folder = r"C:\Users\yanis\Desktop\pokemons_ascii"

# Appeler la fonction de conversion en lot
batch_convert_to_ascii(input_folder, output_folder)
