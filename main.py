from settings import *
from level import Level
from pytmx.util_pygame import load_pygame
import os
from aide import *
from menu import Menu,Button 
import pymunk
import math
from fenetre import * 


space=pymunk.Space()          #création d'un espace pymunk
clock=pygame.time.Clock()
body=pymunk.Body(body_type=pymunk.Body.DYNAMIC) #dynamic=réagie au collisions et sont affectées par d'autres forces
FPS=80                        #nombre d'images par secondes
u_statique=0.9                #coefficient de frottement statique
masse=0.05                    #masse de la balle
liste_lignes_niveau0 =[]      #liste des lignes du niveau 0
liste_bodies_niveau0 =[]      #liste des bodies du niveau 0
liste_lignes_niveau1 =[]      #liste des lignes du niveau 1
liste_bodies_niveau1 = []     #listes des bodies du niveau 1
liste_lignes_niveau2 = []     #liste des lignes du niveau 2
liste_bodies_niveau2 = []     #liste des bodies du niveau 2
points_total = 100            #Nombre de points maximal
x_balle_ini =95               #position de la balle initiale en x
y_balle_ini=550               #position de la balle initiale en y
#création de l'objet qui bouge
obs_body=pymunk.Body(body_type=pymunk.Body.KINEMATIC)    
obs_shape=pymunk.Circle(obs_body, 7)


#classe Ligne (pour créer des objets pymunk pour délimiter notre fenêtre)
class Ligne:
    def __init__(self, pt_ini, pt_fin):
        self.pt_ini=pt_ini
        self.pt_fin=pt_fin
        
    def creer_ligne(self):
        segment_body=pymunk.Body(body_type=pymunk.Body.STATIC) #objets statiques
        segment_shape=pymunk.Segment(segment_body, self.pt_ini, self.pt_fin, 2)
        segment_shape.elasticity=1
        segment_shape.friction=1
        space.add(segment_body, segment_shape)
        return segment_body,segment_shape

    #sert à enlever les lignes lorsqu'on change de niveau
    def enlever_ligne(self,seg_body,seg_shape):
        space.remove(seg_body,seg_shape) 

    #sert à dessiner chaque ligne si on veut les voir sur l'interface
    def draw(self, display):
        pygame.draw.line(display, (255,0,0), convert_coordinates(self.pt_ini), convert_coordinates(self.pt_fin), 2)


#côtés de la fenêtre
md=Ligne((1155,0), (1155,800))
md.creer_ligne()

mg=Ligne((0,0), (0,800))
mg.creer_ligne()

mh=Ligne((0,800), (1155,800))
mh.creer_ligne()


def creer_niveau0(): #niveau facile
    #on va creer plusieurs lignes pour pouvoir délimiter notre fenêtre
    #délimitation du sol
    l1=Ligne((0,375), (230, 375))
    l1b = l1.creer_ligne()

    l2=Ligne((230,375), (313, 290))
    l2b = l2.creer_ligne()

    l3=Ligne((313, 290), (610, 290))
    l3b = l3.creer_ligne()

    l4=Ligne((610, 290), (695,377))
    l4b = l4.creer_ligne()

    l5=Ligne((695,377), (885, 377))
    l5b = l5.creer_ligne()

    l6=Ligne((885, 377), (968, 460))
    l6b = l6.creer_ligne()

    l7=Ligne((968,460), (1134, 460))
    l7b = l7.creer_ligne()

    #délimitation du trou
    g_trou=Ligne((1134, 460), (1134, 442))
    g_troub = g_trou.creer_ligne()

    b_trou=Ligne((1134,442), (1155,442))
    b_troub = b_trou.creer_ligne()

    #délimitation de la platform
    plat_flot_inf=Ligne((400,455), (503,455))
    plat_flot_infb = plat_flot_inf.creer_ligne()

    plat_flot_sup=Ligne((400,460), (503,460))
    plat_flot_supb = plat_flot_sup.creer_ligne()

    #délimitation des briques
    b1=Ligne((758,377), (758,400))
    b1b = b1.creer_ligne()

    b2=Ligne((758,399), (776, 399))
    b2b = b2.creer_ligne()

    b3=Ligne((778,399), (778, 421))
    b3b = b3.creer_ligne()

    b4=Ligne((778,420), (796, 420))
    b4b = b4.creer_ligne()

    b5=Ligne((796,420), (796, 400))
    b5b = b5.creer_ligne()

    b6=Ligne((796,400), (816, 400))
    b6b = b6.creer_ligne()

    b7=Ligne((816,400), (816,377))
    b7b = b7.creer_ligne()

    #délimitation des l'objet qui bouge
    obs_body.position= 1039,600   
    obs_shape.elasticity=1 
    obs_shape.friction=1

    #Liste des lignes du niveau 0
    global liste_lignes_niveau0
    global liste_bodies_niveau0
    liste_lignes_niveau0 = [l1,l2,l3,l4,l5,l6,l7,g_trou,b_trou,plat_flot_inf,plat_flot_sup,b1,b2,b3,b4,b5,b6,b7]
    #Liste des "bodies" associés aux lignes du niveau 0
    liste_bodies_niveau0 = [l1b,l2b,l3b,l4b,l5b,l6b,l7b,g_troub,b_troub,plat_flot_infb,plat_flot_supb,b1b,b2b,b3b,b4b,b5b,b6b,b7b]

