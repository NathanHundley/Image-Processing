#Open Pokedex folder, #Create Pokedex/new/ folder

import os
from PIL import Image

image_folder = './Pokedex/'
output_path = 'Pokedex/PNG_Images/'

def JPGtoPNGConverter(import_folder, output_folder):

    os.makedirs(output_folder, exist_ok=True)
    new_folder_name = output_folder.replace(import_folder, '')[:-1]

    for filename in os.listdir(import_folder):
        if filename == new_folder_name:
            continue
        else:
            clean_name = os.path.splitext(filename)[0]
            current_path_name = os.path.join(import_folder, filename)
            img = Image.open(current_path_name)
            name = clean_name + '.png'
            path_name = os.path.join(output_folder, name )
            img.save(path_name, "png")

JPGtoPNGConverter(image_folder, output_path)

