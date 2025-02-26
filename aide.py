from settings import *
from os import walk
from os.path import join 

def import_image(*path, alpha = True, format = 'png'):
    full_path = join(*path) + f'.{format}'
    return pygame.image.load(full_path).convert_alpha() if alpha else pygame.image.load(full_path).convert()


def import_fichier(*path):
    frames = []
    for fichier_path, subfolders, nom_images in walk(join(*path)):
        for nom_image in sorted(nom_images, key= lambda name : int (name.split('.')[0])):
            full_path = join(fichier_path,nom_image)
            frames.append(pygame.image.load(full_path).convert_alpha())
    return frames

      

