
import pygame
from pygame.locals import *

pygame.init()

def menu():
        
        fond_menu = pygame.image.load("ressource/image/Menu.png")
        son_menu = pygame.mixer.Sound("ressource/son/Rouge.wav")

        fenetre = pygame.display.set_mode((800, 600))           #ouverture d'une fenetre , collage de l'image , rafraichissement
        fenetre.blit(fond_menu, (0, 0))                                 
        pygame.display.flip()

        son_menu.play()                 #fonction pour lancer la musique
        
        continuer = 1                   #boucle infinie pour que le jeu tourne
        while continuer:
                for event in pygame.event.get():                #Attente des événements
                        if event.type == QUIT :                 #fermeture en mettant fin a la boucle
                                continuer = 0
                                pygame.quit()

                        if event.type == KEYDOWN:               #gestion du son
                                if event.key == K_p:
                                        son_menu.play()
                                if event.key == K_o:
                                        son_menu.stop()

                        if event.type == MOUSEBUTTONUP and event.button == 1:
                                if event.pos[0] > 264 and event.pos[0] < 511 and event.pos[1] > 332 and event.pos[1] < 446:     #on lance en mode solo/multi en definissant
                                        son_menu.stop()                                                                         #une zone ou faire un clic gauche lance 
                                        main_MULTI()                                                                            #l'une des fonction respective
                                if event.pos[0] > 260 and event.pos[0] < 365 and event.pos[1] > 190 and event.pos[1] < 226:
                                        son_menu.stop()
                                        main_SOLO()
                                        
#===========================================================================                        
        
        
def refresh(fenetre, fond, position_fond, zombie, zombie2, position_zombie, leroux, leroux2, position_leroux, animzby, animroux, findugame):

        #Re-collage
        fenetre.blit(fond, position_fond)                                       #recolle du fond a chaque tour de boucle
        if findugame == 0 :                                                     #condition respécté si le jeu n'est pas fini

                if animroux % 2 == 0 :
                    fenetre.blit(leroux, position_leroux)                       #gestion des animations grace a un compteur qui affiche 2 image en décalé
                else :
                    fenetre.blit(leroux2, position_leroux)


                if animzby % 2 == 0 :
                    fenetre.blit(zombie, position_zombie)
                else :
                    fenetre.blit(zombie2, position_zombie)

        if findugame == 1:
                 for event in pygame.event.get():                               #Attente des événements
                        if event.type == KEYDOWN and event.key == K_r:          #si le jeu est fini , R permet un retour au menu
                                menu()


        #Rafraichissement
        pygame.display.flip()                                                   #actualisation          

#===============================================================================        

def create_texture(chemin, alpha):
        if alpha:
                return pygame.image.load(chemin).convert_alpha()                        #création de 2 fonction permettant d'introduire directement les ressources son et image
        else:
                return pygame.image.load(chemin).convert()

def create_sound(chemin):
        return pygame.mixer.Sound(chemin)
                