creer_niveau0()


def creer_niveau1(): #niveau moyen
    space.gravity = 0, -300    #Changement de la force gravitationnelle

    #Delimitation du sol
    ligne1 = Ligne((0,295),(190,295))
    ligne1b = ligne1.creer_ligne()

    ligne2 = Ligne((190,295),(250,350))
    ligne2b = ligne2.creer_ligne()

    ligne3 = Ligne((250,355),(400,355))
    ligne3b =ligne3.creer_ligne()

    ligne4 = Ligne((400,355),(520,230))
    ligne4b = ligne4.creer_ligne()

    ligne5 = Ligne((520,230),(800,230))
    ligne5b = ligne5.creer_ligne()

    ligne6 = Ligne((800,230),(970,400))
    ligne6b = ligne6.creer_ligne()

    ligne7 = Ligne((970,400),(1070,400))
    ligne7b = ligne7.creer_ligne()

    ligne8 = Ligne((1070,400),(1120,350))
    ligne8b = ligne8.creer_ligne()

    ligne9 = Ligne((1110,360),(1135,360))
    ligne9b = ligne9.creer_ligne()

    ligne10 = Ligne((1135,360),(1135,340))
    ligne10b = ligne10.creer_ligne()

    ligne11 = Ligne((1135,340),(1155,340))
    ligne11b = ligne11.creer_ligne()

    #Vaisseau spaciale bleu
    ligne12 = Ligne((655,265),(660,290))
    ligne12b = ligne12.creer_ligne()

    ligne13 = Ligne((660,290),(650,295))
    ligne13b = ligne13.creer_ligne()

    ligne14 = Ligne((650,295),(649,315))
    ligne14b = ligne14.creer_ligne()

    ligne15 = Ligne((649,315),(660,320))
    ligne15b = ligne15.creer_ligne()

    ligne16 = Ligne((660,320),(654,342))
    ligne16b = ligne16.creer_ligne()

    ligne17 = Ligne((654,342),(683,360))
    ligne17b = ligne17.creer_ligne()

    ligne18 = Ligne((683,360),(705,315))
    ligne18b = ligne18.creer_ligne()

    ligne19 = Ligne((705,315),(725,308))
    ligne19b = ligne19.creer_ligne()

    ligne20 = Ligne((725,308),(725,300))
    ligne20b = ligne20.creer_ligne()

    ligne21 = Ligne((725,300),(705,295))
    ligne21b = ligne21.creer_ligne()

    ligne22 = Ligne((705,295),(683,250))
    ligne22b = ligne22.creer_ligne()

    ligne23 = Ligne((683,250),(655,265))
    ligne23b = ligne23.creer_ligne()

    #Vaisseau spaciale rouge
    ligne24 = Ligne((1005,433),(1025,433))
    ligne24b = ligne24.creer_ligne()

    ligne25 = Ligne((1005,433),(1002,440))
    ligne25b = ligne25.creer_ligne()

    ligne26 = Ligne((1002,440),(970,447))
    ligne26b = ligne26.creer_ligne()

    ligne27 = Ligne((970,447),(966,475))
    ligne27b = ligne27.creer_ligne()

    ligne28 = Ligne((966,475),(976,465))
    ligne28b = ligne28.creer_ligne()

    ligne29 = Ligne((976,465),(1005,480))
    ligne29b = ligne29.creer_ligne()

    ligne30 = Ligne((1005,480),(1007,505))
    ligne30b = ligne30.creer_ligne()

    ligne31 = Ligne((1007,505),(1023,505))
    ligne31b = ligne31.creer_ligne()

    ligne32 = Ligne((1023,505),(1025,480))
    ligne32b = ligne32.creer_ligne()

    ligne33 = Ligne((1025,480),(1055,465))
    ligne33b = ligne33.creer_ligne()

    ligne34 = Ligne((1055,465),(1064,475))
    ligne34b = ligne34.creer_ligne()

    ligne35 = Ligne((1064,475),(1062,447))
    ligne35b = ligne35.creer_ligne()

    ligne36 = Ligne((1062,447),(1030,441))
    ligne36b = ligne36.creer_ligne()

    ligne37 = Ligne((1030,441),(1025,433))
    ligne37b = ligne37.creer_ligne()

    #Liste de lignes du niveau 1
    global liste_lignes_niveau1
    liste_lignes_niveau1 = [ligne1,ligne2,ligne3,ligne4,ligne5,ligne6,ligne7,ligne8,ligne9,ligne10,ligne11,ligne12,ligne13,
                            ligne14,ligne15,ligne16,ligne17,ligne18,ligne19,ligne20,ligne21,ligne22,ligne23,ligne24,
                            ligne25,ligne26,ligne27,ligne28,ligne29,ligne30,ligne31,ligne32,ligne33,ligne34,ligne35,ligne36,
                            ligne37]
    #Liste des "bodies" associés aux lignes du niveau 1
    global liste_bodies_niveau1
    liste_bodies_niveau1 = [ligne1b,ligne2b,ligne3b,ligne4b,ligne5b,ligne6b,ligne7b,ligne8b,ligne9b,ligne10b,ligne11b,ligne12b,
                            ligne13b,ligne14b,ligne15b,ligne16b,ligne17b,ligne18b,ligne19b,ligne20b,ligne21b,ligne22b,ligne23b,
                            ligne24b,ligne25b,ligne26b,ligne27b,ligne28b,ligne29b,ligne30b,ligne31b,ligne32b,ligne33b,ligne34b,
                            ligne35b,ligne36b,ligne37b]


