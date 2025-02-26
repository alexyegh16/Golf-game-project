from settings import *
from sprites import Sprite


# Classe pour la création des boutons
class Button:
    def __init__(self, x=0, y=0, text="", width=200, height=50, elev=6):
        self.font = pygame.font.SysFont('impact', 24)
        self.text = self.font.render(text, True, "#ffffff")
        self.text_rect = self.text.get_rect()

        self.bottom_rect = pygame.Rect((x+elev, y+elev), (width, height))
        self.top_rect = pygame.Rect((x, y), (width, height))
        self.text_rect.center = self.top_rect.center

        self.hover = False
        self.pressed = False
        self.clicked = False

    def update(self):
        # Le bouton n'est pas appuié
        self.clicked = False
        # Vérification de la position de la souris sur le bouton
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.hover = True
            # Condition si la souris est enfoncée pendant qu'on est sur le bouton
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                # Condition si la souris n'est pas enfoncée pendant qu'on est sur le bouton
                if self.pressed is True:
                    self.pressed = False
                    self.clicked = True
                    
        else:
            self.pressed = False
            self.hover = False

    def draw(self, display):
        top_rect_color = "#317bcf" if self.hover else "#3194cf"
        if not self.pressed:
            #Si on n'apppuie pas sur la souris, on dessine le boutons dans sa position originale
            pygame.draw.rect(display, "#1a232e", self.bottom_rect)
            pygame.draw.rect(display, top_rect_color, self.top_rect)
            self.text_rect.center = self.top_rect.center
        else:
            #Si on appuie sur la souris, on change la position du dessin des boutons 
            pygame.draw.rect(display, top_rect_color, self.bottom_rect)
            self.text_rect.center = self.bottom_rect.center
        display.blit(self.text, self.text_rect)


class Menu:
    def __init__(self,tmx_map,switch_stage):
        
        self.display_surface = pygame.display.get_surface()
        self.switch_stage = switch_stage
        #Groupe
        self.all_sprites = pygame.sprite.Group()
        #Création des boutons 
        self.button_jouer = Button(480, 150, "JOUER")
        self.button_quitter = Button(480, 300, "QUITTER")
        self.button_credits = Button(480, 225, "CRÉDITS")
    
       
         
        self.setup(tmx_map)

    def setup(self, tmx_map):
        #tuiles
        for layer in ['Bg','Terrain','objets']:
            for x,y, surf, in tmx_map.get_layer_by_name(layer).tiles():
                Sprite((x*TAILLE_TILE,y*TAILLE_TILE),surf,self.all_sprites)

                    


    def run(self,dt):
            # Changement d'interface si on appuie sur le bouton jouer (Affichage du premier niveau)
            if self.button_jouer.clicked:
                self.switch_stage('level',0)
            # Changement d'interface si on appuie sur le bouton crédits (Affichage des crédits)
            if self.button_credits.clicked:
                self.display_surface.fill('black')   
                self.switch_stage('fenetre',3)
                
            # Condition si on veut fermer le jeu à l'aide du bouton  quitter
            if self.button_quitter.clicked:
                sys.exit() 


            self.all_sprites.draw(self.display_surface)
            self.button_jouer.draw(self.display_surface)
            self.button_quitter.draw(self.display_surface)
            self.button_credits.draw(self.display_surface)

            self.all_sprites.update()
            self.button_jouer.update()
            self.button_credits.update()
            self.button_quitter.update()
                
        
        


        
       