#===============================================================================
def main_SOLO():

        soundtrack = create_sound("ressource/son/texas.wav")
        zombie_sound = create_sound("ressource/son/zombie_sound.wav")           

        fond = create_texture("ressource/image/SCROLL FINAL.png", 1)
        position_fond = fond.get_rect()

        zombie = create_texture("ressource/image/MRZBY.png", 1)
        position_zombie = zombie.get_rect()
        zombie2 = create_texture("ressource/image/MRZBY2.png", 1)
        
        leroux = create_texture("ressource/image/LEROUX.png", 1)
        position_leroux = leroux.get_rect()
        leroux2 = create_texture("ressource/image/LEROUX2.png", 1)

        findugame = 0                   #gestion de fin pour empecher les deplacement apres la victoire d'un joueur
        d_parcourue = 0                 #valeur que l'on soustrait lors de la teleportation vers l'ecran de fin si victoire du zombie
        animzby = 0                     #gestion de l'animation 1 pas sur 2
        animroux = 0

        position_zombie = position_zombie.move(400,525)         # deplacement des personnages a leurs positions initiales
        position_leroux = position_leroux.move(600,525)

        fenetre = pygame.display.set_mode((1280, 720))
        zombie_sound.play()
        soundtrack.play()

        continuer = 1

        #Boucle time pour faire avancer le zby
        while continuer:

                if findugame == 0:
                        pygame.time.Clock().tick(30)            #limitation du nombre de "tours" par sec
                        boucle = pygame.time.get_ticks()        # boucle time agit comme un generateur de nombre aleatoires , lorsqu'il s'agit de multiples de 4 , le zombie avance

                        if boucle % 3 == 0:
                               position_zombie = position_zombie.move(20,0)
                               animzby += 1
                        #gestion de fin
                        if position_zombie == position_leroux  :
                                findugame += 1
                                position_fond = position_fond.move(-5800 + d_parcourue, 0)
                                zombie_sound.stop()
                                soundtrack.stop()
                                              

                for event in pygame.event.get():        #Attente des événements
                        if event.type == QUIT :
                                continuer = 0

                        if event.type == KEYDOWN and findugame == 0 :   #type d'evenement attendu

                                # Musiques de fond
                                 if event.key == K_p:
                                         zombie_sound.play()
                                         soundtrack.play()
                                 if event.key == K_o:
                                         zombie_sound.stop()
                                         soundtrack.stop()
                                #Si "flèche droite ": On bouge le zombie et le fond

                                 if event.key == K_RIGHT:
                                                 position_zombie = position_zombie.move(-20,0)  #scrolling , au lieu de bouger l'humain , on fait reculer le fond et le zombie
                                                 position_fond = position_fond.move(-20,0)
                                                 d_parcourue += 20      
                                                 animroux += 1

                                # Gestion de Fin
                                 if position_fond == (-2660, 0, 9197, 720) :
                                        findugame+= 1
                                        position_fond = position_fond.move(-1850,0)
                                        zombie_sound.stop()
                                        soundtrack.stop()
                                        
                                
                refresh(fenetre, fond, position_fond, zombie, zombie2, position_zombie, leroux, leroux2, position_leroux, animzby, animroux, findugame)

#============================================================================


def main_MULTI():

        soundtrack = create_sound("ressource/son/texas.wav")
        zombie_sound = create_sound("ressource/son/zombie_sound.wav")

        fond = create_texture("ressource/image/SCROLL FINAL.png", 1)
        position_fond = fond.get_rect()

        zombie = create_texture("ressource/image/MRZBY.png", 1)
        position_zombie = zombie.get_rect()
        zombie2 = create_texture("ressource/image/MRZBY2.png", 1)
        
        leroux = create_texture("ressource/image/LEROUX.png", 1)
        position_leroux = leroux.get_rect()
        leroux2 = create_texture("ressource/image/LEROUX2.png", 1)

        position_zombie = position_zombie.move(530,525)
        position_leroux = position_leroux.move(600,525)

        d_parcourue = 0
        animzby = 0
        animroux = 0
        findugame = 0

        fenetre = pygame.display.set_mode((1450, 720))
        zombie_sound.play()
        soundtrack.play()
        
        continuer = 1
        while continuer:
                for event in pygame.event.get():
                        if event.type == QUIT :
                                continuer = 0

                        if event.type == KEYDOWN and findugame == 0 :

                             
                                 if event.key == K_p:
                                         zombie_sound.play()
                                         soundtrack.play()
                                 if event.key == K_o:
                                         zombie_sound.stop()
                                         soundtrack.stop()
                       

                                 if event.key == K_f:
                                                 position_zombie = position_zombie.move(30,0)
                                                 animzby += 1

                                 if event.key == K_RIGHT:
                                                 position_zombie = position_zombie.move(-20,0)
                                                 position_fond = position_fond.move(-20,0)
                                                 d_parcourue += 20
                                                 animroux += 1
                 


                                 if position_fond == (-2660, 0, 9197, 720) :
                                        findugame+= 1
                                        position_fond = position_fond.move(-1850,0)
                                        zombie_sound.stop()
                                        soundtrack.stop()



                                 if position_zombie == position_leroux  :
                                        findugame+= 1
                                        position_fond = position_fond.move(-5800 + d_parcourue, 0)
                                        zombie_sound.stop()
                                        soundtrack.stop()
 


                                 if event.key == K_f:
                                                 position_zombie = position_zombie.move(-10,0)
                                
                refresh(fenetre, fond, position_fond, zombie, zombie2, position_zombie, leroux, leroux2, position_leroux, animzby, animroux, findugame)

#===================================================================

menu()