def creer_niveau2(): #niveau difficile
    global u_statique   
    u_statique = 0.04 #changement du coefficient de frottement statique
    space.gravity = 0, -700

    #-------DELIMITATION POUR LE NIVEAU 2 (GLACE)--------
    #Sol du bas
    ligne1 = Ligne((0,274),(502,274))
    ligne1b =ligne1.creer_ligne()

    ligne2 = Ligne((502,274),(605,170))
    ligne2b = ligne2.creer_ligne()

    ligne3 = Ligne((605,169),(1155,169))
    ligne3b = ligne3.creer_ligne()

    #sol du haut
    ligne4 = Ligne((0,420),(212,420))
    ligne4b = ligne4.creer_ligne()

    ligne5 = Ligne((270,420),(505,420))
    ligne5b = ligne5.creer_ligne()

    ligne6 = Ligne((505,420),(626,297))
    ligne6b = ligne6.creer_ligne()

    ligne7 = Ligne((626,294),(820,294))
    ligne7b = ligne7.creer_ligne()

    ligne8 = Ligne((820,294),(1051,526))
    ligne8b = ligne8.creer_ligne()

    ligne9 = Ligne((1051,526),(1132,526))
    ligne9b = ligne9.creer_ligne()

    #Delimitation du trou
    ligne10 = Ligne((1132,526),(1132,508))
    ligne10b = ligne10.creer_ligne()

    ligne11 = Ligne((1132,508),(1155,508))
    ligne11b = ligne11.creer_ligne()

    #Plafond
    ligne12 = Ligne((0,400),(196,400))
    ligne12b = ligne12.creer_ligne()

    ligne13 = Ligne((287,400),(483,400))
    ligne13b = ligne13.creer_ligne()

    ligne14 = Ligne((483,400),(630,255))
    ligne14b = ligne14.creer_ligne()

    ligne15 = Ligne((630,255),(1155,255))
    ligne15b = ligne15.creer_ligne()

    ligne16 = Ligne((196,400),(212,420))
    ligne16b = ligne16.creer_ligne()

    ligne17 = Ligne((270,420),(287,400))
    ligne17b = ligne17.creer_ligne()

    #Bloques
    ligne18 = Ligne((735,169),(735,191))
    ligne18b = ligne18.creer_ligne()

    ligne19 = Ligne((735,191),(755,191))
    ligne19b = ligne19.creer_ligne()

    ligne20 = Ligne((755,191),(755,211))
    ligne20b = ligne20.creer_ligne()

    ligne21 = Ligne((755,211),(775,211))
    ligne21b = ligne21.creer_ligne()

    ligne22 = Ligne((775,211),(775,191))
    ligne22b = ligne22.creer_ligne()

    ligne23 = Ligne((775,191),(795,191))
    ligne23b = ligne23.creer_ligne()

    ligne24 = Ligne((795,191),(795,169))
    ligne24b = ligne24.creer_ligne()

    #Iglou
    ligne25 = Ligne((0,300),(18,316))
    ligne25b = ligne25.creer_ligne()

    ligne26 = Ligne((18,316),(48,316))
    ligne26b = ligne26.creer_ligne()

    ligne27 = Ligne((48,316),(60,300))
    ligne27b = ligne27.creer_ligne()

    ligne28 = Ligne((60,300),(60,270))
    ligne28b = ligne28.creer_ligne()

    #Bonhomme de neige
    ligne29 = Ligne((720,420),(750,420))
    ligne29b = ligne29.creer_ligne()

    ligne30 = Ligne((710,400),(720,420))
    ligne30b = ligne30.creer_ligne()
    
    ligne31 = Ligne((710,382),(710,400))
    ligne31b = ligne31.creer_ligne()

    ligne32 = Ligne((710,382),(715,375))
    ligne32b = ligne32.creer_ligne()

    ligne33 = Ligne((680,294),(715,375))
    ligne33b = ligne33.creer_ligne()

    ligne34 = Ligne((750,420),(765,400))
    ligne34b = ligne34.creer_ligne()

    ligne35 = Ligne((765,400),(780,403))
    ligne35b = ligne35.creer_ligne()

    ligne36 = Ligne((765,400),(765,382))
    ligne36b = ligne36.creer_ligne()

    ligne37 = Ligne((765,382),(755,372))
    ligne37b = ligne37.creer_ligne()

    ligne38 = Ligne((755,372),(790,294))
    ligne38b = ligne38.creer_ligne()



    global liste_lignes_niveau2
    global liste_bodies_niveau2
    #Liste de lignes pour le niveau 2
    liste_lignes_niveau2 = [ligne1,ligne2,ligne3,ligne4,ligne5,ligne6,ligne7,ligne8,ligne9,ligne10,ligne11,ligne12,ligne13,
                        ligne14,ligne15,ligne16,ligne17,ligne18,ligne19,ligne20,ligne21,ligne22,ligne23,ligne24,ligne25,
                        ligne26,ligne27,ligne28,ligne29,ligne30,ligne31,ligne32,ligne33,ligne34,ligne35,ligne36,ligne37,ligne38]
    #Liste des "bodies" associés aux lignes du niveau 2
    liste_bodies_niveau2 = [ligne1b,ligne2b,ligne3b,ligne4b,ligne5b,ligne6b,ligne7b,ligne8b,ligne9b,ligne10b,ligne11b,ligne12b,ligne13b,
                        ligne14b,ligne15b,ligne16b,ligne17b,ligne18b,ligne19b,ligne20b,ligne21b,ligne22b,ligne23b,ligne24b,ligne25b,
                        ligne26b,ligne27b,ligne28b,ligne29b,ligne30b,ligne31b,ligne32b,ligne33b,ligne34b,ligne35b,ligne36b,ligne37b,ligne38b]



