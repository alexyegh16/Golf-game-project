from settings import *
from sprites import Sprite
from menu import Button


class Fenetre:
    def __init__(self,tmx_map,switch_stage):
        
        self.display_surface = pygame.display.get_surface()
        self.switch_stage = switch_stage
        # groupe
        self.all_sprites = pygame.sprite.Group()
        # Création du bouton
        self.button_retour = Button(475, 500,"RETOUR AU MENU")
        
       
         
        self.setup(tmx_map)

    def setup(self, tmx_map):
        #tuiles
        for layer in ['BG']:
            for x,y, surf, in tmx_map.get_layer_by_name(layer).tiles():
                Sprite((x*TAILLE_TILE,y*TAILLE_TILE),surf,self.all_sprites)

                    


    def run(self,dt):
            self.display_surface.fill('black')
            #Changement de l'interface si on appuie sur le bouton aide (Retour au menu principal)   
            if self.button_retour.clicked:
                self.switch_stage('menu',5)
                 
            self.all_sprites.update()
            self.all_sprites.draw(self.display_surface)
            self.button_retour.draw(self.display_surface)
            self.button_retour.update()

class FenetreNiveaux:
    def __init__(self,tmx_map,switch_stage):
        
        self.display_surface = pygame.display.get_surface()
        self.switch_stage = switch_stage
        #Groupe
        self.all_sprites = pygame.sprite.Group()
        #Création des boutons
        self.button_retour = Button(470, 250,"RETOUR AU MENU")
        self.button_quitter = Button(470, 375,"QUITTER")
        
        self.setup(tmx_map)

    def setup(self, tmx_map):
        #tuiles
        for layer in ['BG']:
            for x,y, surf, in tmx_map.get_layer_by_name(layer).tiles():
                Sprite((x*TAILLE_TILE,y*TAILLE_TILE),surf,self.all_sprites)

                    


    def run(self,dt):
            
            self.display_surface.fill('black')
            #Changement de l'interface si on appuie sur le bouton aide (affichage d'un menu)
            if self.button_retour.clicked:
                self.switch_stage('menu',5)
            #Condition si on veut fermer le jeu à l'aide du bouton  quitter
            if self.button_quitter.clicked:
                  sys.exit() 
            
            self.all_sprites.update()
            self.all_sprites.draw(self.display_surface)
            self.button_retour.draw(self.display_surface)
            self.button_quitter.draw(self.display_surface)
            self.button_retour.update()
            self.button_quitter.update()
