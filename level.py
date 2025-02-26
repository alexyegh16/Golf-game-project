from settings import *
from sprites import Sprite, AnimationSprite, MovingSprite
from menu import Button

class Level:
    def __init__(self, tmx_map,level_frames,switch_stage):
        self.display_surface = pygame.display.get_surface()
        self.popup_surf = pygame.Surface((LONGUEUR_FENETRE,LARGEUR_FENETRE))
        self.switch_stage = switch_stage
        self.button_aide = Button(1111, 25,"",TAILLE_TILE,TAILLE_TILE)
         

        # groupes
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.cle_sprite = pygame.sprite.Group()
        
        self.setup(tmx_map, level_frames)
    
    def setup(self, tmx_map,level_frames):

        #tuiles
        for layer in ['BG','BGO','terrain','level']:
             for x,y,surf in tmx_map.get_layer_by_name(layer).tiles():
                groups = [self.all_sprites]
                if layer == 'terrain':groups.append(self.collision_sprites)
                Sprite((x*TAILLE_TILE,y*TAILLE_TILE),surf,groups)
        
        #objets   
        for obj in tmx_map.get_layer_by_name('objets'):
            if obj.name in ('boite','fleche','boutonAide'):
                    Sprite( (obj.x, obj.y), obj.image,(self.all_sprites, self.collision_sprites))
            else:
                #frames
                frames = level_frames[obj.name] 
                #groupes
                groups = [self.all_sprites]
                    
                AnimationSprite((obj.x, obj.y),level_frames [obj.name],groups)

        #Objets en mouvement  
        for obj in tmx_map.get_layer_by_name('moving objets'):
             if obj.name == 'obstacle':
                pass
             else:
                frames = level_frames[obj.name]
                groups = (self.all_sprites, self.collision_sprites)
                if obj.width > obj.height :
                    move_dir = 'x' #Horizontal
                    start_pos = (obj.x,obj.y + obj.height /2)
                    end_pos = (obj.x+obj.width,obj.y + obj.height /2)
                else :
                    move_dir = 'y' # Verticale
                    start_pos = (obj.x + obj.width /2, obj.y )
                    end_pos = (obj.x + obj.width /2, obj.y + obj.height)
                speed = obj.properties['speed']
                

                if obj.name == 'scie':
                    if move_dir == 'x': # Horizontal
                        y = start_pos[1]- level_frames['scie_chain'].get_height() /2
                        left,right = int(start_pos[0]),int(end_pos[0])
                        for x in range(left,right,20):
                            Sprite((x,y), level_frames['scie_chain'],self.all_sprites)

                    else : # Verticale 
                        x = start_pos[0]- level_frames['scie_chain'].get_width() /2
                        top,bottom = int(start_pos[1]),int(end_pos[1])
                        for y in range(top,bottom,20):
                            Sprite((x,y), level_frames['scie_chain'],self.all_sprites)
                MovingSprite(frames,groups,start_pos,end_pos,move_dir,speed)            

       
    def run(self,dt):
        # Changement de l'interface si on appuie sur le bouton aide 
        if self.button_aide.clicked:
            self.display_surface.fill('black')
            self.switch_stage('fenetre',4)


        self.all_sprites.update(dt)
        self.display_surface.fill('black')    
        self.all_sprites.draw(self.display_surface)
        self.button_aide.update()
          
        
        
    
        