#Permet de calculer le nombre de points du joueur
def calcul_de_points(nombre_coups):
    global points_total
    if nombre_coups < 20: 
        points = points_total - nombre_coups*5 #Enlève 5 points pour chaque coup
    else:
        #Si le joueur fait 20 coups ou plus, il n'a pas de points pour le niveau. 
        points = 0
    return points   #points_total


#permet de convertir les coordonnées pymunk en coordonnées pygame
def convert_coordinates(point):
    return point[0], 800-point[1]

#permet de trouver la force apliquer sur la balle
def trouver_force(xa,xb,ya,yb):
    forceX = xb-xa 
    forceY = (yb-ya)
    force = (math.sqrt(pow(forceX,2) + pow(forceY,2))) 

    #Si la force est plus grande que 200, on le met à 200.
    #Force limite que le joueur peut donner à la balle
    if force>200:
        force=200
    return force


def trouver_angle(xa,xb,ya,yb):
    compX = xb-xa
    compY = -(yb-ya)
    try:
        angle =  math.degrees(math.atan(compY/compX)) 
    except:
        print("exception")
    
    #determiner le cadran pour trouver la vraie angle
    if compX > 0 and compY > 0:
        angle = 180 + abs(angle)
    elif compX < 0 and compY > 0:
        angle = 360 - abs(angle)
    elif compX < 0 and compY < 0:
        angle = abs(angle)
    else:
        angle = 180 - abs(angle)    
    return angle    


