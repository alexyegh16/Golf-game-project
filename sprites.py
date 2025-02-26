
from pygame import Surface
from settings import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf = pygame.Surface((TAILLE_TILE,TAILLE_TILE)) ,groups= None):
        super().__init__(groups)
        self.image  = surf
        self.rect = self.image.get_rect(topleft = pos)
        self.old_rect = self.rect.copy()

class AnimationSprite (Sprite):
    def __init__(self, pos, frames, groups, vitesse_animation = VITESSE_ANIMATION):
        self.frames, self.frame_index = frames , 0
        super().__init__(pos, self.frames[self.frame_index], groups)     
        self.vitesse_animation = vitesse_animation
    #Animation des objets
    def animer (self,dt):
        self.frame_index += self.vitesse_animation*dt
        self.image = self.frames[int(self.frame_index % len(self.frames))]

    def update (self, dt) :
        self.animer(dt)


class MovingSprite(AnimationSprite):

    def __init__(self,frames, groups,start_pos,end_pos,move_dir,vitesse):
        super().__init__(start_pos, frames, groups)
        if move_dir == 'x':
            self.rect.midleft = start_pos
        else :
            self.rect.midtop = start_pos   
        
        self.start_pos = start_pos
        self.end_pos = end_pos

        # Mouvement 
        self.vitesse = vitesse
        self.direction = vector(1,0) if move_dir== 'x' else vector (0,1)
        self.move_dir = move_dir

    # Vérification de la bordure de l'objet en mouvement
    def check_border(self):
        if self.move_dir == 'x': #Horizontal
            if self.rect.right >= self.end_pos[0] and self.direction.x == 1:
                self.direction.x = -1
                self.rect.right = self.end_pos[0]
            if self.rect.left <= self.start_pos[0] and self.direction.x == -1:
                self.direction.x = 1
                self.rect.left = self.start_pos[0]    
        else : # Verticale
            if self.rect.bottom >= self.end_pos[1] and self.direction.y == 1:
                self.direction.y = -1
                self.rect.bottom = self.end_pos[1]
            if self.rect.top <= self.start_pos[1] and self.direction.y == -1:
                self.direction.y = 1
                self.rect.top = self.start_pos[1] 

    def update (self,dt):
        self.old_rect = self.rect.copy()
        self.rect.topleft += self.direction * self.vitesse * dt
        self.check_border()
        self.animer(dt)