def calcul_force_balle(force,angle):
    #nous permet de trouver la force en x et y appliquée sur la balle
    fx=(force*math.cos(angle*(math.pi/180)))*3 
    fy=force*math.sin(angle*(math.pi/180))*3
    return fx,fy



class Jeu:
    level_picked = False        #Détermine si le niveau a été choisi
    level_number = 0            #Numero du niveau
    credits_ouvert = False      #Détermine si la fenêtre de crédit est ouverte
    #Texte dans les crédits
    texte_noms = "Projet par Mia Matsumoto-Depatie, Jenny Alejandra Eslava Bonilla" 
    texte_noms_suite = "et Alexandra Yeghiayan"
    texte_approuver = "Projet approuvée par Cynthia Genest Beaulieu"
    texte_sources_titre = "Sources:"
    texte_sources_1 = "Clear code,(2024, 11 février).Creating 2D platformer in Python [vidéo]. Youtube. https://www.youtube.com/watch?v=WViyCAa6yLI&t=10477s "
    texte_sources_2 = "Pygame. Pygame documentation. Pygame. https://www.pygame.org/docs/ "
    texte_sources_3 = "techwithtim. (2024, 15 février). Projectile-Motion-Physics-Engine. GitHub.​ https://github.com/techwithtim/Projectile-Motion-Physics-Engine/blob/master/projectile_motion.py ​"
    texte_sources_4 = "Ear Of Corn Programming. (27 juin 2020). Pymunk Basics: Bouncing Ball [vidéo]. Youtube. https://www.youtube.com/watch?v=nNjRz31-7s0​"
    texte_sources_5 = "Pymunk. (s.d.). Source code for pymunk.body. https://www.pymunk.org/en/latest/_modules/pymunk/body.html ​" 
    texte_sources_6="Coding With Russ. (12 février 2023). Displaying Text on The Screen In Pygame - Beginner Tutorial [vidéo]. Youtube. https://www.youtube.com/watch?v=ndtFoWWBAoE "

    space.gravity=0, -700                    #gravité
    body.position= x_balle_ini,y_balle_ini   #position initiale de la balle
    shape=pymunk.Circle(body, 7)             #shape=cercle
    shape.density=1                          #densité de la ball de golf
    shape.elasticity=0.3                     #elasticité de la balle de golf (très peu élastic)
    shape.friction=1
    space.add(body, shape)                   #ajouter la balle dans l'espace

    #ajout de la scie en mouvement dans le niveau 0
    space.add(obs_body,obs_shape)
    mouse_drag=False
    run = True    
    x_flag = 0
    y_flag_min =0
    y_flag_max =0
    nb_coups=0
    start_moving_ball = False

    #Constructeur du jeu
    def __init__(self):
        #Création d'une fênetre
        pygame.init()
        self.display_surface = pygame.display.set_mode((LONGUEUR_FENETRE,LARGEUR_FENETRE))
        pygame.display.set_caption("Golf")
        self.clock = pygame.time.Clock()
        self.import_graph()
        self.button_aide = Button(1111, 25,"",TAILLE_TILE,TAILLE_TILE)

        #fichier pour les différents interfaces graphiques
        self.tmx_maps = {
            0: load_pygame('./data/tmx/0.tmx'),
            1: load_pygame('./data/tmx/1.tmx'),
            2: load_pygame('./data/tmx/2.tmx'),
            }
        
        
        self.tmx_fenetre = (load_pygame('./data/tmx/3.tmx'))
        self.tmx_fenetre_niveaux = (load_pygame('./data/tmx/4.tmx'))
        self.tmx_menu = (load_pygame('./data/tmx/menu.tmx'))


        self.fenetre_niveaux = FenetreNiveaux(self.tmx_fenetre_niveaux,self.switch_stage)
        self.fenetre = Fenetre(self.tmx_fenetre, self.switch_stage)
        self.current_stage= Menu(self.tmx_menu, self.switch_stage)


    #Applique le frottement sur la balle lors d'une collision
    def post_solve(arbiter: pymunk.Arbiter, space, data):
        body.angular_velocity *= (1-u_statique)


    #Vérification de toutes les collisions
    handler = space.add_default_collision_handler()
    handler.post_solve = post_solve
 
    #trace la ligne de force donnée par le joueur
    def tracer_ligne(self,tracer):
        if tracer == True:
            couleur = "black"
            if Jeu.level_number==1:
                couleur = "white" #Il faut changer la couleur de la ligne pour le niveau sur la ligne pour que le joueur puisse le voir.
            pygame.draw.line(self.display_surface,couleur,Jeu.line[0],Jeu.line[1],width=2)
        elif tracer == False:
            Jeu.line.clear  

    #Importer les graphiques 
    def import_graph(self):
        self.level_frames = {
            'redflag' : import_fichier('./tiles/animation/redflag'),
            'greenflag' : import_fichier('./tiles/animation/greenflag'),
            'blueflag' : import_fichier('./tiles/animation/blueflag'),
            'yellowflag' : import_fichier('./tiles/animation/yellowflag'),
            'scie_chain' : import_image('./tiles/objets/scie_chain'),
            'scie' : import_fichier('./tiles/animation/scie')
            
        }


    #affichage de texte sur l'écran
    pygame.font.init()
    texte_font = pygame.font.SysFont("Arial",20)

    #fonction qui permet d'afficher le texte sur l'écran
    def draw_text(self,text,font,couleur_texte,x,y):
        img = font.render(text,True,couleur_texte)
        self.display_surface.blit(img,(x,y))

    #fonction qui nous permet d'enlever les objets statiques délimitant un niveau lorsqu'on change de niveau
    def enlever_delimitation(numero_niveau):
        liste_bodies_enlever = liste_bodies_niveau0
        liste_lignes_enlever = liste_lignes_niveau0
        if numero_niveau == 0:
            liste_bodies_enlever = liste_bodies_niveau0
            liste_lignes_enlever = liste_lignes_niveau0
            space.remove(obs_body,obs_shape)
        elif numero_niveau == 1:
            liste_bodies_enlever = liste_bodies_niveau1
            liste_lignes_enlever = liste_lignes_niveau1
        else:
            liste_bodies_enlever = liste_bodies_niveau2
            liste_lignes_enlever = liste_lignes_niveau2
        
        for i in range(len(liste_lignes_enlever)):    #boucle qui enleve les lignes du niveau de l'espace Pymunk
            seg_bod = liste_bodies_enlever[i][0]
            seg_shap = liste_bodies_enlever[i][1]
            liste_lignes_enlever[i].enlever_ligne(seg_bod,seg_shap)

    # Méthode pour changer de fenêtre
    def switch_stage(self,target,current_level):
        if target == 'level':
            if current_level == 0:
                self.current_stage = Level(self.tmx_maps[0], self.level_frames, self.switch_stage)
                obs_body.position= 1039,600 
            elif current_level == 1:
                self.current_stage = Level(self.tmx_maps[1], self.level_frames, self.switch_stage)
            elif current_level == 2:
                self.current_stage = Level(self.tmx_maps[2], self.level_frames, self.switch_stage)    
            Jeu.level_picked = True
                
        elif target == 'menu':
            if current_level ==5:
                self.current_stage = Menu(self.tmx_menu,self.switch_stage)
                Jeu.credits_ouvert=False

                #Réinitialise le niveau 0 (facile)
                Jeu.nb_coups = 0
                body.position = x_balle_ini, y_balle_ini
                space.gravity = 0,-700
                Jeu.enlever_delimitation(Jeu.level_number)
                space.add(obs_body,obs_shape)
                Jeu.level_number=0
                global u_statique
                u_statique = 0.9
                creer_niveau0()
                Jeu.level_picked=False
                Jeu.start_moving_ball=False 

        elif target == 'fenetre':
            if current_level ==3:   
                self.current_stage = Fenetre(self.tmx_fenetre, self.switch_stage)
                Jeu.credits_ouvert = True

            elif current_level ==4:
                self.current_stage = FenetreNiveaux(self.tmx_fenetre_niveaux, self.switch_stage)
                Jeu.level_picked= False
                body.position = x_balle_ini,y_balle_ini
                Jeu.nb_coups=0
                 

    # Boucle du jeu 
    def run(self):
        while Jeu.run:
            x,y = convert_coordinates(body.position) #position de la balle en coordonnées pygame
            x_obs,y_obs = convert_coordinates(obs_body.position) #position de l'obstacle qui bouge en coordonnées pygame  
            dx= pygame.mouse.get_pos()[0]-x
            dy = pygame.mouse.get_pos()[1]-y
            Jeu.line = [((x,y)),((x-dx,y-dy))] #création de la ligne de force déterminé par le joueur en fonction du positionnement de la souris

            #calcul d'énergie
            vitesse = math.sqrt(body.velocity[0]**2 + body.velocity[1]**2)
            energie = 0.5*masse*(vitesse**2)
            text_energie = "Énergie: " + str(round(energie,1))  + " J"

            #nombre de coups
            text_nb_coups = "Nombre de coups: " + str(Jeu.nb_coups)


            if Jeu.level_picked:
                Jeu.tracer_ligne(self,Jeu.mouse_drag) #dessiner la ligne de force
                pygame.draw.circle(self.display_surface, (255, 255, 255), (int(x), int(y)), 7) #dessiner la balle de golf
                #Affichage du texte sur l'écran
                Jeu.draw_text(self,text_nb_coups,Jeu.texte_font,(0,0,0),10,670)
                Jeu.draw_text(self,text_energie,Jeu.texte_font,(0,0,0),10,700)


                #mouvement de l'obstacle
                if Jeu.start_moving_ball == False:
                    obs_body.velocity = (0,-80)
                    Jeu.start_moving_ball=True
                
                if y_obs>317:
                    obs_body.velocity = (0,80)    
                elif y_obs<199:
                    obs_body.velocity = (0,-80) 


            #Affiche le texte pour les crédits
            if Jeu.credits_ouvert:  
                font_credits =  pygame.font.SysFont("Arial ",8)
                Jeu.draw_text(self,Jeu.texte_noms, Jeu.texte_font,(0,0,0),330,180)
                Jeu.draw_text(self,Jeu.texte_noms_suite, Jeu.texte_font,(0,0,0),490,210)
                Jeu.draw_text(self,Jeu.texte_approuver, Jeu.texte_font,(0,0,0),400,260)
                Jeu.draw_text(self,Jeu.texte_sources_titre, Jeu.texte_font,(0,0,0),270,300)
                Jeu.draw_text(self,Jeu.texte_sources_1, font_credits,(0,0,0),255,340)
                Jeu.draw_text(self,Jeu.texte_sources_2, font_credits,(0,0,0),255,370)
                Jeu.draw_text(self,Jeu.texte_sources_3, font_credits,(0,0,0),255,400)
                Jeu.draw_text(self,Jeu.texte_sources_4, font_credits,(0,0,0),255,430)
                Jeu.draw_text(self,Jeu.texte_sources_5, font_credits,(0,0,0),255,460)
                Jeu.draw_text(self,Jeu.texte_sources_6, font_credits,(0,0,0),255,490)

        
            #position du trou dépendant du niveau
            if Jeu.level_number==0:
                Jeu.x_flag =1140
                Jeu.y_flag_min = 345
                Jeu.y_flag_max = 350


            elif Jeu.level_number==1:  
                Jeu.x_flag = 1140
                Jeu.y_flag_min = 440
                Jeu.y_flag_max = 460


            elif Jeu.level_number==2:
                Jeu.x_flag = 1140
                Jeu.y_flag_min = 280
                Jeu.y_flag_max = 292
                

            pygame.display.update()
            dt = self.clock.tick(80)/1000
            space.step(1/FPS)


            #Calcul de la condition de victoire
            if x > Jeu.x_flag and (y<jeu.y_flag_max and y>Jeu.y_flag_min):
                print("Nombre de coups: ", Jeu.nb_coups, "Points: ", calcul_de_points(Jeu.nb_coups)) #afficher le nombre de coups et les points dans le terminal
                Jeu.enlever_delimitation(Jeu.level_number) #enlever les délimitations du jeu dépendant du niveau 

                #changer le niveau
                if Jeu.level_number == 0:
                    self.switch_stage('level',1)
                    Jeu.level_number=1
                    Jeu.nb_coups=0
                    x_balle_ini =90
                    y_balle_ini=390
                    body.position = x_balle_ini,y_balle_ini
                    creer_niveau1() 

                elif Jeu.level_number == 1:
                    self.switch_stage('level',2)
                    Jeu.level_number=2
                    Jeu.nb_coups=0
                    x_balle_ini =90
                    y_balle_ini=390
                    body.position = x_balle_ini,y_balle_ini
                    creer_niveau2() 

                else:
                    Jeu.run = False  #On ferme le jeu quand le joueur a completé les trois niveaux. 
                
            
            for event in pygame.event.get():
                tirer = False #le balle ne peut pas bouger
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #L'utilisateur pèse sur la souris, donc une flèche va appraitre sur l'écran pour pouvoir donner une force à la balle.
                if event.type == pygame.MOUSEBUTTONDOWN and Jeu.level_picked==True and energie<0.1:
                    Jeu.mouse_drag = True
                    tirer=False

                if event.type == pygame.MOUSEBUTTONUP and Jeu.level_picked==True and energie<0.1:
                    Jeu.mouse_drag = False
                    if tirer == False:  
                        Jeu.nb_coups=Jeu.nb_coups+1 #incrémente le nombre de coups
                        pos_x = body.position[0] #position en x de la balle
                        pos_y=800-body.position[1] #poisition en y de la balle
                        pos = pygame.mouse.get_pos() #position de la souris
                        tirer=True #la balle peut maintenant bouger

                        #calcul de la force et de l'angle
                        force = trouver_force(pos_x,pos[0],pos_y,pos[1])
                        angle = trouver_angle(pos_x,pos[0],pos_y,pos[1])
                        force_balle = calcul_force_balle(force,angle)
                        body.velocity=(force_balle[0],force_balle[1]) #vitesse de la balle est proportionnelle à la force


            self.current_stage.run(dt)
                
            

if __name__ == '__main__' : 
    jeu = Jeu()
    jeu.run()
